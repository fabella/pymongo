import sys
import pymongo

# connect to mongo
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the reddit database
db = connection.reddit
stories = db.stories

def find():

   print "find, reporting for duty"

   expression = sys.argv[1]
   print expression
   query = {'title':{'$regex':expression}}
   projection = {'title': 1, '_id': 0}

   try:
      cursor = stories.find(query, projection)

   except:
      print "Unexpected error", sys.exc_info()[0]

   sanity = 0
   for doc in cursor:
      print doc
#      sanity += 1
#     if (sanity > 10)
#         break

find()
