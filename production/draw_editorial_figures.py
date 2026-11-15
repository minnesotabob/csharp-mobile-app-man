"""Authored technical figures. Reproduce with Python + Pillow; no runtime screenshots."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'assets/figures';OUT.mkdir(parents=True,exist_ok=True)
FONT='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
BOLD='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
W,H=1800,1200
class Figure:
 def __init__(self,title,subtitle):
  self.im=Image.new('RGB',(W,H),'white');self.d=ImageDraw.Draw(self.im)
  self.text(80,52,title,58,True);self.text(80,143,subtitle,36)
  self.d.line((80,210,1720,210),fill='#444444',width=3)
 def text(self,x,y,s,size=42,bold=False,center=False):
  f=ImageFont.truetype(BOLD if bold else FONT,size)
  while not center and self.d.textlength(s,font=f)>W-x-70:
   size-=1;f=ImageFont.truetype(BOLD if bold else FONT,size)
  self.d.text((x,y),s,font=f,fill='#181818',anchor='mt' if center else 'lt',spacing=12)
 def box(self,x,y,w,h,title,lines=(),dashed=False):
  self.d.rounded_rectangle((x,y,x+w,y+h),radius=14,fill='#f2f2f2',outline='#333333',width=4)
  title_size=44
  while self.d.textlength(title,font=ImageFont.truetype(BOLD,title_size))>w-36:title_size-=1
  self.text(x+w/2,y+23,title,title_size,True,True)
  rendered=[]
  for line in lines:
   size=40
   if self.d.textlength(line,font=ImageFont.truetype(FONT,size))>w-40:size=36
   words=line.split(); row=''
   for word in words:
    candidate=(row+' '+word).strip()
    if row and self.d.textlength(candidate,font=ImageFont.truetype(FONT,size))>w-40:
     rendered.append((row,size));row=word
    else:row=candidate
   rendered.append((row,size))
  assert 84+len(rendered)*44<=h+12,(title,rendered,h)
  for i,(line,size) in enumerate(rendered):self.text(x+w/2,y+84+i*44,line,size,center=True)
 def arrow(self,points,label=None,lx=None,ly=None):
  self.d.line(points,fill='#333333',width=5,joint='curve')
  x,y=points[-1];a,b=points[-2];ang=math.atan2(y-b,x-a)
  self.d.polygon([(x,y),(x-23*math.cos(ang-.5),y-23*math.sin(ang-.5)),(x-23*math.cos(ang+.5),y-23*math.sin(ang+.5))],fill='#333333')
  if label:self.text(lx,ly,label,35)
 def note(self,s):self.text(80,1125,s,34)
 def save(self,name):self.im.convert('L').save(OUT/(name+'.png'),optimize=True,dpi=(300,300))

f=Figure('1.1  Follow the first search','Part I implementation: screen input and portable rules have different owners.')
f.box(90,280,680,190,'MAUI page',('Text input and search event',))
f.box(1030,280,680,190,'Portable search',('CatalogSearch.Find',))
f.box(1030,735,680,190,'Catalog fixture',('Stable IDs and public metadata',))
f.box(90,735,680,190,'Visible results',('Page assigns the returned list',))
f.arrow([(770,375),(1030,375)],'query',830,310)
f.arrow([(1370,735),(1370,470)],'records',1410,575)
f.arrow([(1030,435),(900,435),(900,830),(770,830)],'result list',830,910)
f.note('A passing search test proves the rule; a device check proves the visible handoff.');f.save('fig-01-first-search')

f=Figure('7.1  State and platform actions','Part II architecture: binding is a two-way relationship, not a data source.')
f.box(90,280,650,205,'Catalog view',('XAML bindings and commands',))
f.box(1010,280,700,205,'View model',('Query, selection and result state',))
f.box(90,750,650,205,'Portable catalog',('Records and search rules',))
f.box(1010,750,700,205,'Navigation adapter',('ICatalogNavigation to Shell',))
f.arrow([(740,345),(1010,345)],'input / commands',755,270)
f.arrow([(1010,445),(740,445)],'notifications',770,500)
f.arrow([(1120,485),(1120,625),(415,625),(415,750)],'search',560,655)
f.arrow([(1410,485),(1410,750)],'open item by ID',1440,600)
f.note('Portable tests cover state and guards. Native focus, layout and navigation need device evidence.');f.save('fig-07-mvvm')

f=Figure('17.1  A response must cross every gate','Chapter 17 contract: the first failed gate stops publication of new catalog data.')
ys=[270,450,630,810]
for y,t,sub in zip(ys,['HTTP response','Bounded body','Valid catalog','Return accepted list'],['Expected status and JSON media type','Read within byte and time limits','Parse, validate metadata and IDs','Caller decides whether it still owns the result']):
 f.box(100,y,1040,145,t,(sub,))
 if y<810:f.arrow([(620,y+145),(620,y+180)])
f.box(1280,455,420,280,'Failure',('Classify the cause','Dispose response','Caller keeps prior data'))
f.arrow([(1140,342),(1220,342),(1220,550),(1280,550)])
f.arrow([(1140,522),(1280,522)])
f.arrow([(1140,702),(1220,702),(1220,650),(1280,650)])
f.note('The networking lab uses a fixture handler. It does not establish a live phone-to-API path.');f.save('fig-17-http-gates')

f=Figure('20.1  Local reading and durable refresh','One worker commits the snapshot and matching acknowledgment together.')
f.box(80,270,740,200,'ReadLocalAsync',('Read saved snapshot, or bundled data',))
f.box(980,270,740,200,'RunPendingAsync',('Read ticket and perform bounded GET',))
f.box(80,770,740,200,'Local result',('Origin, retrieval time and stale flag',))
f.box(980,770,740,200,'SQLite transaction',('Save snapshot and retrieval time','Delete only the matching ticket'))
f.arrow([(450,470),(450,770)],'no network required',95,585)
f.arrow([(1350,470),(1350,770)],'success',1400,580)
f.arrow([(980,900),(820,900)],'next local read',825,975)
f.arrow([(980,360),(890,360),(890,680),(450,680)],'failure: retain intent',950,550)
f.note('Persist intent before fetching. Native browser wiring and OS scheduling remain pending.');f.save('fig-20-offline')

f=Figure('I.1  From development to public release','Planned roadmap: a store distributes a client package; the API is deployed separately.')
f.box(80,270,730,200,'Development and local API',('Fixtures, tests and temporary hosting','Chapters 3-5 and 17-21'))
f.box(990,270,730,200,'Staging and test device',('Trusted endpoints and real journeys','Chapters 35-37'))
f.box(990,740,730,200,'Signed client and stores',('Android / iOS build and test tracks','Chapters 38-39'))
f.box(80,740,730,200,'Production operations',('API, monitoring and maintenance','Chapters 35 and 40'))
f.arrow([(810,370),(990,370)])
f.arrow([(1355,470),(1355,740)])
f.arrow([(990,840),(810,840)],'release gates',790,990)
f.note('Deployment, store submission and production activation are later work, not claims of this draft.');f.save('fig-intro-release')

f=Figure('18.1  Preview the protected-data boundary','Planned for Part V: an anonymous visitor can continue browsing public catalog data.')
f.box(80,270,730,200,'Native public client',('No embedded private client secret','Browser-based sign-in'))
f.box(990,270,730,200,'Identity provider',('Authenticates the customer','MFA and recovery policies'))
f.box(80,760,730,230,'Protected API',('Validate access token and policy','Check resource ownership'))
f.box(990,760,730,230,'Customer data',('Access through the authorized API','No direct mobile database access'))
f.arrow([(810,330),(990,330)],'sign-in',820,265)
f.arrow([(990,435),(810,435)],'token via client library',795,485)
f.arrow([(445,470),(445,760)],'bearer access token',95,595)
f.arrow([(810,875),(990,875)],'authorized query',800,1010)
f.note('Chapter 18 has public endpoints only. Protected customer data arrives in Part V.');f.save('fig-18-security-preview')

f=Figure('Part I recap  |  Choose the evidence','Question to remember: which boundary did this check actually exercise?')
items=[('Portable rule','Search and validation','Expected IDs, values and rejected inputs'),('Integration boundary','Actual adapter or service','Serialization, database and pipeline behavior'),('Native experience','Emulator or physical device','Keyboard, lifecycle, focus and permissions')]
for y,(a,b,c) in zip([280,535,790],items):
 f.box(90,y,620,190,a,(b,));f.box(910,y,800,190,'Evidence to record',(c,));f.arrow([(710,y+95),(910,y+95)])
f.note('A green check in one row does not fill another row. Keep unobserved claims pending.');f.save('recap-05-evidence')

f=Figure('Part II recap  |  Keep ownership visible','One selected item can have a stable identity across several layouts.')
items=[('View','Render and accept input','Width, focus and text size'),('View model','Own current presentation state','Query, selection and command guards'),('Platform adapter','Perform native actions','Navigation and external launches')]
for y,(a,b,c) in zip([280,535,790],items):
 f.box(90,y,600,190,a,(b,));f.box(910,y,800,190,'What to inspect',(c,));f.arrow([(690,y+95),(910,y+95)])
f.note('Phone navigation and tablet inline detail present the same selected ID; they need separate UI checks.');f.save('recap-11-ownership')

f=Figure('Part III recap  |  A request is not payment','Chapter 15-16 teaching workflow: draft editing and simulated acceptance are distinct.')
f.box(80,270,730,200,'Editable draft',('Customer story and musical choices','Explicit local Save draft'))
f.box(990,270,730,200,'Reviewed snapshot',('All required fields validated','Any edit invalidates review'))
f.box(990,760,730,230,'Quote and submission',('Versioned terms and operation ID','Uncertain response: reconcile same ID'))
f.box(80,760,730,230,'Simulated receipt',('Demonstration acceptance only','No live order or payment proof'))
f.arrow([(810,370),(990,370)],'review',820,295)
f.arrow([(1355,470),(1355,760)],'request terms',1395,590)
f.arrow([(990,875),(810,875)],'accept',820,1010)
f.note('Later authenticated service and verified payment events establish real order and payment state.');f.save('recap-16-request')
f=Figure('19.1  Upgrade without losing a favorite','Chapter 19 checkpoint: schema 2 is current; Chapter 20 adds schema 3.')
f.box(80,270,640,200,'Read schema version',('0 or 1: prepare upgrade','2: use current schema'))
f.box(1010,270,710,200,'Future version: refuse',('Do not downgrade or delete','Preserve file for diagnosis'))
f.box(80,740,640,230,'Upgrade transaction',('Create only missing tables','Update user_version in transaction'))
f.box(1010,650,710,180,'Commit succeeds',('Publish schema and version together',))
f.box(1010,900,710,180,'Failure before commit',('Roll back; preserve committed state',))
f.arrow([(720,365),(1010,365)],'> 2',810,290)
f.arrow([(400,470),(400,740)],'0 or 1',440,580)
f.arrow([(720,800),(870,800),(870,740),(1010,740)])
f.arrow([(720,920),(870,920),(870,990),(1010,990)])
f.note('Existing schema-1 favorites survive the upgrade. Version 2 needs no upgrade transaction.');f.save('fig-19-migration')

f=Figure('Part IV progress  |  Name the boundary','Chapters 17-20: four decisions require different evidence.')
items=[('17  Accept a response','Status, body bounds and payload validation'),('18  Define the public API','Contract, validation and controlled errors'),('19  Commit local state','Real-file migrations and rollback checks'),('20  Recover refresh intent','Freshness, tickets and matching acknowledgment')]
for y,(a,b) in zip([250,460,670,880],items):
 f.box(80,y,690,180,a)
 f.box(960,y,760,180,'Evidence',(b,))
 f.arrow([(770,y+90),(960,y+90)])
f.note('Chapter 21 adds user synchronization. Native integration and device checks remain separate.');f.save('recap-20-data-boundaries')
print('Created',len(list(OUT.glob('*.png'))),'authored figures')
