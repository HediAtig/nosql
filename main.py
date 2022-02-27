
import pymongo as pymongo
from bson import ObjectId

client = pymongo.MongoClient(
    "mongodb+srv://hedi:110998ImeneHedi!@cluster0.hdyyx.mongodb.net/test?retryWrites=true&w=majority")
db = client.test
continents = db.continents
countries = db.countries



def print_hi(name):

    print(f'Hi, {name}')


def connectdb():

    client = pymongo.MongoClient("mongodb+srv://hedi:110998ImeneHedi!@cluster0.hdyyx.mongodb.net/test?retryWrites=true&w=majority")
    db = client.test
    print(db.list_collection_names())


def search1():
    var = input("enter the word to search")
    s = countries.find({"name": {"$regex": str(var)}})

    for x in s:
        print(x)


def list_continents():
    connectdb()
    for continent in continents.find():
         print(continent['name'], ':',len(continent['countries']))


def display_fourth_counties():
    l=list()
    for continent in continents.find():
     s=continent['countries'][2]
     for country in countries.find():
       if country['_id']==s:
          s=country['name']
          l.append(s)
    l.sort()
    print(l)

def add_att_pop():
    myquery = {{"_id":ObjectId()}, {'$set':{"population":0}}}
    s=countries.updateMany(myquery)
    for x in s:
        print(x)


def search2():

    s = countries.find({"name": {"$regex": ".u"}, "population": { "$gt": "100000" } })
    for x in s:
        print(x)


def sort_pop():

    s = countries.find().sort('population')

    for x in s:
        print(x)


def display_counties():
    for continent in continents.find():
        for country in countries.find():
            if (country['continent'] == continent['_id']):
                country['continent'] = continent['name']
                print(country)


def sort_alf():

    tri=countries.find().sort('name')

    for country in tri:
        print(country['name'])









if __name__ == '__main__':
    print_hi('PyCharm')
    connectdb()
    search1()
    list_continents()
    display_fourth_counties()
    #add_att_pop()
    search2()
    print("")
    sort_pop()
    #display_counties()
    #sort_alf()
