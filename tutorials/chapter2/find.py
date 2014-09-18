import pymongo
import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the test database
db = connection.test
scores = db.scores

def find():
   print "find, report for duty"

   query = {'type': 'exam', 'score': {'$gt':50, '$lt': 70}}
   selector = {'_id': 0, 'student': 1}

   try:
      cursor = scores.find(query)

   except:
      print "Unexpected error:", sys.exc_info()[0]

   sanity = 0
   for doc in cursor:
      print doc
      sanity += 1
      if (sanity > 10):
         break


def find_one():
   print "find one, reporting for duty"
   query = {'student':10}
   
   try:
      doc = scores.find_one(query)

   except:
      print "Unexpected error:", sys.exc_info()[0]

   print doc

#find_one()
find()
