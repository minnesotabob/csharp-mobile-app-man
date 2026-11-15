# Chapter 19
# Local Storage and Database Migrations

A phone may lose its connection, close under memory pressure, or restart after an operating-system update. A visitor returning to Gnazzo's World should still find their saved public catalog and chosen favorites. A reader partway through a sample should not lose their progress simply because the app's process stopped. Persistence is not one feature; it is a collection of contracts about *which information survives*, *who owns it*, *how it changes*, and *what to do when it is unreadable*.

Chapters 12–14 developed a validated public catalog, discovery and a bounded favorites example. Chapter 15 saved an explicitly requested song draft as a local JSON envelope. Chapters 17–18 established a network reader and a small public API. Here we create a real SQLite-backed teaching store using **Microsoft.Data.Sqlite 11.0.0** with **C# 15 and .NET 11**. This store holds a complete validated public catalog document, a set of local favorites, and percentage reading progress. It introduces an upgrade from schema 1 to schema 2 without deleting existing favorites.

We do **not** claim that this file is encrypted, tied to an authenticated account, or ready to persist confidential customer stories. The implementation is registered in the MAUI composition root but does not replace the existing catalog or saved-draft UI. Chapter 20 will decide when downloaded data becomes authoritative, how old a cached snapshot may be, and how pending work survives interrupted connectivity. Chapter 21 will consider synchronization and conflict resolution.

## What You'll Learn

By the end of the chapter, you will be able to:

1. Choose between preferences, local files, secure storage and SQLite using the lifetime and sensitivity of the data.
2. Build parameterized CRUD operations over a real SQLite database, with explicit ownership and cancellation boundaries.
3. Upgrade an existing version-1 database to version 2 inside a transaction while preserving data.
4. Store and recover a whole catalog snapshot without exposing a partially replaced document.
5. Test new-file initialization, data persistence, migrations, rejected writes and future-schema failures using disposable database files.

**Prerequisites:** Chapters 12–18, an SDK matching `global.json`, and the companion source at `work/chapter16-pricing` after the Chapter 19 commits. For an exact comparison, use the code and tests at the same Git commit rather than reading whichever version happens to be on `main`.

**What you will build:** `LocalCatalogDatabase`, a small SQLite database with two schema migrations, and a portable integration suite that runs without an Android emulator. This is a **real local database exercise** with a **deliberately limited production contract**.

## 19.1 Pick a storage mechanism before writing a repository

A familiar temptation is to create one general-purpose storage abstraction for everything. That obscures different requirements. A theme choice is a tiny user preference. A scanned image can be many megabytes. An access token must be handled differently from a public book title. The right first decision is to identify the information and its owner.

| Data | Suitable starting mechanism | Important limitation |
|---|---|---|
| Theme or small filter preference | MAUI Preferences | Small values; not a transactionally related collection |
| Explicitly saved editable request draft | App-data file with versioned envelope | No built-in confidentiality or account ownership |
| API refresh token or small secret | Platform-backed SecureStorage, with threat-model review | Not a general database or a substitute for server-side authorization |
| Public catalog snapshot and relationships | SQLite | Requires validation, schema versioning and freshness rules |
| Favorites and reading progress | SQLite | A local scope label is not an authenticated identity |
| Downloaded cover images | App-managed files and cache metadata | Quota, eviction, rights and stale-image policies |
| Pending customer transaction | Future durable service-backed workflow | Do not confuse offline local acceptance with a completed order |

The Chapter 13 `IFavoriteStore` example uses Preferences so that its bounded set of IDs is easy to inspect. The Chapter 15 `IRequestDraftStore` uses a versioned JSON envelope because a customer explicitly saves one editable request. Neither is automatically a migration target. We can teach a separate SQLite layer before choosing how to move existing state without silently deleting or duplicating it.

**Design decision:** In this chapter, the SQLite file is an *additional local store*. It is not a public API, a payment ledger, an encrypted vault, or a cross-device account database.

### Worked reasoning: why not put the song request in this file now?

An anonymous request may contain names, contact details and personal stories. Changing its storage mechanism does not establish encryption, data retention policy, logout cleanup, lawful access boundaries, or account ownership. It is safer to keep the Chapter 15 workflow explicit and explain that a later protected draft design needs encryption at rest where appropriate, authenticated ownership when synchronized, and a deliberate migration/consent policy. SQLite's file format alone supplies none of those guarantees.

