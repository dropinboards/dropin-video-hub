import os,json,datetime,urllib.parse,urllib.request,pathlib
ROOT=pathlib.Path(__file__).parent
KEY=os.environ.get('YOUTUBE_API_KEY','')
if not KEY: raise SystemExit('Missing YOUTUBE_API_KEY GitHub Actions secret')
QUERIES=[('snow','backcountry','snowboard freeride backcountry pro'),('snow','street','snowboard street full part'),('snow','park','snowboarding pro park rail edit'),('snow','film','snowboard full film'),('snow','competition','snowboarding slopestyle big air finals'),('snow','powder','snowboarding deep powder pro'),('skate','street','skateboarding pro street video part'),('skate','technical','skateboarding technical ledge pro part'),('skate','transition','skateboarding vert bowl transition pro'),('skate','film','skateboarding full length film'),('skate','competition','skateboarding street finals pro'),('skate','crew','skateboarding independent crew raw edit')]
items={}
after=(datetime.datetime.now(datetime.timezone.utc)-datetime.timedelta(days=45)).isoformat().replace('+00:00','Z')
for sport,style,q in QUERIES:
 params=urllib.parse.urlencode({'part':'snippet','type':'video','order':'date','maxResults':25,'publishedAfter':after,'q':q,'key':KEY})
 try:
  with urllib.request.urlopen('https://www.googleapis.com/youtube/v3/search?'+params,timeout=25) as r: data=json.load(r)
 except Exception as e:
  print('Search failed:',q,e);continue
 for v in data.get('items',[]):
  vid=v.get('id',{}).get('videoId');s=v.get('snippet',{})
  if not vid:continue
  title=s.get('title','');low=title.lower()
  if any(x in low for x in ['beginner','first time','how to start','tutorial for beginners','kids lesson','learn to']):continue
  if vid not in items:items[vid]={'id':vid,'title':title,'channel':s.get('channelTitle',''),'published':s.get('publishedAt',''),'thumbnail':s.get('thumbnails',{}).get('high',s.get('thumbnails',{}).get('medium',{})).get('url',''),'sport':sport,'styles':[style],'url':'https://www.youtube.com/watch?v='+vid}
  elif style not in items[vid]['styles']:items[vid]['styles'].append(style)
old=ROOT/'feed.json'
if not items:raise SystemExit('No videos returned; keeping previous feed')
output={'updatedAt':datetime.datetime.now(datetime.timezone.utc).isoformat(),'videos':sorted(items.values(),key=lambda x:x['published'],reverse=True)}
old.write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Saved',len(items),'videos')
