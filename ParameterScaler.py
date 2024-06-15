import requests
import os
from urllib.parse import urlparse
import fade
from colorama import Fore, Style

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
        url = f"https://web.archive.org/cdx/search/cdx?url=*.{siteUrl}/*&output=txt&fl=original&collapse=urlkey&page=/"
        response = requests.get(url)
        if response.status_code == 200:
            lines = response.text.splitlines()
            for line in lines:
                foundUrls.add(line)
        else:
            print(f"[X] Error: {response.status_code}")
    except Exception as e:
        print(f"[X] Error: {str(e)}")
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
        print(f"[*] URLs saved in > '{fileName}'.")
    except Exception as e:
        print(f"[X] Error while saving URLs: {str(e)}")

clear()
banner = """
    __  __________    __    ________  ____  __
   / / / / ____/ /   / /   / ____/ / / /\ \/ /
  / /_/ / __/ / /   / /   / / __/ / / /  \  / 
 / __  / /___/ /___/ /___/ /_/ / /_/ /   / /  
/_/ /_/_____/_____/_____/\____/\____/   /_/   
                                              
    ✸  Tool made BY: Hellguy ! ✸
""";print(fade.fire(banner))

option = input("[1] - Only Parameters\n[2] - All URLs\n:> " + Fore.CYAN)
print(Fore.RESET)
if option == "1":
    siteUrl = input("URL (https/http)\n:> " + Fore.CYAN)
    urls = find(siteUrl)
    urls = rmvd(urls)

    print("\n[+] URLs found with parameters:\n")
    for url in urls:
        if params(url):
            print(Fore.GREEN + url + Fore.RESET)

    save(urls, siteUrl)
elif option == "2":
    siteUrl = input("URL (https/http)\n:> " + Fore.CYAN)
    urls = find(siteUrl)
    urls = rmvd(urls)

    print("\n[+] URLs Found:\n")
    for url in urls:
        if params(url):
            print(Fore.BLUE + "[!] Parameter found: " + url + Fore.RESET)
        else:
            print(Fore.GREEN + url + Fore.RESET)

    save(urls, siteUrl)

exit()
