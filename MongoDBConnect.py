from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string

def mongoConnect():
 client = MongoClient("127.0.0.1:27017")
 #db = client.AttractionDetails.Attraction.find()
 return client
# Issue the serverStatus command and print the results
#serverStatusResult = db1.command("serverStatus")
 for document in db:
  pprint(document)