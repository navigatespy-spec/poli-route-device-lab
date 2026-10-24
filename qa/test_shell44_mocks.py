"""shell44 simulated-storage regression only; NOT browser-origin persistence or iPhone PWA."""
import json,re
from pathlib import Path
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1]
checks=[];errors=[]
def check(title,passed):
 checks.append({'name':title,'passed':bool(passed)})
 print(('PASS ' if passed else 'FAIL ')+title,flush=True)
def snapshot(page):
 return page.evaluate('''() => Object.fromEntries(Array.from({length:localStorage.length},(_,i)=>{const k=localStorage.key(i);return [k,localStorage.getItem(k)]}))''')
def load(page,filename,store=None):
 page.goto('about:blank')
 page.evaluate('''seed => { const records=Object.assign({},seed||{}); Object.defineProperty(window,'localStorage',{configurable:true,value:{getItem:k=>Object.prototype.hasOwnProperty.call(records,k)?records[k]:null,setItem:(k,v)=>{records[k]=String(v)},removeItem:k=>delete records[k],key:i=>Object.keys(records)[i],get length(){return Object.keys(records).length}}}); }''',store or {})
 page.set_content((ROOT/filename).read_text(),wait_until='domcontentloaded')
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-dev-shm-usage'])
 ctx=browser.new_context(viewport={'width':390,'height':844},is_mobile=True,has_touch=True)
 page=ctx.new_page();page.on('pageerror',lambda e:errors.append(str(e)));page.on('dialog',lambda d:d.accept())
 load(page,'index.html')
 check('shell-44 表示','shell-44' in page.locator('body').inner_text())
 check('旧データと隔離された新保存キー',page.evaluate("STORAGE_KEY==='poli-route-shell44-device-lab-v1'"))
 check('iPhone検証ページへのリンク',page.locator('a[href="device-check.html"]').count()==1)
 check('アプリ起動完了',page.locator('#state').get_attribute('data-booted')=='1')
 check('空データでロックなし',page.evaluate('!storageLocked'))
 page.evaluate('''() => {db={places:[{id:'lab-p1',name:'架空検証施設',address:'架空市1丁目',ward:'架空区'}],routes:[],rules:[],parking:[],origin:'架空出発地',drives:[]};return persist()}''')
 check('模擬localStorageへの保存',page.evaluate('JSON.parse(localStorage.getItem(STORAGE_KEY)).places.length===1'))
 s=snapshot(page);load(page,'index.html',s)
 check('模擬リロード後に架空施設を復元',page.evaluate("db.places.length===1 && db.places[0].name==='架空検証施設'"))
 check('模擬リロード後も保存ロックなし',page.evaluate('!storageLocked'))
 old=page.evaluate('localStorage.getItem(STORAGE_KEY)')
 # invalid backup is rejected without mutating storage
 result=page.evaluate('''() => {try{restoreFullBackup({places:[],routes:[],rules:[],parking:[],drives:[{id:'bad',minutes:-5}],origin:''});return 'accepted'}catch(e){return 'rejected'}}''')
 check('不正な復元データの拒否',result=='rejected')
 check('不正復元後に以前の保存値を保持',page.evaluate('localStorage.getItem(STORAGE_KEY)')==old)
 saved=snapshot(page)
 load(page,'device-check.html',saved)
 check('検証ページに12項目のチェック欄',page.locator('#checks input[type="checkbox"]').count()==12)
 check('診断画面の書込み・読返し', '書込み・読返し：成功' in page.locator('#trace').inner_text())
 page.locator('#checks input').first.check()
 check('チェック操作で1/12を表示','1 / 12' in page.locator('#progress').inner_text())
 s=snapshot(page);load(page,'device-check.html',s)
 check('模擬リロードでチェック状態を維持',page.locator('#checks input').first.is_checked())
 check('模擬リロードで前回の保存印を確認','前回値を読取成功' in page.locator('#trace').inner_text())
 check('共有する判定票に施設名を含まない',page.evaluate("() => !makeReport().includes('架空検証施設') && makeReport().includes('実用化ゲート未通過')"))
 check('検証ページからアプリへ戻れる',page.locator('a[href="./index.html"]').count()==1)
 check('Service Workerがオフライン検証ページをキャッシュ対象に含める',"./device-check.html" in (ROOT/'sw.js').read_text() and 'device-check' in (ROOT/'sw.js').read_text())
 check('manifest は検証版名と専用id',json.loads((ROOT/'manifest.webmanifest').read_text())['id']=='./index.html?edition=shell44-lab')
 check('JavaScriptの未処理例外なし',not errors)
 ctx.close();browser.close()
result={'method':'Chromium set_content / in-memory simulated localStorage / no HTTP, no PWA or iPhone testing','passed':sum(x['passed'] for x in checks),'total':len(checks),'checks':checks,'jsErrors':errors}
(ROOT/'qa'/'shell44_mock_test_results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
print('TOTAL',result['passed'],'/',result['total'],'errors',errors,flush=True)
if result['passed']!=result['total']:raise SystemExit(1)
