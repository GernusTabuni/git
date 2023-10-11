from pymongo import MongoClient

client = MongoClient('mongodb+srv://nusyoman:manis@cluster0.wjeaswn.mongodb.net/?retryWrites=true&w=majority')

db = client.dbsparta
url= 'https://www.bilibili.tv/id/anime'
doc = [
   {"#": "1","item":  "title", "One Piece: Gold": "12"},
   {"#": "2","item": "genre", "lazy": "13"},
   {"#": "3","item": "cover_link", "https://pic.bstarstatic.com/ogv/cc498a980f26cd699f82b63e8cbe463872378f6d.jpg@720w_405h_1e_1c_90q.webp": "13"}
]
db.Data.insert_many(doc)
