import os
import pymongo
import datetime
from pymongo import MongoClient
from bson.objectid import ObjectId

MONGO_URL = os.getenv('MONGOLAB_URI', 'mongodb://admin:admin@oceanic.mongohq.com:10086/ztis')

client = MongoClient(MONGO_URL)
db = client.ztis
collection = db.data

def get_data_collection():
  return collection;

def find_all():
  return collection.find()

def find(data_id):
  try:
    object_id = ObjectId(data_id)
  except:
    return None
  return collection.find_one({"_id": object_id})

def insert(data):
  return collection.insert({'date': str(datetime.datetime.now()), 'data': data})

def insertEvents(events):
  for e in events:
  	collection.insert(e)