## 19.2 Map the SQL schema to the reader's tasks

Our first schema has two tables:

- `public_catalog` holds one versioned, serialized catalog document. The document is validated before replacement, and contains both catalog items and their creators.
- `favorites` holds stable item IDs keyed by a local `scope`. Favorite rows do not copy titles or artist names.

Schema 2 adds `reading_progress`, keyed by the same `scope` and item ID, with a percentage constrained to 0–100.

The complete source is `src/GnazzosWorld.Core/Storage/LocalCatalogDatabase.cs`. The essential DDL looks like this:

```sql
CREATE TABLE public_catalog (
    singleton INTEGER PRIMARY KEY CHECK(singleton=1),
    revision TEXT NOT NULL,
    payload TEXT NOT NULL
);
CREATE TABLE favorites (
    scope TEXT NOT NULL,
    item_id TEXT NOT NULL,
    PRIMARY KEY(scope, item_id)
);
```

And the second migration adds:

```sql
CREATE TABLE reading_progress (
    scope TEXT NOT NULL,
    item_id TEXT NOT NULL,
    percent INTEGER NOT NULL CHECK(percent BETWEEN 0 AND 100),
    PRIMARY KEY(scope, item_id)
);
```

**Why store the catalog as one document?** Chapter 18 already defines a complete `CatalogDocument` with a schema version, revision, items and creators. Replacing that one validated document atomically is easier to reason about than updating separately serialized records while other readers might observe half a refresh. The compromise is that this small teaching database rewrites the entire public snapshot and does not support efficient SQL searches over every item. For a larger catalog, normalized tables and indexes may be preferable; the import transaction must still preserve a coherent revision.

**Why store favorites as rows?** A composite primary key prevents the same item ID from appearing twice within one scope. Removing a favorite becomes a targeted `DELETE`, and item identity remains independent of translated names.

### Schema invariants

A useful database contract is more precise than "SQLite stores my data":

1. There is at most one current public catalog snapshot.
2. A catalog replacement happens only after the entire incoming document validates.
3. A failed replacement never erases the last successfully committed snapshot.
4. A favorite ID can appear once per local scope and remains stable when its title changes.
5. Progress is between 0 and 100 inclusive.
6. Migration never silently downgrades an unknown newer schema.
7. This store does not contain a customer order or credentials.

These rules inform the code and the tests before we write the first query.

## 19.3 Add the provider and choose the file location

The companion project `src/GnazzosWorld.Core/GnazzosWorld.Core.csproj` now contains:

```xml
<PackageReference Include="Microsoft.Data.Sqlite" Version="11.0.0" />
```

The version is pinned for the reader's reproducibility rather than silently choosing a future package. It is the Microsoft-supported low-level ADO.NET SQLite provider. Read the package's licensing and native-library dependencies when planning actual iOS/Android delivery.

The MAUI composition root registers a database pointing into the application's private app-data location:

```csharp
builder.Services.AddSingleton(_ => new LocalCatalogDatabase(
    Path.Combine(FileSystem.Current.AppDataDirectory,
                 "public-catalog-v2.sqlite3")));
```

This code is in `src/GnazzosWorld.App/MauiProgram.cs`. A single shared instance serializes its own operations, and the dependency-injection container disposes it with the application's lifetime. Do not build the path from customer-controlled text or use a temporary folder for durable user state. In the portable test suite, however, each test creates a separate temporary directory so that its database cannot affect another test.

The store's constructor accepts an absolute or relative path and normalizes it with `Path.GetFullPath`. It creates the parent directory on the first operation, not during DI registration. This separates constructing the application graph from opening a native file.

**Security boundary:** An app-data directory is not synonymous with encrypted storage. Device backups, rooted devices, debug builds and shared machines need separate handling. This exercise intentionally stores only nonsecret teaching data.

## 19.4 Open connections with an explicit lifetime

`LocalCatalogDatabase` uses an instance-owned `SemaphoreSlim`. Every operation waits for the gate, opens a fresh `SqliteConnection`, applies the schema on first use, executes its command, closes the connection and releases the gate in a `finally` block.

A trimmed excerpt shows the intended ownership:

