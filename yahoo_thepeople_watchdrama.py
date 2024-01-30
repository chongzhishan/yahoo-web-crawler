from typing import ItemsView
import requests, bs4,os
from bs4 import BeautifulSoup, NavigableString, Tag
from requests.api import get

url = 'https://movies.yahoo.com.tw/ott_index.html'
watchdrama= requests.get(url)
objSoup = bs4.BeautifulSoup(watchdrama.text, 'lxml')

photos = []
new_drama= objSoup.find_all('div','title')[3]
for item in new_drama:
    if isinstance(item, NavigableString):
        continue
    if isinstance(item, Tag):
        print(item.text.lstrip())
new_drama = objSoup.find_all('ul','featured_img informpage')[0]
for item in new_drama:
    if isinstance(item,NavigableString):
        continue
    if isinstance(item,Tag):
        title = item.find('div','text_truncate_2')
        date = item.find('span')
        photo = item.img['src']
        print("文章標題:\n",title.text.lstrip())
        print("日期",date.text,"\n")
        for item in item.find_all('a'):
            print("連結",item.get('href'))
        photos.append(photo)
        print('圖片網址',photo,"\n")
see_more = objSoup.find_all('div','btn_plus_more')[3]               # 列出搜尋到的圖片數量
for i in see_more:
    if isinstance(i, NavigableString):
        continue
    if isinstance(i, Tag):
        print(i.text.lstrip())
        url = i.get('href')
        print("網址",url,"\n")

destDir = '最新線上戲劇_追劇咖'
if os.path.exists(destDir) == False:                    # 如果沒有此資料夾就建立
    os.mkdir(destDir) 
print("搜尋到的圖片數量 = ", len(photos))               # 列出搜尋到的圖片數量
for photo in photos:                                    # 迴圈下載圖片與儲存
    picture = requests.get(photo)                       # 下載圖片
    picture.raise_for_status()                          # 驗證圖片是否下載成功
    print("%s 圖片下載成功\n" % photo)
# 先開啟檔案, 再儲存圖片
    pictFile = open(os.path.join(destDir, os.path.basename(photo)), 'wb')
    for diskStorage in picture.iter_content(10240):
        pictFile.write(diskStorage)
    pictFile.close()
yourPath = r'C:\Users\User\Desktop\新爬蟲\最新線上戲劇_追劇咖'
allFileList = os.listdir(yourPath)
for file in allFileList:
    jpg = '.jpg'
    new_file = file+jpg
    os.rename(os.path.join(yourPath, file), os.path.join(yourPath, new_file))
    pictFile.close()

photos = []
new_drama= objSoup.find_all('div','title')[4]
for item in new_drama:
    if isinstance(item, NavigableString):
        continue
    if isinstance(item, Tag):
        print(item.text.lstrip())
new_drama = objSoup.find_all('ul','featured_img informpage')[1]
for item in new_drama:
    if isinstance(item,NavigableString):
        continue
    if isinstance(item,Tag):
        title = item.find('div','text_truncate_2')
        date = item.find('span')
        photo = item.img['src']
        print("文章標題:\n",title.text.lstrip())
        print("日期",date.text,"\n")
        for item in item.find_all('a'):
            print("連結",item.get('href'))
        photos.append(photo)
        print('圖片網址',photo,"\n")
see_more = objSoup.find_all('div','btn_plus_more')[4]               # 列出搜尋到的圖片數量
for i in see_more:
    if isinstance(i, NavigableString):
        continue
    if isinstance(i, Tag):
        print(i.text.lstrip())
        url = i.get('href')
        print("網址",url,"\n")

destDir = '最新線上電影_追劇咖'
if os.path.exists(destDir) == False:                    # 如果沒有此資料夾就建立
    os.mkdir(destDir) 
print("搜尋到的圖片數量 = ", len(photos))               # 列出搜尋到的圖片數量
for photo in photos:                                    # 迴圈下載圖片與儲存
    picture = requests.get(photo)                       # 下載圖片
    picture.raise_for_status()                          # 驗證圖片是否下載成功
    print("%s 圖片下載成功\n" % photo)
# 先開啟檔案, 再儲存圖片
    pictFile = open(os.path.join(destDir, os.path.basename(photo)), 'wb')
    for diskStorage in picture.iter_content(10240):
        pictFile.write(diskStorage)
    pictFile.close()
yourPath = r'C:\Users\User\Desktop\新爬蟲\最新線上電影_追劇咖'
allFileList = os.listdir(yourPath)
for file in allFileList:
    jpg = '.jpg'
    new_file = file+jpg
    os.rename(os.path.join(yourPath, file), os.path.join(yourPath, new_file))
    pictFile.close()


photos = []
new_drama= objSoup.find_all('div','title')[5]
for item in new_drama:
    if isinstance(item, NavigableString):
        continue
    if isinstance(item, Tag):
        print(item.text.lstrip())
new_drama = objSoup.find_all('ul','featured_img informpage')[2]
for item in new_drama:
    if isinstance(item,NavigableString):
        continue
    if isinstance(item,Tag):
        title = item.find('div','text_truncate_2')
        date = item.find('span')
        photo = item.img['src']
        print("文章標題:\n",title.text.lstrip())
        print("日期",date.text,"\n")
        for item in item.find_all('a'):
            print("連結",item.get('href'))
        photos.append(photo)
        print('圖片網址',photo,"\n")
see_more = objSoup.find_all('div','btn_plus_more')[5]               # 列出搜尋到的圖片數量
for i in see_more:
    if isinstance(i, NavigableString):
        continue
    if isinstance(i, Tag):
        print(i.text.lstrip())
        url = i.get('href')
        print("網址",url,"\n")

destDir = '預告與解析_追劇咖'
if os.path.exists(destDir) == False:                    # 如果沒有此資料夾就建立
    os.mkdir(destDir) 
print("搜尋到的圖片數量 = ", len(photos))               # 列出搜尋到的圖片數量
for photo in photos:                                    # 迴圈下載圖片與儲存
    picture = requests.get(photo)                       # 下載圖片
    picture.raise_for_status()                          # 驗證圖片是否下載成功
    print("%s 圖片下載成功\n" % photo)
# 先開啟檔案, 再儲存圖片
    pictFile = open(os.path.join(destDir, os.path.basename(photo)), 'wb')
    for diskStorage in picture.iter_content(10240):
        pictFile.write(diskStorage)
    pictFile.close()
yourPath = r'C:\Users\User\Desktop\新爬蟲\預告與解析_追劇咖'
allFileList = os.listdir(yourPath)
for file in allFileList:
    jpg = '.jpg'
    new_file = file+jpg
    os.rename(os.path.join(yourPath, file), os.path.join(yourPath, new_file))
    pictFile.close()