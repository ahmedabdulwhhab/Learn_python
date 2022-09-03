#2) Creating a Database
print('Create a database called "mydatabase":')

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]

#3)Check if Database Exists

dblist = myclient.list_database_names()
print('dblist', dblist)
if "mydatabase" in dblist:
  print("The database exists.")
