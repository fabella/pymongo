import bottle
import pymongo

# connect to mongoDB
uri = "mongodb://admin:yKzDuTpSEKyzTwYiyvKi@ds033750.mongolab.com:33750/pymongo"
connection = pymongo.MongoClient(uri)

# attach to test database
db = connection.pymongo

# get handle for names collection
fruits = db.fruits

@bottle.route('/')
def home_page():
    # find all the fruits in the database
    my_things = fruits.find().sort("name", pymongo.ASCENDING)
    my_fruits = []
    #iterate and get the name
    for thing in my_things:
        my_fruits.append(thing['name'])
    return bottle.template('hello_world', username='Fidel', things=my_fruits)
    # return bottle.template('hello_world', {'username':'Fidel', 'things':my_things})

@bottle.route('/testpage')
def test_page():
    return "this is a test page"

@bottle.post('/favorite_fruit')
def favorite_fruit():
    fruit = bottle.request.forms.get("fruit")
    if fruit is None or fruit == "":
        fruit = "No Fruit Selected"
    else:
        fruits.save({'name': fruit})
    bottle.response.set_cookie("fruit", fruit)
    bottle.redirect('/show_fruit')

@bottle.route('/show_fruit')
def show_fruit():
    fruit = bottle.request.get_cookie("fruit")
    return bottle.template('fruit_selection.tpl', {'fruit': fruit})


bottle.debug(True)
bottle.run(host='localhost', port=8080)