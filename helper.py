import requests
import json
import pandas as pd

responce=requests.get("https://s3.amazonaws.com/open-to-cors/assignment.json")
responce_json=json.loads(responce.text)

products=responce_json["products"]

product_id=[]
subcategory=[]
title=[]
price=[]
popularity=[]

for pdt in products:
    product_id.append(pdt)
    subcategory.append(products[pdt]["subcategory"])
    title.append(products[pdt]["title"])
    price.append(products[pdt]["price"])
    popularity.append(products[pdt]["popularity"])

data = {
    'product_id': product_id,
    'subcategory': subcategory,
    'title': title,
    'price': price,
    'popularity': popularity
}

df=pd.DataFrame(data)
df.set_index('product_id',inplace=True)
print(df.head())
