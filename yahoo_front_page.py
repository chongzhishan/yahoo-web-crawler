from typing import ItemsView
import requests, bs4,os
from bs4 import BeautifulSoup, NavigableString, Tag

from requests.api import get
url = 'https://movies.yahoo.com.tw/'
moviefrontpage = requests.get(url)
objSoup = bs4.BeautifulSoup(moviefrontpage.text, 'lxml')

Items = objSoup.find_all('div','_slickcontent')
print(Items)
print("最新電影")
for item in Items:
    Name = item.find('div','movielist_info')
    tralier_url = item.find('div','movielist_btn color_btnbox')
    video = []
    if Name == None:
        pass
    else:
        upload_date = Name.find('h3')
        rate = Name.find('div','percent').span.text
        print(Name.a.text.strip())
        print("上映日期",upload_date.text)
        print(rate)
        for item in Name.find_all('a'):
            print("電影介紹連結",item.get('href'))
    if tralier_url == None:
        pass
    else:
        for item in tralier_url.find_all('a'):
            video =item.get('href')
            if video == 'javascript:void(0)':
                pass
            else:
                print("預告片連結",video,'\n')
photos = []                                             # 放置劇照串列
items = objSoup.find_all('div', 'movie_foto')
for item in items:
    photo = item.img['src']                           # 取得劇照網址
    photos.append(photo)

destDir = '最新電影'
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

print("編輯推薦")
edit =   objSoup.find_all('div','edit_choice')
photos = []
for item in edit:
    text = item.find('div','edit_txt').text
    url = item.find('a')
    article = url.get('href')
    photo = item.img['src']
    photos.append(photo)
    print(text)
    print("照片",photo)
    print("文章網址",article)

destDir = '編輯推薦'
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

print("最新預告片")
photos = []
newest_tralier = objSoup.find_all('div','l_box_inner')
for item in newest_tralier:
    url = item.find_all('ul','trailer_list _slickhelf')
    for item in url:
        url = item.find_all('a')
        for item in url:
            title = item.find('h2')
            date = item.find_all('span')
            url = item.get('href')
            photo = item.img['src']
            print("標題",title.text)
            for item in date:
                print("副標",item.text)
            print("預告片連結",url)
            print("照片", photo,"\n")
            photos.append(photo)
                                          

destDir = '最新預告片'
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

print("網友期待榜/網友滿意榜")
expect_rank = objSoup.find('dl','web_friends_box')
for item in expect_rank:
    li = item.find('ul')
    if li == -1:
        pass
    else:
        url = item.find_all('a')
        for item in url:
            title = item.find_all('div','list_info')
            rate = item.find_all('div',"circlenum")
            for name in title:
                name = name.find('h2')
                date = item.find_all('span')[0]
                print("片名",name.text)
                print(date.text)
            url = item.get('href')
            if url == 'https://movies.yahoo.com.tw/chart.html?cate=exp_30':
                pass
            else:
                print("預告片連結",url)
            if rate == []:
                pass
            else:
                for item in rate:
                    rate = item.find_all('span')
                    for item in rate:
                        print("期待",item.text,"%\n")
see_more = objSoup.find_all('div','btn_plus_more')[4]
for i in see_more:
    if isinstance(i, NavigableString):
        continue
    if isinstance(i, Tag):
        print(i.text.lstrip())
        url = i.get('href')
        print("網址",url,"\n")

photos = []                                             # 放置劇照串列
items = objSoup.find_all('div', 'web_friends_foto')
for item in items:
    photo = item.img['src']                           # 取得劇照網址
    photos.append(photo)

destDir = '網友期待榜'
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


information_post = objSoup.find_all('div','title')[4]
for item in information_post:
    if isinstance(item, NavigableString):
        continue
    if isinstance(item, Tag):
        print(item.text.lstrip())

information_post_1 = objSoup.find_all('ul','news_list infolist')
for i in range(0,5):
    for item in information_post_1:
        print("第",i+1,"則")
        list = item.find_all('li')
        list = list[i]
        title = list.find('h2')
        introduction = list.find('span')
        date = list.find('div','day')
        photo = list.img['src']
        print(title.text)
        print(introduction.text.lstrip())
        print("日期",date.text,"\n")
        for item in list.find_all('a'):
            print("連結",item.get('href'),"\n")
        print('圖片網址',photo,"\n")
photos = []                                             # 放置劇照串列
items = objSoup.find_all('div', 'fotoinner')
for item in items:
    photo = item.img['src']
    photos.append(photo)

destDir = '最新文章'
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
yourPath = r'C:\Users\User\Desktop\新爬蟲\最新文章'
allFileList = os.listdir(yourPath)
for file in allFileList:
    jpg = '.jpg'
    new_file = file+jpg
    os.rename(os.path.join(yourPath, file), os.path.join(yourPath, new_file))

