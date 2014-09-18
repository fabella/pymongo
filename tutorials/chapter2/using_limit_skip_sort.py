import sys
import pymongo

# connect to mongo
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the reddit database
db = connection.test
scores = db.scores

def find():

   print "find, reporting for duty"

   query = {}

   try:
      cursor = scores.find(query).skip(4).limit(3)
      cursor = cursor.sort('student', pymongo.ASCENDING)
   
      #cursor = cursor.sort([('student', pymongo.ASCENDING), ('score', pymongo.DESCENDING'])

   except:
      print "Unexpected error", sys.exc_info()[0]

   sanity = 0
   for doc in cursor:
      print doc
#      sanity += 1
#     if (sanity > 10)
#         break

find()
