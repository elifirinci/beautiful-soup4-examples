from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

url="https://www.teknosa.com/arama/?s=116004%2B116006001"
my_req={"user-agent":""}
req=requests.get(url,headers=my_req).content
soup=bs(req,"html.parser")
prices=soup.find_all("div",{"class":"prd-prices"})
names=soup.find_all("h3",{"class":"prd-title"})
for name, price in zip(names, prices):
    bilgi = {name.text.strip(): price.text.strip()}
    print(bilgi)

for name, price in zip(names, prices):
    name=[name.text.strip()]
    price=[price.text.strip()]
    bilgi=dict(names=name,prices=price)
    df=pd.DataFrame(bilgi)
    print(df)
    
print("************************************\n")
data = []

for name, price in zip(names, prices):
    bilgi = {'Name': name.text.strip(), 'Price': price.text.strip()}
    data.append(bilgi)

df = pd.DataFrame(data)
print(df)

