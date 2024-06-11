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
clear()
text = """
  Termux is bad ~ hellguy
    
 ██░ ██ ▓█████  ██▓     ██▓      ▄████  █    ██▓██   ██▓
▓██░ ██▒▓█   ▀ ▓██▒    ▓██▒     ██▒ ▀█▒ ██  ▓██▒▒██  ██▒
▒██▀▀██░▒███   ▒██░    ▒██░    ▒██░▄▄▄░▓██  ▒██░ ▒██ ██░
░▓█ ░██ ▒▓█  ▄ ▒██░    ▒██░    ░▓█  ██▓▓▓█  ░██░ ░ ▐██▓░
░▓█▒░██▓░▒████▒░██████▒░██████▒░▒▓███▀▒▒▒█████▓  ░ ██▒▓░
 ▒ ░░▒░▒░░ ▒░ ░░ ▒░▓  ░░ ▒░▓  ░ ░▒   ▒ ░▒▓▒ ▒ ▒   ██▒▒▒ 
 ▒ ░▒░ ░ ░ ░  ░░ ░ ▒  ░░ ░ ▒  ░  ░   ░ ░░▒░ ░ ░ ▓██ ░▒░ 
 ░  ░░ ░   ░     ░ ░     ░ ░   ░ ░   ░  ░░░ ░ ░ ▒ ▒ ░░  
 ░  ░  ░   ░  ░    ░  ░    ░  ░      ░    ░     ░ ░     
                                                ░ ░      
    ✸ Misuse of the tool can lead to ARREST! ✸
    ✸  Tool made to FACILITATE BUG BOUNTY! ✸
"""

faded_text = fade.pinkred(text)
print(faded_text)

option = input("[1] - Only Parameters\n[2] - All URLs\n>> " + Fore.CYAN)
print(Fore.RESET)
if option == "1":
    

    def check_params(url):
        parsed_url = urlparse(url)
        if parsed_url.query:
            return True
        return False

    def remove_duplicate_folders(urls):
        filtered_urls = set()
        folders = set()
        for url in urls:
            path = urlparse(url).path
            folder = path.split('/')[-1]
            if folder not in folders:
                filtered_urls.add(url)
                folders.add(folder)
        return filtered_urls

    def find_urls(site_url):
        found_urls = set()
        try:
            url = f"https://web.archive.org/cdx/search/cdx?url=*.{site_url}/*&output=txt&fl=original&collapse=urlkey&page=/"
            response = requests.get(url)
            if response.status_code == 200:
                lines = response.text.splitlines()
                for line in lines:
                    if line not in found_urls:
                        found_urls.add(line)
            else:
                print(f"[۞] Error: {response.status_code}")
        except Exception as e:
            print(f"[۞] Error: {str(e)}")
        return found_urls

    def save_urls(urls, site_url):
        try:
            file_name = site_url.replace('https://', '').replace('http://', '')  
            if file_name.endswith('/'):
                file_name = file_name[:-1]  
            file_name += ".txt"

            if os.path.exists(file_name):
                number = 1
                while True:
                    file_name_with_number = f"{file_name[:-4]} ({number}).txt"
                    if not os.path.exists(file_name_with_number):
                        break
                    number += 1
                file_name = file_name_with_number
            
            with open(file_name, 'w') as file:
                for url in urls:
                    file.write(url + '\n')
            print(f"[۞] URLs saved in >>> '{file_name}'.")
        except Exception as e:
            print(f"[۞] Error while saving URLs: {str(e)}")

    site_url = input("URL (https/http)\n>> " + Fore.CYAN)
    urls = find_urls(site_url)
    urls = remove_duplicate_folders(urls)

    print("[۞] URLs found with parameters:")
    for url in urls:
        if check_params(url):
            print(Fore.GREEN + url + Fore.RESET)

    save_urls(urls, site_url)
    exit1 = input("[۞] EXIT >> press enter to close the window.")
elif option == "2":
    def check_params(url):
        parsed_url = urlparse(url)
        if parsed_url.query:
            return True
        return False

    def remove_duplicate_folders(urls):
        filtered_urls = set()
        folders = set()
        for url in urls:
            path = urlparse(url).path
            folder = path.split('/')[-1]
            if folder not in folders:
                filtered_urls.add(url)
                folders.add(folder)
        return filtered_urls

    def find_urls(site_url):
        found_urls = set()
        try:
            url = f"https://web.archive.org/cdx/search/cdx?url=*.{site_url}/*&output=txt&fl=original&collapse=urlkey&page=/"
            response = requests.get(url)
            if response.status_code == 200:
                lines = response.text.splitlines()
                for line in lines:
                    if line not in found_urls:
                        found_urls.add(line)
            else:
                print(f"[۞] Error: {response.status_code}")
        except Exception as e:
            print(f"[۞] Error: {str(e)}")
        return found_urls

    def save_urls(urls, site_url):
        try:
            file_name = site_url.replace('https://', '').replace('http://', '')  
            if file_name.endswith('/'):
                file_name = file_name[:-1]  
            file_name += ".txt"

            if os.path.exists(file_name):
                number = 1
                while True:
                    file_name_with_number = f"{file_name[:-4]} ({number}).txt"
                    if not os.path.exists(file_name_with_number):
                        break
                    number += 1
                file_name = file_name_with_number
            
            with open(file_name, 'w') as file:
                for url in urls:
                    file.write(url + '\n')
            print(f"[۞] URLs saved in >>> '{file_name}'.")
        except Exception as e:
            print(f"[۞] Error while saving URLs: {str(e)}")

    site_url = input("URL (https/http)\n>> " + Fore.CYAN)
    urls = find_urls(site_url)
    urls = remove_duplicate_folders(urls)

    print("[۞] URLs found:")
    for url in urls:
        if check_params(url):
            print(Fore.RED + "[!] Parameter Found: " + url + Fore.RESET)
        else:
            print(Fore.GREEN + url + Fore.RESET)

    save_urls(urls, site_url)
    exit1 = input("[۞] EXIT >> press enter to close the window.")
