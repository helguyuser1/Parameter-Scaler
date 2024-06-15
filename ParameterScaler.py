import requests
import os
from urllib.parse import urlparse
import fade
from colorama import Fore

def clear():
    if os.name == 'nt': 
        os.system('cls')
    else:  
        os.system('clear')

def params(url):
    parsedUrl = urlparse(url)
    return bool(parsedUrl.query)

def rmvd(urls):
    filteredUrls = set()
    folders = set()
    for url in urls:
        path = urlparse(url).path
        folder = path.split('/')[-1]
        if folder not in folders:
            filteredUrls.add(url)
            folders.add(folder)
    return filteredUrls

def find(siteUrl):
    foundUrls = set()
    try:
        userresponse = input(Fore.RESET+"\n[?] Hard Mode (y/n) \n> ")
        if userresponse == "y":
            url = f"https://web.archive.org/cdx/search/cdx?url=*.{siteUrl}/*&output=txt&fl=original&collapse=urlkey&page=/"
        else:
            url = f"https://web.archive.org/cdx/search/cdx?url={siteUrl}/*&output=txt&fl=original&collapse=urlkey&page=/"
        clear()
        printbanner()
        print(Fore.RESET+F"[!] Searching... (Target: {Fore.YELLOW+siteUrl+Fore.RESET})")
        r = requests.get(url)
        if r.status_code == 200:
            lines = r.text.splitlines()
            for line in lines:
                foundUrls.add(line)
        else:
            print(f"[ X ] Error: {r.status_code}")
    except Exception as e:
        print(f"[ X ] Error: {str(e)}")
    return foundUrls

def save(urls, siteUrl):
    try:
        fileName = siteUrl.replace('https://', '').replace('http://', '')  
        if fileName.endswith('/'):
            fileName = fileName[:-1]  
        fileName += ".txt"

        if os.path.exists(fileName):
            number = 1
            while True:
                fileNameWithNumber = f"{fileName[:-4]} ({number}).txt"
                if not os.path.exists(fileNameWithNumber):
                    break
                number += 1
            fileName = fileNameWithNumber
        
        with open(fileName, 'w') as file:
            for url in urls:
                file.write(url + '\n')
        print(f"\n[ * ] URLs saved in > '{fileName}'.")
    except Exception as e:
        print(f"[ X ] Error while saving URLs: {str(e)}")

clear()
def printbanner():
    banner = """
        __  __________    __    ________  ____  __
    / / / / ____/ /   / /   / ____/ / / /\ \/ /
    / /_/ / __/ / /   / /   / / __/ / / /  \  / 
    / __  / /___/ /___/ /___/ /_/ / /_/ /   / /  
    /_/ /_/_____/_____/_____/\____/\____/   /_/   
                                                
        ✸  Tool made BY: Hellguy ! ✸
    """;print(fade.fire(banner))
printbanner()
option = input("[1] - Only Parameters\n[2] - All URLs\n:> " + Fore.CYAN)
print(Fore.RESET)
clear()
printbanner()
if option == "1":
    siteUrl = input("[-] Domain (ex: youtube.com)\n:> " + Fore.CYAN)
    urls = find(siteUrl)
    urls = rmvd(urls)
    print(Fore.YELLOW+"\n[ + ] URLs found with parameters:\n", Fore.RESET)
    for url in urls:
        if params(url):
            print(f"[{Fore.YELLOW}PARAMETER{Fore.RESET}]: "+Fore.CYAN + url + Fore.RESET)
    save(urls, siteUrl)

elif option == "2":
    siteUrl = input("[-] Domain (ex: youtube.com)\n:> " + Fore.CYAN)
    urls = find(siteUrl)
    urls = rmvd(urls)
    print(Fore.YELLOW+"\n[ + ] URLs Found:\n", Fore.RESET)
    for url in urls:
        if params(url):
            print(Fore.RESET + f"[{Fore.YELLOW}PARAMETER{Fore.RESET}]: "+Fore.CYAN + url + Fore.RESET)
        else:
            print(Fore.CYAN + url + Fore.RESET)
    save(urls, siteUrl)
exit()
