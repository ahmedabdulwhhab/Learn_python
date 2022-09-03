import pymongo


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
from datetime import datetime


mydict = { "name": "John", "arrive_at": str(datetime.now()) }

x = mycol.insert_one(mydict)

#Insert another record in the "customers" collection, and return the value of the _id field:

mydict = { "name": "Peter", "arrive_at": str(datetime.now())}

x = mycol.insert_one(mydict)

print(x.inserted_id)