```csharp
await gate.WaitAsync(ct);
try
{
    using var db = new SqliteConnection(builder.ToString());
    await db.OpenAsync(ct);
    if (!ready)
    {
        Migrate(db, ct);
        ready = true;
    }
    return await operation(db, ct);
}
finally
{
    gate.Release();
}
```

This is deliberately **an excerpt**: `builder`, `operation`, `ready`, and `gate` belong to the complete `InDatabaseAsync` method in the companion file. The real method creates the folder, checks disposal and constructs the connection string before opening.

### What is asynchronous—and what isn't?

The public API uses `Task` and accepts cancellation tokens, which lets callers await a database operation and cancel before acquiring the gate. There is a critical provider detail: SQLite itself does not offer the same asynchronous I/O model as remote database providers, and Microsoft.Data.Sqlite's ADO.NET async operations can execute synchronously. **An `Async` suffix alone does not guarantee the UI thread stays responsive during large or blocked disk operations.**

Our small sample controls concurrency and makes operations composable with async callers; it is **not** a measured proof of nonblocking native UI responsiveness. Larger production workloads need measured scheduling, connection strategy and native-device performance tests. Do not hide every SQLite call inside `Task.Run` without first defining cancellation, transaction ownership and lifetime correctly.

### Why not hold a transaction open during a network request?

A local transaction should protect a short, local state transition. A network call can take seconds, hang or return after the user changes screens. Holding a database transaction while waiting for HTTP increases contention and does not make the remote server atomic with the phone. In Chapter 20, a completed remote document will be validated first, then written locally within one short transaction.

## 19.5 Create and upgrade the schema atomically

SQLite exposes `PRAGMA user_version`, an application-owned integer stored in the database header. The sample recognizes schema versions **0, 1 and 2**:

- **0:** New file. Create the public-catalog and favorites tables.
- **1:** Preserve those tables and add the progress table.
- **2:** Current schema. No migration is necessary.
- **Greater than 2:** Refuse to open for modification rather than guessing how to downgrade.

Both upgrade steps run inside one SQLite transaction when the file begins at version 0. The complete `Migrate` implementation checks the current version before opening its upgrade transaction, performs controlled schema commands, checks cancellation, and commits once the desired schema is ready.

The important sequence is:

```text
Read user_version
  -> Reject unsupported future version
  -> Begin local transaction
  -> Create missing version-1 tables (if necessary)
  -> Create version-2 progress table (if necessary)
  -> Commit both schema and user_version
```

If an upgrade fails before commit, disposing the transaction rolls it back. On the next open, migration can retry against the still-committed schema. A migration must not update the version number *before* committing the corresponding schema.

### Real upgrade exercise

`LocalCatalogDatabaseTests.Migrates_an_existing_v1_database_without_deleting_favorites` creates an actual SQLite file using the original schema-1 statements, inserts a favorite, sets `user_version` to 1 and closes the connection. It then opens that file through the Chapter 19 store. The expected result is version 2, the original favorite still present, and a working progress table.

This tests a real file upgrade—not a mocked migration service. It also demonstrates why dropping and recreating the database would be a serious defect: it might produce the new tables but would discard legitimate saved state.

**Production extension:** An unrecoverable migration can require a controlled backup, an explicit repair path and a minimum supported version policy. This teaching implementation does not yet run `PRAGMA integrity_check`, manage a backup rotation or repair a damaged database. Do not silently delete corrupted or unsupported data to make the app launch.

## 19.6 Write parameterized queries, not SQL-shaped strings

User-controlled scope IDs and content IDs are passed as SQLite parameters. The favorite operation chooses between two *fixed SQL statements*; the user cannot supply a table name or extra SQL.

```csharp
using var cmd = Command(db,
    "SELECT item_id FROM favorites " +
    "WHERE scope=$scope ORDER BY item_id COLLATE BINARY;");
cmd.Parameters.AddWithValue("$scope", scope);
```

The complete source also parameterizes every item ID, revision, catalog payload and percentage value.

**Why is this important?** Constructing SQL with `"WHERE scope='" + scope + "'"` introduces quoting errors and SQL-injection risk. Parameterized values avoid treating input as SQL syntax. They do *not* substitute for domain validation: the store separately checks that identifiers are nonempty, bounded and contain no control characters.

