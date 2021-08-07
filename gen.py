import requests
import string
import random

def getRandomString(length): #Letters and numbers
	pool=string.ascii_lowercase+string.digits
	return "".join(random.choice(pool) for i in range(length))

def getRandomText(length): #Chars only
	return "".join(random.choice(string.ascii_lowercase) for i in range(length))

print("==Spotify Account Generator by AncientBanana♥, modified thanks to kacemws\n")

ips= [
	"http://128.199.202.122:3128",
	"http://101.4.136.34:8080",
	"http://138.68.60.8:8080",
	"http://150.129.151.42:6666",
	"http://140.227.237.154:1000",
	"http://46.160.123.115:8080",
	"http://5.252.161.48:8080",
	"http://193.106.130.249:8080",
	"http://200.24.17.54:8080",
	"http://200.229.227.237:8080",
	"http://119.252.161.110:80",
	"http://221.1.200.242:43399",
	"http://5.22.154.50:34895",
	"http://200.73.128.86:80",
	"http://122.154.72.102:8080",
	"http://201.59.214.82:8080",
	"http://118.175.93.103:48214",
	"http://179.159.208.233:8080",


]

print("Setting up..")
accs = input("Enter the number of accounts to be generated:\n")
for i in range(int(accs)):
	user = getRandomText(8)
	passw = "password"
	email = user+"@gmail.com"
	payload = {"creation_point": "client_mobile",
			"gender": "male",
			"postal_code": 1,
			"birth_year": 1995,
			"username": user,
			"iagree": 1,
			"birth_month": 4,
			"password_repeat": passw,
			"password": passw,
			"invitecode": "",
			"key": "142b583129b2df829de3656f9eb484e6",
			"platform": "Android-ARM",
			"email": email,
			"birth_day": 9,
			"creation_flow": "client_mobile"}
	headers={"Accept-Encoding": "gzip",
			 "Accept-Language": "it-IT;q=1, en-US;q=0.5",
			 "Connection": "Keep-Alive",
			 "Content-Type": "application/x-www-form-urlencoded",
			 "Host": "www.spotify.com",
			 "User-Agent": "Spotify/8.4.38 Android/25 (GT-P7500)"}

	print("Sending request..")
	proxy_index = random.randint(0,len(ips)-1)
	proxyDict = {
		'http' : ips[proxy_index],
		'https' : ips[proxy_index]
	}
	print(ips[proxy_index])
	r = requests.post('https://www.spotify.com/int/xhr/json/sign-up/', headers=headers, data=payload)

	if r.status_code==200:
		if r.json()['status']==1:
			print("Account created successfully!")
			print("User: "+user)
			print("Password: "+passw)
			print("Email: "+email)
			with open('email.txt', 'a+') as f:
				f.write(email+"\n")
		else:
			print("Could not create the account.")
			print("Response error:")
			print(r.json()['errors'])
	else:
		print("Could not load the page, some errors occurred. Response code:", r.status_code)
print("Accounts were generated. Thank you for using this generator :D")
exit()
f.close()