import requests
import os
from colorama import Fore , init
import time
init(autoreset=False)

os.system("clear" if os.name == "nt" "cls" else "clear")


def started():
    print(Fore.LIGHTRED_EX + """ 
    ┌─────────────────────────────────────────────┐
    │              *** Proxy ***                  │ 
    ├─────────────────────────────────────────────┤
    │       Gelistirilme Asamasındadır            │
    │          + Eklenicek                        │
    │          + Eklenicek                        │
    │          + Eklenicek                        │
    │          + Eklenicek                        │
    ├─────────────────────────────────────────────┤
    │ Link: https://github.com/mrhacker51         │             
    └─────────────────────────────────────────────┘
    """)


started()

class Proxy():
    def __init__(self):
        self.url = "https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&country=all"
    def request(self):
        response = requests.get(f"{self.url}").text
        return response

answered = Proxy()

def get_proxy():
    while True:
        try:
            kullanici = input(Fore.YELLOW + "1-Proxy Cek : \n2-Exit :\n")
            if kullanici == "2":
                print("Bye Bye")
                break
            else:
                if kullanici == "1":
                    x = answered.request()
                    with open("proxies.txt","w") as proxy:
                        new_x_file = proxy.write(x)
                        finally_x = len(open("proxies.txt").readlines())
                        os.system("clear" if os.name == "nt" "cls" else "clear")
                        time.sleep(0.5)
                        print(Fore.GREEN+f"Bulunan proxy adresi : {str(finally_x)}")
                        print(Fore.RED + "Proxy adresleri 'proxies.txt'ye kayit olmustur")
                        break
        except KeyboardInterrupt:
            break

get_proxy()