The `scope` string is only a partition label for local exercise data. It is **not proof of authentication**. Later account-scoped storage must derive ownership from a trusted session and account lifecycle, not from any string a caller happens to supply.

## 19.7 Replace a public catalog without half an update

The Chapter 18 public API's contract is `CatalogDocument`. Before writing it, `ReplaceCatalogAsync` invokes `document.Validate()`, which checks document version, revision and catalog relationships. Only then does it serialize the complete document and enter the database transaction.

The statement uses SQLite's upsert syntax:

```sql
INSERT INTO public_catalog(singleton, revision, payload)
VALUES (1, $revision, $payload)
ON CONFLICT(singleton) DO UPDATE SET
    revision = excluded.revision,
    payload = excluded.payload;
```

Because there is only one row, the replacement can commit as a coherent unit. A consumer should not observe a new revision beside an old payload. If validation fails, the old row remains untouched. If the command fails, the transaction has not successfully committed the replacement.

Reading reverses the process: fetch the serialized document, deserialize using the same enum configuration, validate it again and return the document. This second validation is deliberate. A file can be modified outside the application, an old code version can write incompatible data, or corruption can occur. We should fail explicitly rather than converting malformed data into an apparently empty catalog.

### Worked failure scenario

1. Save `sample-1` as the accepted catalog revision.
2. Construct a second document with a creator ID that does not appear in its creators list.
3. Attempt replacement; the domain validator throws `InvalidDataException` before the transaction begins.
4. Read the stored document again. Its revision must still equal `sample-1`.
5. Save a valid `sample-2` document and verify it is now the stored revision.

The integration test named `Catalog_is_atomically_replaced_and_invalid_input_does_not_destroy_previous_snapshot` executes these steps. A future app must also decide whether `sample-2` is newer or fresher; the SQLite upsert alone cannot establish server authority.

## 19.8 Model favorites and progress as stable local state

Favorites are inserted with `INSERT OR IGNORE` and removed with a targeted `DELETE`. The composite key makes repeated "favorite" operations idempotent within one scope.

Progress is stored as an integer percentage. The application validates 0–100, and the SQL column independently enforces the same range:

```csharp
if (percent is < 0 or > 100)
    throw new ArgumentOutOfRangeException(nameof(percent));
```

The storage method uses an upsert keyed by `(scope, item_id)`. A missing progress row returns `null`, not zero. That distinction matters: "the reader has never started" is different from "the reader explicitly recorded zero percent."

**Tradeoff:** A percentage is a good small example but is not a complete reading-position model. EPUB positions, chapter IDs, narration timestamps and edition changes need richer identity and mapping rules. A book revision may invalidate a numeric offset. Chapters 20–21 will separate stored local progress from server reconciliation.

### Lab: prove local isolation

1. Open a temporary file store.
2. Mark `book-kai-01` as favorite under `guest-a`.
3. Mark another ID favorite under `guest-b`.
4. Save 25% progress for `book-kai-01` under `guest-a`.
5. Verify that `guest-b` does not see `guest-a`'s favorite or progress.
6. Remove the first favorite and verify that the progress row remains.

**Expected:** Favorites and progress are independent tables whose keys include the same local scope. This does not demonstrate authorized multiuser accounts or cross-device sync.

## 19.9 Plan recovery instead of pretending every write succeeds

Persistence failures matter because the application may still be running and showing unsaved edits. The portable tests deliberately inject failures at meaningful boundaries.

| Scenario | Expected behavior | Evidence |
|---|---|---|
| Invalid catalog document | Reject replacement; preserve prior revision | Real SQLite file test |
| Invalid progress percent | Reject before SQL; preserve existing value | Portable integration test |
| Canceled operation | Honor cancellation before acquiring the gate | Canceled-token test |
| SQLite constraint or trigger failure | Return an error; do not overwrite prior row | Real database trigger test |
| Version-1 database | Upgrade to version 2 without removing favorites | Real upgrade test |
| Future schema version 99 | Refuse unsupported downgrade | Real-file version test |
| Process restarts after a successful write | Data remains in the file | Close/reopen test |

A database write may fail because the filesystem is full, storage permissions changed, the process terminated, or another actor holds a lock. The test uses a database trigger to make a write fail predictably while retaining the old value. That test proves the failure path at the database boundary; it does not recreate every physical disk failure.

