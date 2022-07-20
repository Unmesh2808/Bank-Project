from re import I
import pymongo
from pymongo import MongoClient

client = pymongo.MongoClient("mongodb://127.0.0.1:27017")

db = client.Project1

mycol = db["mybank"]


def initialize(doc1):
    db.mybank.insert_one(doc1)

def acquire(dict1):
    return db.mybank.find(dict1)

def edit(bal, pin):
    db.mybank.update_one({"Pin":pin},{'$set':{"Balance":bal}})
    print("Balance updated successfully")
    
#acquire({"AcnNum":"BOI1941"})
# data1 =  db.mybank.find({"AcnNum":"ICICI76591"})
# for i in data1:
#     print(i)    