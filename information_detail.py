from typing import ItemsView
import requests, bs4,os
from bs4 import BeautifulSoup, NavigableString, Tag
from requests.api import get

url = 'https://movies.yahoo.com.tw/tagged/movieheadline'
url_1 = 'https://movies.yahoo.com.tw/tagged/spotlight'
url_2 = 'https://movies.yahoo.com.tw/tagged/moviereview'
url_3 = 'https://movies.yahoo.com.tw/tagged/moviespecial02'
url_4 = 'https://movies.yahoo.com.tw/tagged/moviespecial01'
movieheadline= requests.get(url)
spotlight = requests.get(url_1)
moviereview = requests.get(url_2)
moviespecial02 = requests.get(url_3)
moviespecial01 = requests.get(url_4)
objSoup = bs4.BeautifulSoup(movieheadline.text, 'lxml')
objSoup_1 = bs4.BeautifulSoup(spotlight.text,'lxml')
objSoup_2 = bs4.BeautifulSoup(moviereview.text,'lxml')
objSoup_3 = bs4.BeautifulSoup(moviespecial02.text,'lxml')
objSoup_4 = bs4.BeautifulSoup(moviespecial01.text,'lxml')


new_drama= objSoup.find_all('div','l_box_inner')
photos = [] 
print("電影新聞")
for item in new_drama:
    url = item.find_all('a')
    for i in url:
        title = i.find('h2')
        introduction = i.find('span')
        date = i.find('div','day')
        photo = i.img['src']
        photos.append(photo)
        print("文章標題:\n",title.text)
        print("介紹\n",introduction.text.lstrip().rstrip())
        print("日期",date.text)
        print("連結",i.get('href'))
        print("圖片網址", photo,'\n')
destDir = '電影新聞_細節'
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
yourPath = r'C:\Users\User\Desktop\新爬蟲\電影新聞_細節'
allFileList = os.listdir(yourPath)
for file in allFileList:
    jpg = '.jpg'
    new_file = file+jpg
    os.rename(os.path.join(yourPath, file), os.path.join(yourPath, new_file))
    pictFile.close()

new_movie= objSoup_1.find_all('div','l_box_inner')
photos = [] 
print("專題報導")
for item in new_movie:
    url = item.find_all('a')
    for i in url:
        title = i.find('h2')
        introduction = i.find('span')
        date = i.find('div','day')
        photo = i.img['src']
        photos.append(photo)
        print("文章標題:\n",title.text)
        print("介紹\n",introduction.text.lstrip().rstrip())
        print("日期",date.text)
        print("連結",i.get('href'))
        print("圖片網址", photo,'\n')

destDir = '專題報導_細項'
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
yourPath = r'C:\Users\User\Desktop\新爬蟲\專題報導_細項'
allFileList = os.listdir(yourPath)
for file in allFileList:
    jpg = '.jpg'
    new_file = file+jpg
    os.rename(os.path.join(yourPath, file), os.path.join(yourPath, new_file))
    pictFile.close()

new_movie= objSoup_2.find_all('div','l_box_inner')
photos = [] 
print("影評")
for item in new_movie:
    url = item.find_all('a')
    for i in url:
        title = i.find('h2')
        introduction = i.find('span')
        date = i.find('div','day')
        photo = i.img['src']
        photos.append(photo)
        print("文章標題:\n",title.text)
        print("介紹\n",introduction.text.lstrip().rstrip())
        print("日期",date.text)
        print("連結",i.get('href'))
        print("圖片網址", photo,'\n')

destDir = '影評_細項'
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
yourPath = r'C:\Users\User\Desktop\新爬蟲\影評_細項'
allFileList = os.listdir(yourPath)
for file in allFileList:
    jpg = '.jpg'
    new_file = file+jpg
    os.rename(os.path.join(yourPath, file), os.path.join(yourPath, new_file))
    pictFile.close()


new_movie= objSoup_3.find_all('div','l_box_inner')
photos = [] 
print("奧斯卡")
for item in new_movie:
    url = item.find_all('a')
    for i in url:
        title = i.find('h2')
        introduction = i.find('span')
        date = i.find('div','day')
        photo = i.img['src']
        photos.append(photo)
        print("文章標題:\n",title.text)
        print("介紹\n",introduction.text.lstrip().rstrip())
        print("日期",date.text)
        print("連結",i.get('href'))
        print("圖片網址", photo,'\n')

destDir = '奧斯卡'
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
yourPath = r'C:\Users\User\Desktop\新爬蟲\奧斯卡'
allFileList = os.listdir(yourPath)
for file in allFileList:
    jpg = '.jpg'
    new_file = file+jpg
    os.rename(os.path.join(yourPath, file), os.path.join(yourPath, new_file))
    pictFile.close()

new_movie= objSoup_3.find_all('div','l_box_inner')
photos = [] 
print("金馬奇幻影展")
for item in new_movie:
    url = item.find_all('a')
    for i in url:
        title = i.find('h2')
        introduction = i.find('span')
        date = i.find('div','day')
        photo = i.img['src']
        photos.append(photo)
        print("文章標題:\n",title.text)
        print("介紹\n",introduction.text.lstrip().rstrip())
        print("日期",date.text)
        print("連結",i.get('href'))
        print("圖片網址", photo,'\n')

destDir = '金馬奇幻影展'
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
yourPath = r'C:\Users\User\Desktop\新爬蟲\金馬奇幻影展'
allFileList = os.listdir(yourPath)
for file in allFileList:
    jpg = '.jpg'
    new_file = file+jpg
    os.rename(os.path.join(yourPath, file), os.path.join(yourPath, new_file))
    pictFile.close()