from bs4 import BeautifulSoup as bs 
import requests
from parse import *
import time
import random
for i in range(1,10):
    adres=f'https://www.lcw.com/kadin-tisort-t-348?sayfa={i}'
    baslik={'user-agent':''}
    sayfa=requests.get(adres,headers=baslik)
    soup=bs(sayfa.content,features='lxml')
    kadın=soup.find_all('img',{'class':'product-image__image'})
    time.sleep(random.randint(3,8))
     for foto in kadın:
         print(foto)


