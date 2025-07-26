# coding: utf-8
import requests
import pandas as pd
import datetime as dt
import json
url = "https://api.cnyes.com/media/api/v1/newslist/category/headline"#連結
payload ={
    "page":9,
    "limit":30,
    "isCategoryHeadline":1,
    "startAt":int((dt.datetime.today()- dt.timedelta(days = 11)).timestamp()),
    "endAt":int(dt.datetime.today().timestamp())   
} #參數
res = requests.get(url, params = payload) #連線鉅亨網
jd = json.loads(res.text) #解析JSON to 
df = pd.DataFrame(jd['items']['data'])
df = df [['newsId','title','summary']]
df['link'] = df['newsId'].apply(lambda x: 'https://m.cnyes.com/news/id/' + str(x))
#print(df)
df
df.to_csv('news.csv',encoding ='utf-8-sig')