see_more = objSoup.find_all('div','btn_plus_more')[5]
for i in see_more:
    if isinstance(i, NavigableString):
        continue
    if isinstance(i, Tag):
        print(i.text.lstrip())
        url = i.get('href')
        print("網址",url,"\n")

information_post = objSoup.find_all('div','title')[5]
for item in information_post:
    if isinstance(item, NavigableString):
        continue
    if isinstance(item, Tag):
        print(item.text.lstrip())

photos = []
new_drama = objSoup.find_all('ul','featured_img _slickthreeEdit')[0]
for item in new_drama.find_all('li'):
    if isinstance(item,NavigableString):
        continue
    if isinstance(item,Tag):
        title = item.find('div','text_truncate_2')
        introduction = item.find('div','jq_text_overflow_80 jq_text_overflow_link')
        date = item.find('span')
        photo = item.img['src']
        photos.append(photo)
        print(title.text.lstrip())
        print(introduction.text.lstrip())
        print("日期",date.text,"\n")
        for item in item.find_all('a'):
            print("連結",item.get('href'),"\n")
        print('圖片網址',photo,"\n")                                            
    
destDir = '最新線上戲劇'
if os.path.exists(destDir) == False:                    # 如果沒有此資料夾就建立
    os.mkdir(destDir) 
print("搜尋到的圖片數量 = ", len(photos))
see_more = objSoup.find_all('div','btn_plus_more')[6]               # 列出搜尋到的圖片數量
for i in see_more:
    if isinstance(i, NavigableString):
        continue
    if isinstance(i, Tag):
        print(i.text.lstrip())
        url = i.get('href')
        print("網址",url,"\n")
for photo in photos:                                    # 迴圈下載圖片與儲存
    picture = requests.get(photo)                       # 下載圖片
    picture.raise_for_status()                          # 驗證圖片是否下載成功
    print("%s 圖片下載成功\n" % photo)
# 先開啟檔案, 再儲存圖片
    pictFile = open(os.path.join(destDir, os.path.basename(photo)), 'wb')
    for diskStorage in picture.iter_content(10240):
        pictFile.write(diskStorage)
    pictFile.close()
yourPath = r'C:\Users\User\Desktop\新爬蟲\最新線上戲劇'
allFileList = os.listdir(yourPath)
for file in allFileList:
    jpg = '.jpg'
    new_file = file+jpg
    os.rename(os.path.join(yourPath, file), os.path.join(yourPath, new_file))
    pictFile.close()


new_movie= objSoup.find_all('div','title')[6]
for item in new_movie:
    if isinstance(item, NavigableString):
        continue
    if isinstance(item, Tag):
        print(item.text.lstrip())

photos = []
new_movie = objSoup.find_all('ul','featured_img _slickthreeEdit')[1]
for item in new_movie.find_all('li'):
    if isinstance(item,NavigableString):
        continue
    if isinstance(item,Tag):
        title = item.find('div','text_truncate_2')
        introduction = item.find('div','jq_text_overflow_80 jq_text_overflow_link')
        date = item.find('span')
        photo = item.img['src']
        photos.append(photo)
        print(title.text.lstrip())
        print(introduction.text.lstrip())
        print("日期",date.text,"\n")
        for item in item.find_all('a'):
            print("連結",item.get('href'),"\n")
        print('圖片網址',photo,"\n")
see_more = objSoup.find_all('div','btn_plus_more')[7]               # 列出搜尋到的圖片數量
for i in see_more:
    if isinstance(i, NavigableString):
        continue
    if isinstance(i, Tag):
        print(i.text.lstrip())
        url = i.get('href')
        print("網址",url,"\n")                                            
    
destDir = '最新線上電影'
if os.path.exists(destDir) == False:                    # 如果沒有此資料夾就建立
    os.mkdir(destDir) 
print("搜尋到的圖片數量 = ", len(photos))
for photo in photos:                                    # 迴圈下載圖片與儲存
    picture = requests.get(photo)                       # 下載圖片
    picture.raise_for_status()                          # 驗證圖片是否下載成功
    print("%s 圖片下載成功\n" % photo)
# 先開啟檔案, 再儲存圖片
    pictFile = open(os.path.join(destDir, os.path.basename(photo)), 'wb')
    for diskStorage in picture.iter_content(10240):
        pictFile.write(diskStorage)
    pictFile.close()
yourPath = r'C:\Users\User\Desktop\新爬蟲\最新線上電影'
allFileList = os.listdir(yourPath)
for file in allFileList:
    jpg = '.jpg'
    new_file = file+jpg
    os.rename(os.path.join(yourPath, file), os.path.join(yourPath, new_file))
    pictFile.close()
