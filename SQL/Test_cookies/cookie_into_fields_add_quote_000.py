import requests
import threading
import argparse
from colorama import Fore, Style, init
import urllib3
from http.cookies import SimpleCookie

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Example cookie string
cookie_string = """api_uid=CnBoZGeEEp2QggBdS61hAg==; _bee=1f3rGHksg10p6O7cK7ASnd8omzfxvaoE; njrpl=1f3rGHksg10p6O7cK7ASnd8omzfxvaoE; dilx=FZIc4gsRHvYKhuKOWEJQf; hfsc=L3yJfo4w4Tnw05LKfQ==; AccessToken=TBQGY6TE7DV5W2U73PMFF7E2SGEORJUC7HYDUQEMXU7WUV32NDXA0110d253d05a; user_uin=BALW7KC65EVLZOBYAMOJEUTHFCLUFWVUTPTIO3SP; isLogin=1739261640806; __cf_bm=Of69u04xWfTtlkuVtQ.EiPBcSdp5xqj_6aNcfnQ5iyY-1739297927-1.0.1.1-9SJCtwioWvA8ZtmFjWkQmzplRirRugOU0vm70AjpqIbjwxzb3DkrDhhgZTr6vPFAzflXRxbfF.Eu24wwizxVZA"""

#cookies={"session_id":"ahmed",      "TracingId":"sally"}

url= "https://www.temu.com/api/server/_stm?t=1739119294447"
proxies = {
            "http": "http://127.0.0.1:8090",
            "https": "http://127.0.0.1:8090"
        }



def initiate_request():
    #try:

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0',
            'Accept': 'application/json, text/plain,txt/doc, */*'
        }
            # Character to find
        char = ";"
    
        count = 0
        for index, c in enumerate(cookie_string):
            if c == char:
                #if count == 2:
                # Extract "value"
                cookie_string_mod = cookie_string[0:index] +"';"+cookie_string[index+1:]
                print(cookie_string_mod)  # Output: Hello
                
                cookies = (dict(i.split('=',1) for i in cookie_string_mod.split(';')))
                # # Split the cookie into key-value pairs           
                # cookies_str = cookie_string_mod.split("; ")
                # print("cookie_string_mod " ,cookie_string_mod)
                # print("cookies_str " ,cookies_str)
                # cookie_dict={}
                # for pair in cookie_string_mod.split(";"):
                    # key, value = pair.strip.split("=",1)
                    # cookie_dict[key]= value
                    # print("key = ", key," value = ",value)
                # print(cookie_dict)    
                # #cookies.load(cookies_str)
                #print(cookies)
                response = requests.get(url, proxies=proxies,cookies=cookies, verify=False,headers=headers)
                if response.status_code == 200:
                    #print(Fore.GREEN + f"Success: {url} - Status Code: {response.status_code}")
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
        
    #except Exception as e:
    #    print(Fore.RED + f"Failed: {url} - Error: {str(e)}")
        
        
        


initiate_request()