import os, sys, time, shutil
try: 
    import requests 
except: 
    os.system("pip install requests")
    #pass
try: 
    import cfonts
    pass
except: 
    os.system("pip install python-cfonts")
    pass
try: 
    import threading
    pass
except: 
    os.system("pip install threading")
    pass
try: 
    import urllib
    pass
except: 
    os.system("pip install urllib")
    pass
from cfonts import render
from threading import active_count
threads = []
####
Y = '\x1b[1;33m'#اصفر
R = '\x1b[1;31m'#احمر
W = '\x1b[2;39m'#ابيض
P = '\x1b[2;35m'#بمبي
B = '\x1b[2;36m'#سماوي
G = '\x1b[2;32m'#اخضر
R = '\x1b[1;31m'#احمر
B = '\x1b[2;36m'#سماوي
print(R+"≈"*shutil.get_terminal_size().columns)
TerminalSize = shutil.get_terminal_size().columns
TextS = "Telegram viewer increase tool"
TextTer = TerminalSize-len(TextS)
Ttext = int(TextTer / 2)
print(R+"≈"*Ttext+B+TextS+R+"≈"*Ttext)
print(R+"≈"*shutil.get_terminal_size().columns)
####
Y = '\x1b[1;33m'#اصفر
TerminalSize = shutil.get_terminal_size().columns
TextS = "# MarCo #"
TextTer = TerminalSize-len(TextS)
Ttext = int(TextTer / 2)
print(Y+" "*Ttext+Y+TextS+R+" "*Ttext)
####
lsd = 'https://pastebin.com/raw/mNDV5UMF'
jd = requests.get(lsd).text
while True :
 p = input(P+"Password: ")
 if p == jd:
  break
 else:
   print (R+"Error Password Please Try again")
n_threads = int(input(Y+"[+] ENTER SPEED: "))  
mm =    input(B+"[+] Post link: ")
links =    [mm]
while True:
    marko =    input(Y+"[+] Post link, to finish please write 1: ")
    if marko !=    "1" :
        links.append(marko)
    else:
        print(G+"\n Post links saved successfully in progress...")
        break
print("\n")
TerminalSize = shutil.get_terminal_size().columns
TextS = "View results sent"
TextTer = TerminalSize-len(TextS)
Ttext = int(TextTer / 2)
print(R+"≈"*Ttext+B+TextS+R+"≈"*Ttext)
print("\n")
#################
def view2(proxy):
    for i in links:
        channel = i.split('/')[3]
        msgid = i.split('/')[4]
        send_seen(channel, msgid, proxy)
###############
def send_seen(channel, msgid, proxy):
    s = requests.Session()
    proxies = {
        'http': proxy,
        'https': proxy,
    }
    try:
        a = s.get("https://t.me/"+channel+"/"+msgid,
                  timeout=10, proxies=proxies)
        cookie = a.headers['set-cookie'].split(';')[0]
    except Exception as e:
        return False
    h1 = {"Accept": "*/*", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US,en;q=0.9,fa;q=0.8,de;q=0.7", "Connection": "keep-alive", "Content-Length": "5", "Content-type": "application/x-www-form-urlencoded",
          "Cookie": cookie, "Host": "t.me", "Origin": "https://t.me", "Referer": "https://t.me/"+channel+"/"+msgid+"?embed=1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "User-Agent": "Chrome"}
    d1 = {"_rl": "1"}
    try:
        r = s.post('https://t.me/'+channel+'/'+msgid+'?embed=1',
                   json=d1, headers=h1, proxies=proxies)
        key = r.text.split('data-view="')[1].split('"')[0]
        now_view = r.text.split('<span class="tgme_widget_message_views">')[1].split('</span>')[0]
        if now_view.find("K") != -1:
            now_view = now_view.replace("K","00").replace(".", "")
    except Exception as e:
        return False
    h2 = {"Accept": "*/*", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US,en;q=0.9,fa;q=0.8,de;q=0.7", "Connection": "keep-alive", "Cookie": cookie, "Host": "t.me",
          "Referer": "https://t.me/"+channel+"/"+msgid+"?embed=1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "User-Agent": "Chrome", "X-Requested-With": "XMLHttpRequest"}
    try:
        i = s.get('https://t.me/v/?views='+key, timeout=10,
                  headers=h2, proxies=proxies)
        if(i.text == "true"):
            for i in now_view:
                print(G+f"{now_view} views have been provided", end="\r")
                time.sleep(0.0)           
    except Exception as e:
        return False
    try:
        h3 = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US,en;q=0.9,fa;q=0.8,de;q=0.7",
              "Cache-Control": "max-age=0", "Connection": "keep-alive", "Cookie": cookie, "Host": "t.me", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "none", "Sec-Fetch-User": "?1", "Upgrade-Insecure-Requests": "1", "User-Agent": "Chrome"}
        s.get("https://t.me/"+channel+"/"+msgid, headers=h3,
              timeout=10, proxies=proxies)
    except Exception as e:
        return False

def scrap():
    try:
        https = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=https&timeout=0", proxies=urllib.request.getproxies(), timeout=5).text
        http = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=0", proxies=urllib.request.getproxies(), timeout=5).text
        socks = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=0", proxies=urllib.request.getproxies(), timeout=5).text
    except Exception as e:
        print(e)
        return False
    f = open("proxies.txt", "w")
    f.write(https+"\n"+http)
    f.close()
    f = open("socks.txt", "w")
    f.write(socks)
    f.close()
    
def checker(proxy):
    proxies = {
        'http': proxy,
        'https': proxy,
    }
    try:
#        requests.get("https://t.me/Elshafey_Team/504", timeout=12, proxies=proxies)
        view2(proxy)
    except Exception as e:
        return False

def start():
    s = scrap()
    if s == False:
        return
    list = open('proxies.txt', 'r')
    proxies = list.readlines()
    list.close()
    for i in proxies:
        p = i.split('\n')[0]
        if not p:
            continue
        while active_count() > n_threads:
            liiii=9
        thread = threading.Thread(target=checker, args=(p,))
        threads.append(thread)
        thread.start()

    list = open('socks.txt', 'r')
    proxies = list.readlines()
    list.close()
    for i in proxies:
        p = i.split('\n')[0]
        if not p:
            continue
        while active_count() > n_threads:
          lii7ii=99
        pr = "socks5://"+p
        thread = threading.Thread(target=checker, args=(pr,))
        threads.append(thread)
        thread.start()
    
    
    return True
    
            
def process(run_for_ever:bool = False):
    if run_for_ever:
        while True:
            start()
    else:
        start()

process(True)