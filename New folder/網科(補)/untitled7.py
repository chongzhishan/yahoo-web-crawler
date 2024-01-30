# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 11:55:16 2021

@author: ASUS
"""
##此拿第一筆:死亡漩渦：奪魂鋸新遊戲http://www.atmovies
##.com.tw/movie/fsen10342730/來抓取內文、圖片、資料
content=[]
photos=[]
data=[]
from bs4 import BeautifulSoup
import requests
import requests
URL = "http://www.atmovies.com.tw/movie/fsen10342730/"##此連結可以拿資料的連結來
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
         "AppleWebKit/537.36 (KHTML, like Gecko)"
         "Chrome/63.0.3239.132 Safari/537集.36"}
r = requests.get(URL, headers=headers)
soup = BeautifulSoup(r.text, "lxml")
####################內文下載
orig=soup.find(id="filmTagBlock")
chan=orig.text
for ch in chan:
    if ch in '我要評分' :
        chan=chan.replace(ch,'')
    if ch in '\t' :
        chan=chan.replace(ch,'')
print(chan)
content.append(chan)
####################下載圖片
photo = orig.img['src']  
photos.append(photo)
print("圖片網址", photo,'\n')
picture = requests.get(photo)                      
img=picture .content
pic_out=open("movie.png","wb")
pic_out.write(img)
pic_out.close()
####################資料(電影出版時間等等)
dio=soup.find(id="filmCastDataBlock")
chan2=dio.text
for ch in chan2:
    if ch in '\xa0' :
        chan2=chan2.replace(ch,'')
    if ch in '\t' :
        chan2=chan2.replace(ch,'')
    if ch in '音　　效：' :
        chan2=chan2.replace(ch,'')
print(chan2)
data.append(chan2)
print(content)
print(photos)
print(data)

















  
