import sys

import pymongo


# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")
db = connection.test
things = db.things


def using_upsert():
    print "updating with upsert"

    try:
        # lets remove all stuff from things
        things.drop()

        things.update({'thing': 'apple'}, {'$set': {'color': 'red'}}, upsert=True)
        # this upsert will not work because it will use the criteria on the right
        # to set the document. So, thing: pear will be dropped
        things.update({'thing': 'pear'}, {'color': 'red'}, upsert=True)

        apple = things.find_one({'thing': 'apple'})
        print "apple: ", apple
        pear = things.find_one({'thing': 'pear'})
        print "pear: ", pear

    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise


if __name__ == '__main__':
    using_upsert()
