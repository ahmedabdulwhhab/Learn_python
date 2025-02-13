import requests
import threading
import argparse
from colorama import Fore, Style, init
import urllib3
from http.cookies import SimpleCookie

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Example cookie string
url= "https://www.temu.com/search_result.html?search_key=dual%2Bscale%2Bgauge%2Bpress&search_method=recent&refer_page_el_sn=200254&srch_enter_source=top_search_entrance_10005&refer_page_name=home&refer_page_id=10005_1739299221590_49z62vtjr3&refer_page_sn=10005&_x_sessn_id=34rhmnzlno"

cookie_string = """api_uid=CnBoZGeEEp2QggBdS61hAg==; region=210; language=en; currency=GBP; timezone=Africa%2FCairo; _nano_fp=Xpmqn5mol0m8npXaX9_8KK9ZMaiH8g44jj_OIuX5; _bee=1f3rGHksg10p6O7cK7ASnd8omzfxvaoE; njrpl=1f3rGHksg10p6O7cK7ASnd8omzfxvaoE; dilx=FZIc4gsRHvYKhuKOWEJQf; hfsc=L3yJfo4w4Tnw05LKfQ==; g_state={"i_p":1736716149205,"i_l":1}; _hal_tag=APVkxVFf/z6mfCzQGTDC4mfpLtfe2s/4m58ETt4MXE0VxTG0r3Q2WuQ7RwQUGPFdRg==; AccessToken=TBQGY6TE7DV5W2U73PMFF7E2SGEORJUC7HYDUQEMXU7WUV32NDXA0110d253d05a; user_uin=BALW7KC65EVLZOBYAMOJEUTHFCLUFWVUTPTIO3SP; isLogin=1739261640806; privacy_setting_detail=%7B%22firstPAds%22%3A0%2C%22adj%22%3A0%2C%22fbsAnlys%22%3A0%2C%22fbEvt%22%3A0%2C%22ggAds%22%3A0%2C%22fbAds%22%3A0%2C%22ttAds%22%3A0%2C%22scAds%22%3A0%2C%22ptAds%22%3A0%2C%22bgAds%22%3A0%2C%22tblAds%22%3A0%2C%22obAds%22%3A0%7D; webp=1; __cf_bm=1rBmnGt2Zh6XdZEu8Am2zu_QY9oYzYZHeUOPUZa3MmY-1739298831-1.0.1.1-L93Iyi0tbXpjScs5hICLlpslC9dYxjzRakfPeH6rR5BCgB9rR1EJvh3adhU_6Q8Pgpe6JQt0sGuR04UNYekK2Q"""

proxies = {
            "http": "http://127.0.0.1:8090",
            "https": "http://127.0.0.1:8090"
        }




def initiate_request():
    try:

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0',
            'Accept': 'application/json, text/plain,txt/doc, */*',
            'Connection': 'keep-alive'
        }
        cookie_string_mod = cookie_string
        cookies = (dict(i.split('=',1) for i in cookie_string_mod.split(';')))

        response = requests.get(url, proxies=proxies,cookies=cookies, verify=False,headers=headers)
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
        
        
        


initiate_request()