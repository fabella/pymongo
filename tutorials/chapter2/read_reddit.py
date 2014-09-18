import json
import urllib2
import pymongo

# connect to mongo
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the reddit database
db = connection.reddit
stories = db.stories

# get the reddit home page
reddit_page = urllib2.urlopen("http://www.reddit.com/r/technology/.json")

# parse the json
parsed = json.loads(reddit_page.read())
print parsed
# iterate through every news item on the page
for item in parsed['data']['children']:
#   # put it in mongo
   stories.insert(item['data'])

