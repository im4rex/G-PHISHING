from ZaidPP import Zaid
from darklib import *
import random
import threading
import requests
import os
E = '\033[1;31m'
Z = '\033[1;31m' #احمر
R = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
C1 = '\033[2;35m'
G = '\033[1;35m'
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
V = '\033[1;16m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
M = '\x1b[1;37m'#ابیض
S = '\033[1;33m'
U = '\x1b[1;37m'#ابیض
BRed = '\x1b[1;31m'
BGreen = '\x1b[1;32m'
BYellow = '\x1b[1;33m'
BBlue = '\x1b[1;34m'
BPurple= '\x1b[1;35m'
BCyan = '\x1b[1;36m'
token = '7096521801:AAHua0nUQv0OgXvcodPRPOhKSDhBEZAK-mQ'

ID= '6418195079'

s=0
o=0
t=0
g=0
e=0
def users():
	while True:
		global g,t,o,s,e
		user='1234567890qwertyuiopasdfghjklzxcvbnm.'
		
		num='89'
		rng=int("".join(random.choice(num)for i in range(1)))
		name=str("".join(random.choice(user)for i in range(rng)))
		email1=name
		email=email1+'@gmail.com'
		e+=1
		os.system('cls'if os.name=='net'else'clear')
		print(f'┏{Z}━━━━━━━━━━━━━━━━━━━━━━━━{Z}┓\n┃{F} ⌯ Good Tik Tok : {o} \n{Z}┗{Z}━━━━━━━━━━━━━━━━━━━━━━━━{Z}┛{Z}\n┏{Z}━━━━━━━━━━━━━━━━━━━━━━━━{Z}┓\n┃{X} ⌯ Good Gmail: {s} \n{Z}┗{Z}━━━━━━━━━━━━━━━━━━━━━━━━{Z}┛ \n┏{Z}━━━━━━━━━━━━━━━━━━━━━━━━{Z}┓\n┃{Z} ⌯ Bad Tik Tok : {t} \n┗{Z}━━━━━━━━━━━━━━━━━━━━━━━━{Z}┛\n┏{Z}━━━━━━━━━━━━━━━━━━━━━━━━{Z}┓\n┃{Z} ⌯ Bad Gmail : {g}\n{Z}┗{Z}━━━━━━━━━━━━━━━━━━━━━━━━{Z}┛ \n┏{Z}━━━━━━━━━━━━━━━━━━━━━━━━{Z}┓\n┃{B} ⌯ Email : {e} »» {email} \n{Z}┗{Z}━━━━━━━━━━━━━━━━━━━━━━━━{Z}┛')
		m = check.gmail(email)
		if m['status'] == "Success":
			s+=1
			os.system('cls'if os.name=='net'else'clear')
			print(f'┏{Z}━━━━━━━━━━━━━━━━━━━━━━━━{Z}┓\n┃{F} ⌯ Good Tik Tok : {o} \n{Z}┗{Z}━━━━━━━━━━━━━━━━━━━━━━━━{Z}┛{Z}\n┏{Z}━━━━━━━━━━━━━━━━━━━━━━━━{Z}┓\n┃{X} ⌯ Good Gmail: {s} \n{Z}┗{Z}━━━━━━━━━━━━━━━━━━━━━━━━{Z}┛ \n┏{Z}━━━━━━━━━━━━━━━━━━━━━━━━{Z}┓\n┃{Z} ⌯ Bad Tik Tok : {t} \n┗{Z}━━━━━━━━━━━━━━━━━━━━━━━━{Z}┛\n┏{Z}━━━━━━━━━━━━━━━━━━━━━━━━{Z}┓\n┃{Z} ⌯ Bad Gmail : {g}\n{Z}┗{Z}━━━━━━━━━━━━━━━━━━━━━━━━{Z}┛ \n┏{Z}━━━━━━━━━━━━━━━━━━━━━━━━{Z}┓\n┃{B} ⌯ Email : {e} »» {email} \n{Z}┗{Z}━━━━━━━━━━━━━━━━━━━━━━━━{Z}┛')
			m = check.instagram(email)
			if m['status'] == "Success":
				o+=1
				os.system('cls'if os.name=='net'else'clear')
				print(f'┏{Z}━━━━━━━━━━━━━━━━━━━━━━━━{Z}┓\n┃{F} ⌯ Good Tik Tok : {o} \n{Z}┗{Z}━━━━━━━━━━━━━━━━━━━━━━━━{Z}┛{Z}\n┏{Z}━━━━━━━━━━━━━━━━━━━━━━━━{Z}┓\n┃{X} ⌯ Good Gmail: {s} \n{Z}┗{Z}━━━━━━━━━━━━━━━━━━━━━━━━{Z}┛ \n┏{Z}━━━━━━━━━━━━━━━━━━━━━━━━{Z}┓\n┃{Z} ⌯ Bad Tik Tok : {t} \n┗{Z}━━━━━━━━━━━━━━━━━━━━━━━━{Z}┛\n┏{Z}━━━━━━━━━━━━━━━━━━━━━━━━{Z}┓\n┃{Z} ⌯ Bad Gmail : {g}\n{Z}┗{Z}━━━━━━━━━━━━━━━━━━━━━━━━{Z}┛ \n┏{Z}━━━━━━━━━━━━━━━━━━━━━━━━{Z}┓\n┃{B} ⌯ Email : {e} »» {email} \n{Z}┗{Z}━━━━━━━━━━━━━━━━━━━━━━━━{Z}┛')
				tlg=f'{email} : متاح تيك توك'
				requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(tlg))
			else:
				t+=1
				os.system('cls'if os.name=='net'else'clear')
				print(f'┏{Z}━━━━━━━━━━━━━━━━━━━━━━━━{Z}┓\n┃{F} ⌯ Good Tik Tok : {o} \n{Z}┗{Z}━━━━━━━━━━━━━━━━━━━━━━━━{Z}┛{Z}\n┏{Z}━━━━━━━━━━━━━━━━━━━━━━━━{Z}┓\n┃{X} ⌯ Good Gmail: {s} \n{Z}┗{Z}━━━━━━━━━━━━━━━━━━━━━━━━{Z}┛ \n┏{Z}━━━━━━━━━━━━━━━━━━━━━━━━{Z}┓\n┃{Z} ⌯ Bad Tik Tok : {t} \n┗{Z}━━━━━━━━━━━━━━━━━━━━━━━━{Z}┛\n┏{Z}━━━━━━━━━━━━━━━━━━━━━━━━{Z}┓\n┃{Z} ⌯ Bad Gmail : {g}\n{Z}┗{Z}━━━━━━━━━━━━━━━━━━━━━━━━{Z}┛ \n┏{Z}━━━━━━━━━━━━━━━━━━━━━━━━{Z}┓\n┃{B} ⌯ Email : {e} »» {email} \n{Z}┗{Z}━━━━━━━━━━━━━━━━━━━━━━━━{Z}┛')
		else:
			g+=1
			os.system('cls'if os.name=='net'else'clear')
			print(f'┏{Z}━━━━━━━━━━━━━━━━━━━━━━━━{Z}┓\n┃{F} ⌯ Good Tik Tok : {o} \n{Z}┗{Z}━━━━━━━━━━━━━━━━━━━━━━━━{Z}┛{Z}\n┏{Z}━━━━━━━━━━━━━━━━━━━━━━━━{Z}┓\n┃{X} ⌯ Good Gmail: {s} \n{Z}┗{Z}━━━━━━━━━━━━━━━━━━━━━━━━{Z}┛ \n┏{Z}━━━━━━━━━━━━━━━━━━━━━━━━{Z}┓\n┃{Z} ⌯ Bad Tik Tok : {t} \n┗{Z}━━━━━━━━━━━━━━━━━━━━━━━━{Z}┛\n┏{Z}━━━━━━━━━━━━━━━━━━━━━━━━{Z}┓\n┃{Z} ⌯ Bad Gmail : {g}\n{Z}┗{Z}━━━━━━━━━━━━━━━━━━━━━━━━{Z}┛ \n┏{Z}━━━━━━━━━━━━━━━━━━━━━━━━{Z}┓\n┃{B} ⌯ Email : {e} »» {email} \n{Z}┗{Z}━━━━━━━━━━━━━━━━━━━━━━━━{Z}┛')
		
s1=threading.Thread(target=users,args=())
s2=threading.Thread(target=users,args=())
s3=threading.Thread(target=users,args=())
s1.start()
s3.start()
s2.start()