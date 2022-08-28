#h1 python3 /home/ubuntu/sdn/projects/multi-path/time_out_ping.py



import time
import urllib.request
import urllib.error
import os


def uptime_bot(msg):
    while True:
        try:
            tick= time.time()
            print("tick = " ,tick)
            os.system("ping -c1 10.0.0.2")
            print("time.time() -  tick =" ,time.time()- tick)
        except: 
            print('Error')
        time.sleep(3)

if __name__ == '__main__':
    msg = 'In the name of Allah'
    uptime_bot(msg)