#from pymongo import MongoClient
#client = MongoClient('mongodb+srv://nusyoman:manis@cluster0.wjeaswn.mongodb.net/?retryWrites=true&w=majority')
#db = client.dbsparta 

#target_movie = db.movies.find_one({'movie': 'The Matrix'})
#print(target_movie['rating'])


#target_rating = target_movie['rating']

#from pymongo import MongoClient
#client = MongoClient('mongodb+srv://nusyoman:manis@cluster0.wjeaswn.mongodb.net/?retryWrites=true&w=majority')
#db = client.dbsparta


#target_movie = db.movies.find_one({'movie': 'The Matrix'})
#target_rating = target_movie['rating']

#movies = list(db.movies.find({'rating': target_rating}))

#for movie in movies:
   # print(movie['movie'])

from pymongo import MongoClient
client = MongoClient('mongodb+srv://nusyoman:manis@cluster0.wjeaswn.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta
 
url= 

db.movies.update_one(
    {'movie': 'The Matrix'},
    {'$set': {'rating': '0'}}
)