import sys

import pymongo


# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the test database
db = connection.test
people = db.people

print "insert, reporting for dutty"

richard = {"name": "Richard Kreuter", "company": "10gen",
           "interests": ['horses', 'skydiving', 'fencing']}
andrew = {"_id": "erlichson", "name": "Andrew Erlichson", "company": "10gen",
          "interests": ['running', 'cycling', 'photography']}

try:
    people.insert(richard)
    people.insert(andrew)

except:
    print "Unexpected error:", sys.exec_info()[0]

print(richard)
print(andrew)

