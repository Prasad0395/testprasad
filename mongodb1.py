import pymongo


client = pymongo.MongoClient("mongodb+srv://admin:durga2929@cluster0.cvhp5tp.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d = {
    "name" : "prasad",
    "email" : "ggiufghoi@giui",
    "surname" : "taageti"
}

db1 = client['mongodb']
coll = db1['test']
coll.insert_one(d)

