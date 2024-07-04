import pymongo 
import os
from helper.date import add_date
from info.py import *
mongo = pymongo.MongoClient(DB_URL)
db = mongo[DB_NAME]
dbcol = db["premium"]

def add_premium(chat_id):
	date = add_date()
	user_id = int(chat_id)
	user_data = {"_id":user_id, "date":date[0]}
	try:
		dbcol.insert_one(user_data)
	except:
		print("error")
		pass

def delete(chat_id):
	dbcol.delete_one(chat_id)


def find_one(id):
	return dbcol.find_one({"_id":id})
