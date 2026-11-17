# Appendix C
# API, Data, and Configuration Reference

This is a navigation map to the actual companion contracts. The complete source and corresponding lab remain authoritative for a selected checkpoint. The application evolves across chapters; do not combine an early JSON example with a later client and assume the two describe the same milestone.

## C.1 Find the boundary by project

| Project or directory | Responsibility | Starting point |
| --- | --- | --- |
| GnazzosWorld.Core/Catalog | Stable public identities and validation | CatalogItem.cs; CatalogSnapshot.cs |
| Core/Contracts | Versioned public catalog document | CatalogDocument.cs |
| Core/Presentation | Portable interaction ownership | DebouncedQuery.cs; request/view models |
| Core/Identity | Sessions, leases and account workspace | ApiSession.cs; AccountWorkspace.cs |
| Core/Media | Playback state and progress | PlaybackSession.cs; BackgroundPlaybackOwner.cs |
| Core/Commerce | Quotes, operations and durable customer workflow | Order contract/store/client types |
| GnazzosWorld.Api | HTTP mapping, validation and authorization | Program.cs and named endpoint files |
| GnazzosWorld.App | MAUI views and native adapters | MauiProgram.cs; Platforms directory |
| tests | Executable rules and boundary regressions | Core.Tests; Api.Tests |
| tools and samples | Named executable teaching exercises | Corresponding docs lab |

These are source locations, not independent deployable services. A portable model or client interface is not automatically an HTTP contract. Read the endpoint's request/response type and validation rules before implementing another client.

## C.2 Public catalog routes

| Operation | Shape or purpose | Important limit |
| --- | --- | --- |
| GET /health | Minimal status | Not proof of database/provider readiness |
| GET /api/v1/catalog | Versioned document with items/creators | Validated bounded snapshot |
| GET /api/v1/catalog/items | Earlier items-array contract | Different shape from full document |
| GET /api/v1/catalog/pages | Offset/limit/revision page | Continue with first page's revision |
| GET or HEAD /api/v1/media/timing | Original public WAV fixture | Bounded HTTP range semantics |

The complete public document is limited to 1,000 items and creators by its validator. The HTTP client separately limits response bytes to 1 MiB. The bundled catalog contains five teaching records; Chapter 37's larger stress fixture is a separate performance input, not a silent expansion of this API contract.

Paging defaults to offset 0 and limit 20, with limit 1 through 100. A continuation needs the first page's revision. A changed revision produces a conflict rather than silently mixing two snapshots. An empty terminal page differs from an invalid offset beyond the end. See docs/local-api.md and the Chapter 18 lab for exact cases.

Public catalog metadata does not imply ownership of playable bytes. A streaming-service web link is an external destination, not an audio resource for the app player. The demonstration episode has no included audio. The original reading sample in the catalog is a teaching fixture, not an excerpt from the published book.

## C.3 Protected and synthetic routes

The protected request-preview route is GET /api/v1/requests/{id}. The API validates access independently of the native client. A visible client-side filter is not authorization. The preview is not the later commerce order or private-delivery contract.

| Feature | Selected operations | Complete reference |
| --- | --- | --- |
| Push registration | PUT/DELETE notification-installations/{id} beneath /api/v1 | notification-link-lab.md |
| Quotes | POST /api/v1/commerce/quotes | commerce-lab.md |
| Order acceptance | POST /api/v1/commerce/orders | commerce-lab.md |
| Owned order | GET /api/v1/commerce/orders/{id} | commerce-lab.md |
| Order collection/tracking | GET commerce orders and orders/{id}/tracking | fulfillment-lab.md |
| Revision request | POST orders/{id}/revisions beneath commerce | fulfillment-lab.md |
| Delivery grant/content | Owned order delivery subroutes | fulfillment-lab.md |
| TEST payment | Separately enabled test checkout/events | payment-lab.md |
| Operations readiness | /health/live and /health/ready when enabled | operations-lab.md |

The abbreviated fulfillment paths in the table continue under /api/v1/commerce. Use FulfillmentEndpoints.cs for exact route templates, methods and DTOs. Do not reconstruct a private URL from a table entry or treat a delivery descriptor as permission to read its bytes.

Commerce owner identity comes from validated claims, not a customer-supplied owner field. The server calculates the quote. Its acceptance protocol associates the original operation key, quote and canonical request with a durable outcome. An accepted order is not proof of payment, production or delivery.

