import bottle

# this is the handler for the default path of the web server
# added another comment

@bottle.route('/')
def index():
    # connect to mongoDB
    # connection = pymongo.MongoClient('localhost', 27017)

    # attach to test database
    # db = connection.test

    # get handle for names collection
    # name = db.names

    # find a single document
    # item = name.find_one()

    return '<b>Hello World!</b>'

# run the webserver
bottle.run(host='localhost', port=8000)