A resilient UI must report that its newest operation was not saved. It should not update a "saved" indicator before the commit succeeds. This follows the same principle as Chapter 13's favorite store and Chapter 16's uncertain submission state.

### Corruption and backup policy

Do not use the catch-all strategy "delete the database and start over." Public catalog metadata is potentially recoverable from the API, but local favorites and progress may be irreplaceable. Preserve the failed file for diagnosis under a privacy-appropriate retention policy, consider backups before destructive migrations, and provide a user-visible recovery choice. SQLite integrity checks and backup APIs require separate operational design and tests.

On mobile, platform backup defaults also matter. A backing file can be restored onto a newer application version, or onto a device without the original secrets. Schema migration, account ownership, encryption keys and backup configuration must be evaluated together before public release.

## 19.10 Run the complete source and tests

Open the companion repository at the Chapter 19 source revision and inspect:

- `src/GnazzosWorld.Core/Storage/LocalCatalogDatabase.cs`: complete implementation, connection and transaction ownership.
- `src/GnazzosWorld.Core/GnazzosWorld.Core.csproj`: pinned SQLite package reference.
- `src/GnazzosWorld.App/MauiProgram.cs`: MAUI dependency injection and app-data file path.
- `tests/GnazzosWorld.Core.Tests/LocalCatalogDatabaseTests.cs`: disposable real-file integration tests.

From the companion repository root in PowerShell:

```powershell
dotnet --version
dotnet restore tests/GnazzosWorld.Core.Tests/GnazzosWorld.Core.Tests.csproj
dotnet build tests/GnazzosWorld.Core.Tests/GnazzosWorld.Core.Tests.csproj -c Release --no-restore
dotnet run --project tests/GnazzosWorld.Core.Tests/GnazzosWorld.Core.Tests.csproj -c Release --no-build
```

For the app's separate Android compilation, use the matching SDK, JDK and Android workload described in Chapter 3:

```powershell
dotnet build src/GnazzosWorld.App/GnazzosWorld.App.csproj -f net11.0-android -c Debug
```

**What a successful portable run establishes:** The compiled code exercises actual SQLite files and the listed migration, snapshot, progress and favorite behaviors on the CI operating system. The suite does not verify Android/iOS native SQLite loading, UI responsiveness, encryption, cloud backup configuration, an actual disk-full condition, or application restart UX on a phone. The Android build verifies compilation and packaging dependencies, not device execution.

**Verification record:** Inspect the newest CI runs for the Chapter 19 commit rather than relying on the historical Chapter 18 count of 245 portable tests. If the workflow has not yet finished, mark the new checks *pending*, not passed.

### Troubleshooting

| Symptom | Likely cause or boundary | Diagnostic action |
|---|---|---|
| Restore cannot find Microsoft.Data.Sqlite | Wrong feed, SDK or connectivity | Confirm package version 11.0.0 and inspect restore error |
| "No such table: reading_progress" | Migration not reached or version/data mismatch | Inspect `PRAGMA user_version` and transaction path |
| "Unsupported future database schema" | File created by a newer application | Preserve the file; do not downgrade destructively |
| A favorite appears under another local scope | Incorrect query key or caller scope | Inspect `(scope, item_id)` parameters and add an isolation test |
| Reading progress does not survive restart | Wrong path, ephemeral directory or failed write | Confirm app-data path, commit and reopen test |
| UI freezes on a large import | Provider I/O may be synchronous despite async methods | Measure actual device behavior and keep work bounded |
| Old catalog disappears after invalid fetch | Replacement happened before complete validation | Validate first, transact the complete snapshot, preserve prior revision |
| App loads but storage is unavailable | File permission, native provider, disk or migration error | Report specific failure; do not silently reset personal state |

## 19.11 What remains before this is a production data layer

A short, testable implementation is valuable, but a production architecture needs decisions this exercise intentionally postpones.

**Native performance:** The current store serializes through one instance and opens a connection per operation. This makes ownership easy to teach but does not measure contention, startup cost, large catalog ingestion or UI responsiveness. Profile those on the target devices.

**Cross-process coordination:** The gate serializes a single `LocalCatalogDatabase` instance, not every process or instance that may open the file. SQLite's locking and busy handling remain relevant if external writers exist.

