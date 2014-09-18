import pymongo
import datetime
import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

def remove_review_date():
   print "\n\nremoving all the review dates"

   # get a handle to the test database
   db = connection.test
   scores = db.scores

   try:
      scores.update({}, {'$unset':{'review_date':1}}, multi=True)

   except:
      print "Unexpected error:", sys.exc_info()[0]
      raise

# preform wholesale replacement of a document
def using_save():
   # get a handle to the test database
   db = connection.test
   scores = db.scores
   
   print "updating record using save"

   try:
      # get the doc
      query = {'student':1, 'type':'exam'}
      score = scores.find_one(query)
      print "before: ", score

      # add a review date
      score['review_date'] = datetime.datetime.utcnow()
      
      # update the record with convenience method
      scores.save(score)
      score = scores.find_one(query)
      print "after: ", score

   except:
      print "Unexpected error:", sys.exc_info()[0]
      raise

# perform wholesale replacement of document
def using_update():
   print "updating record using update"

   # get a handle to the test database
   test = connection.test
   scores = test.scores

   try:
      # get the doc
      query = {'student': 1, 'type':'exam'}
      score = scores.find_one(query)
      print "before: ", score

      # add a review date
      score['review_date'] = datetime.datetime.utcnow()

      # update the record with update. Note that there is an _id field but the DB is O.K. with that
      # because it matches what was there.
      scores.update(query, score)

      score = scores.find_one(query)
      print "after: ", score

   except:
      print "Unexpected error:", sys.exc_info()[0]
      raise

# perform the update using set
def using_set():
   print "updating record using set"
   # get a handle to the database
   test = connection.test
   scores = test.scores

   try:
      # get the doc
      query = {'student':1, 'type':'exam'}
      score = scores.find_one(query)
      print "before: ", score

      # update using set
      scores.update(query, {'$set':{'review_date':datetime.datetime.utcnow()}})

      score = scores.find_one(query)
      print "after: ", score

   except:
      print "Unexpected error:", sys.exc_info()[0]
      raise
      

if __name__ == '__main__':
   remove_review_date()
   using_save()
   remove_review_date()
   using_update()
   remove_review_date()
   using_set()
