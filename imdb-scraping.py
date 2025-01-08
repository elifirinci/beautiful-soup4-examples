from bs4 import BeautifulSoup as bs
import requests
from parse import *

url="https://www.imdb.com/chart/top/"
client_req={"user-agent":" "}
req=requests.get(url,headers=client_req).content
#print(req)
soup=bs(req,"html.parser")
list=soup.find("ul",{"class":"ipc-metadata-list"}).find_all('li',limit=100)
print(list)

for item in list:
    movie_name=item.find("h3",{"class":"ipc-title__text"}).text
    movie_ratings=item.find("span",{"class":"ipc-rating-star"}).text
    print(movie_name,movie_ratings)
    