**Sensitive data:** The file is not an encrypted vault. The Chapter 15 JSON draft remains separate, and real customer stories need deliberate encryption, retention, ownership and deletion policies before any migration.

**Atomicity across systems:** A local SQLite commit and a remote API acceptance are two distinct transactions. Chapter 20 will use persisted pending operations for offline work; it must not represent a local receipt as server-confirmed acceptance.

**Migration discipline:** Each new schema version should carry forward all earlier supported versions, test both new installs and upgrade paths, and retain a recovery strategy. A version number alone does not make destructive changes safe.

**Backup and maintenance:** Add integrity checks, explicit recovery, file growth management, and an app-update test matrix. The sample intentionally does not claim device backup or restore verification.

## Chapter Summary

Local persistence is a contract about survival, ownership and change—not merely a call to write a file. This chapter selects SQLite for a versioned public catalog, local favorites and reading progress while retaining Preferences and an explicit JSON draft for their existing purposes. `LocalCatalogDatabase` validates complete catalog documents before atomic replacement, binds user values as SQL parameters and upgrades schema versions inside a transaction. Its real-file tests exercise persistence across reopen, upgrade from version 1, local scope separation, rejected writes, cancellation and refusal to downgrade an unknown future schema. The design remains intentionally small: local scope names are not identities, SQLite async APIs do not guarantee nonblocking device I/O, and no secret or live customer order belongs in this example. Chapter 20 builds on these guarantees to design offline freshness and a restart-safe work queue.

## Exercises and Review Questions

1. **Guided, with a worked check:** Add a new field `last_opened_utc` for reading progress in a hypothetical version 3 migration. Predict the result of opening an existing version-1 file and a version-2 file. **Worked check:** Both must reach version 3 without losing existing favorites or progress; the upgrade must assign a safe default or permit NULL for older rows, run transactionally, and reject a future unsupported schema rather than trying to downgrade.
2. **Failure exercise:** Temporarily remove validation before catalog replacement. Write a test proving why a malformed creator relationship must not replace the known-good document. Restore the original implementation and require the regression test to pass.
3. **Concurrency exercise:** Create two independent `LocalCatalogDatabase` instances pointing to the same temporary file and deliberately overlap writes. Explain what the per-instance semaphore does *not* protect and how SQLite locking and retry policy would need evaluation.
4. **Architecture extension:** Design a secure request-draft migration from the Chapter 15 envelope. Include explicit version recognition, backup, account ownership, encryption-key lifecycle, rollback and the user's unsaved edits. Do not implement or claim live personal-data transfer.
5. **Offline bridge:** Sketch how Chapter 20 should store the time and revision of the last successful API response. Explain why a successful SQLite save by itself cannot tell a user whether catalog metadata is fresh.

**Review questions:** Why is an absent progress row different from 0%? How does a catalog revision differ from SQLite's `user_version`? Why does a passing temporary-file test not prove encrypted storage? What can happen if the process is killed after a server accepts an order but before the phone saves its receipt?

## References

- Microsoft.Data.Sqlite 11.0.0 NuGet package and dependency information: https://www.nuget.org/packages/Microsoft.Data.Sqlite/11.0.0
- Microsoft Learn, Microsoft.Data.Sqlite overview: https://learn.microsoft.com/en-us/dotnet/standard/data/sqlite/
- Microsoft Learn, transactions and async limitations: https://learn.microsoft.com/en-us/dotnet/standard/data/sqlite/async
- SQLite, application file format and `user_version`: https://www.sqlite.org/pragma.html#pragma_user_version
- SQLite, transactions: https://www.sqlite.org/lang_transaction.html
- Microsoft Learn, .NET MAUI file-system helpers: https://learn.microsoft.com/en-us/dotnet/maui/platform-integration/storage/file-system-helpers
- Microsoft Learn, .NET MAUI SecureStorage: https://learn.microsoft.com/en-us/dotnet/maui/platform-integration/storage/secure-storage

## Editorial index terms

SQLite; Microsoft.Data.Sqlite; schema migration; PRAGMA user_version; atomic transaction; parameterized SQL; catalog snapshot; serialization; catalog revision; favorites; local scope; reading progress; optimistic freshness; cancellation; write failure; rollback; app-data directory; secure storage; account ownership; corrupt database; backup; asynchronous database API; offline persistence; DI; MAUI.