Fulfillment's console fixture can manufacture invented TEST-paid state to exercise a review/delivery journey. That local fixture authority is not a customer HTTP privilege or production administration. Push registration similarly records a binding; it does not prove that a provider delivered a notification.

## C.4 Configuration map

| Setting | Meaning | Where to inspect |
| --- | --- | --- |
| Catalog:Revision | Bounded public snapshot identity | appsettings.json; PublicCatalog.cs |
| AllowedHosts | Accepted request hostnames | API configuration and hosting setup |
| Commerce:Enabled | Opt-in synthetic commerce routes | CommerceEndpoints.cs; commerce lab |
| Commerce:Database | Selected teaching database path | CommerceEndpoints.cs; operations lab |
| Payments:Enabled | Separate test-payment opt-in | TestPaymentEndpoints.cs; payment lab |
| Payments:TestSecretKey | Controlled test-provider credential | Private local configuration only |
| Payments:WebhookSecret | Controlled test-event verification secret | Private local configuration only |
| Payments:AccountId | Expected provider account scope | payment-lab.md |
| Payments:ReturnOrigin | Validated browser-return origin | payment-lab.md |
| Fulfillment:Enabled | Separate synthetic fulfillment opt-in | FulfillmentEndpoints.cs |
| Operations:Enabled | Isolated operations profile | OperationsSettings.cs |
| Operations:ArtifactsRoot | Controlled artifact root | operations-lab.md |
| Operations:TracePercent | Bounded diagnostic sampling setting | OperationsSettings.cs |
| Operations:FailureProbe | Isolated controlled-failure exercise | OperationsEndpoints.cs |

Environment variables use the ASP.NET Core double-underscore mapping, for example Commerce__Enabled. That spelling is a configuration mechanism, not permission to enable every lab together. Respect each feature's environment and identity prerequisites. Production rejection and Staging restrictions are deliberate boundaries of these teaching implementations.

Do not copy example paths, credentials or business settings into a live system. A database path must have suitable ownership and access; a provider secret must remain outside tracked source and public logs. Use the complete lab for required settings, defaults and failure behavior.

## C.5 Native identity configuration

NativeIdentitySettings accepts the selected public tenant hostname and native client ID. Its fixed teaching callback is com.johngnazzo.gnazzosworld://callback/. The identity SDK still owns protocol validation. A reader changing application identity must reconcile source, platform declarations and provider registration.

ApiSessionSettings adds a selected HTTPS audience and API origin. An audience identifies the intended resource; an origin identifies where the client sends requests. Matching one does not make the other correct. The native app does not contain a confidential-client secret, and requesting scopes does not grant those scopes.

AccessLease associates a token with the current session generation. OwnedAccessLease also retains issuer/subject identity. These are process/application ownership tools; the API must independently validate the credential and resource authorization. Their redacted ToString implementations do not make arbitrary token logging safe elsewhere.

## C.6 Persistent data is not one interchangeable store

Public snapshots, favorites, request drafts, account workspaces, listening progress and pending order journals have different value and privacy boundaries. Anonymous local partitions are not authenticated accounts. A plaintext teaching SQLite database does not become encrypted because its filename contains a user scope.

Follow the relevant chapter before deleting or migrating a store. Order reconciliation must preserve original keys after an uncertain response. Playback checkpoints must match item and content revision. An export/deletion fixture does not erase a real provider account or every private cache. A full privacy lifecycle needs composition and actual acceptance evidence across those boundaries.

For a useful exercise, choose a saved anniversary draft, a playback checkpoint and a pending order. For each, identify its owner, persistence mechanism, confirmation point, restart behavior and deletion policy. If the answer is only in memory, it cannot establish recovery in a new process.

## C.7 Read a fixture safely

Start with the generator or credited source. Check the intended chapter, content revision, dimensions/duration where relevant, byte limits and declared license/provenance. Use invented contact/story details. The source deliberately labels demonstration content and synthetic customer operations.

A fixture can make a difficult failure reproducible without claiming a live integration. The useful question is which boundary the fixture controls. A player double controls observations; it does not measure native focus. A synthetic payment event controls replay cases; it does not settle production settlement. Chapter 36 explains how to combine evidence without erasing those limits.
