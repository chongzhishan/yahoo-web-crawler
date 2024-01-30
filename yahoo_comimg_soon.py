from typing import ItemsView
import requests, bs4,os

for i in range(1,4):
    url_change =str(i)
    url_comingsoon_standard ='https://movies.yahoo.com.tw/movie_comingsoon.html?page='
    url_comingsoon_page = url_comingsoon_standard+url_change
    moviehtml_comingsoon = requests.get(url_comingsoon_page)
    objSoup_comingsoon_year = bs4.BeautifulSoup(moviehtml_comingsoon.text,'lxml')
    Items = objSoup_comingsoon_year.find_all('div','release_info')
    print("即將上映")
    for item in Items:
        cName = item.find('div','release_movie_name').a.text.strip()
        eName = item.find('div', 'en').a.text.strip()                   # 英文片名
        rTime = item.find('div', 'release_movie_time')
        level = item.find('div', 'leveltext').span.text.strip()
        txt = item.find('div', 'release_text').text.strip()
        photo = item.find_previous_sibling('div', 'release_foto').a.img['src']
        video = item.find('div','release_btn color_btnbox').find_all('a')[1]
        if 'href' in video.attrs:                               # 檢查預告片是否存在
            video = video['href']
        else:
            video = ''
        print("page",i)
        print('中文片名 : ', cName)
        print('英文片名 : ', eName)
        print(rTime.text)
        print('期待度   : ', level)
        print('內容摘要 : ', txt)
        print('海報網址 : ', photo)
        print('預告片   : ', video)
        print()
    photos = []                                             # 放置劇照串列
    items = objSoup_comingsoon_year.find_all('div', 'release_foto')
    for item in items:
        photo = item.a.img['src']                           # 取得劇照網址
        photos.append(photo)

    destDir = 'out9_6'
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
        pictFile.close()                                    # 關閉檔案