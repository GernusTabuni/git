from pymongo import MongoClient

client = MongoClient('mongodb+srv://nusyoman:manis@cluster0.wjeaswn.mongodb.net/?retryWrites=true&w=majority')

db = client.dbsparta(__doc__)

import requests
from bs4 import BeautifulSoup
import certifi

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

cert = certifi.where()

url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
data = requests.get(url=url, headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

movies = soup.select('.lister > table > tbody > tr')


for movie in movies:
   
    movie_title = movie.select_one('.titleColumn > a').text
    year = movie.select_one ('.titleColum > .secondari').text
    year = year.replace ('(', '')
    year = year.replace(')','')
    rating = movie.select_one('.ratingColumn > strong'). text
    print(movie_title,'/', year, '/',rating)

    

db.Data.insert_many(__doc__)


