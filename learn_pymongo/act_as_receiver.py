import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
import time
while(True):
    for x in mycol.find():
      print(x)
    print("wait for 5 seconds ##############################")
    time.sleep(5)  
