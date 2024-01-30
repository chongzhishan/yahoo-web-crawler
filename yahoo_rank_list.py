from typing import ItemsView
import requests, bs4,os
url ='https://movies.yahoo.com.tw/chart.html'
url_us = 'https://movies.yahoo.com.tw/chart.html?cate=us'
url_week = 'https://movies.yahoo.com.tw/chart.html?cate=week'
url_year = 'https://movies.yahoo.com.tw/chart.html?cate=year'
url_30 = 'https://movies.yahoo.com.tw/chart.html?cate=exp_30&search_date=30'
url_365 = 'https://movies.yahoo.com.tw/chart.html?cate=exp_30&search_date=365'
url_satisfy30 = 'https://movies.yahoo.com.tw/chart.html?cate=rating&search_year=30'
moviehtml = requests.get(url)
moviehtml_us = requests.get(url_us)
moviehtml_week =  requests.get(url_week)
moviehtml_year = requests.get(url_year)
moviehtml_30 = requests.get(url_30)
moviehtml_365 = requests.get(url_365)
moviehtml_satisfy30 = requests.get(url_satisfy30)
objSoup = bs4.BeautifulSoup(moviehtml.text, 'lxml')
objSoup_us = bs4.BeautifulSoup(moviehtml_us.text, 'lxml')
objSoup_week = bs4.BeautifulSoup(moviehtml_week.text,'lxml')
objSoup_year = bs4.BeautifulSoup(moviehtml_year.text,'lxml')
objSoup_30 = bs4.BeautifulSoup(moviehtml_30.text,'lxml')
objSoup_365 = bs4.BeautifulSoup(moviehtml_365.text,'lxml')
objSoup_satisfy30 = bs4.BeautifulSoup(moviehtml_satisfy30.text,'lxml')


info_obj =  objSoup.find_all('div','tr')
print("台北排行榜")
for item in info_obj:
     Name = item.find_all('div','rank_txt')
     Rank_newnum = item.find_all('div','td')[0]
     Rank_newnum = Rank_newnum.text
     Rank_updown= item.find_all('div','td')[1].get('class')
     Rank_oldnum = item.find_all('div','td')[2]
     Rank_oldnum = Rank_oldnum.text
     link = item.find_all('div','td')[3]
     upload_date = item.find_all('div','td')[4].text
     tralier_url = item.find_all('div','td')[5]
     rate = item.find_all('div','td starwithnum')
     for item in Name:
         if Name == []:
             pass
         else:
             Name = item.text
             print(Name)
     if Rank_newnum == '本週':
         pass
     else:
          print("本週排名",Rank_newnum)
     if Rank_oldnum == '上週':
         pass
     elif Rank_oldnum == '':
         print("上週 未進榜")
     else:
          print("上週排名",Rank_oldnum)
     if Rank_updown == ['td','updown'] or '上週排名':
         pass
     elif Rank_updown == ['td','new']:
         print("新進榜")
     elif Rank_updown == ['td','down']:
         print("排名下降") 
     else:
         print("排名升高")
     R1 = item.find('dd')
     if R1 == None:
         pass
     else:
         R2 = item.find('h2')
         eName = item.find('h3')
         introduction = item.find('dd').span.text.strip()
         print("中文名子",R2.text)
         print("英文名字",eName.text)
         print("介紹",introduction)
     for item in link.find_all('a'):
         print("連結",item.get('href'))
     if upload_date == '上映日期':
         pass
     else:
         print("上映日期",upload_date)
     for item in tralier_url.find_all('a'):
         print("預告片網址",item.get('href'))
     for item in rate:
         rate = item.find('h6')
         if rate == None:
             pass
         else :
             rate = item.find('h6').get('data-num')
             print("評價 = ",rate,'\n')

info_obj_us =  objSoup_us.find_all('div','tr')
print("全美排行榜")
for item in info_obj_us:
     Name = item.find_all('div','rank_txt')
     Rank_newnum = item.find_all('div','td')[0]
     Rank_newnum = Rank_newnum.text
     Rank_updown= item.find_all('div','td')[1].get('class')
     Rank_oldnum = item.find_all('div','td')[2]
     Rank_oldnum = Rank_oldnum.text
     link = item.find_all('div','td')[3]
     upload_date = item.find_all('div','td')[4].text
     tralier_url = item.find_all('div','td')[5]
     rate = item.find_all('div','td starwithnum')
     for item in Name:
         if Name == []:
             pass
         else:
             Name = item.text
             print(Name)
     if Rank_newnum == '本週':
         pass
     else:
          print("本週排名",Rank_newnum)
     if Rank_oldnum == '上週':
         pass
     elif Rank_oldnum == '':
         print("上週 未進榜")
     else:
          print("上週排名",Rank_oldnum)
     if Rank_updown == ['td','updown'] or '上週排名':
         pass
     elif Rank_updown == ['td','new']:
         print("新進榜")
     elif Rank_updown == ['td','down']:
         print("排名下降") 
     else:
         print("排名升高")     
     R1 = item.find('dd')
     if R1 == None:
         pass
     else:
         R2 = item.find('h2')
         eName = item.find('h3')
         introduction = item.find('dd').span.text.strip()
         print("中文名子",R2.text)
         print("英文名字",eName.text)
         print("介紹",introduction)
     for item in link.find_all('a'):
         print("連結",item.get('href'))
     if upload_date == '上映日期':
         pass
     else:
         print("上映日期",upload_date)     
     for item in tralier_url.find_all('a'):
         print("預告片網址",item.get('href'))
     for item in rate:
         rate = item.find('h6')
         if rate == None:
             pass
         else :
             rate = item.find('h6').get('data-num')
             print("評價 = ",rate,'\n')

info_obj_week = objSoup_week.find_all('div','tr')
print("\n週冠軍票房列表")
for item in info_obj_week:
     Name = item.find_all('div','rank_txt')
     week = item.find_all('div','td')[0].text
     link = item.find_all('div','td')[1]
     count = item.find_all('div','td')[2].text
     tralier_url = item.find_all('div','td')[3]
     rate = item.find_all('div','td starwithnum')
     for item in Name:
         if Name == []:
             pass
         else:
             Name = item.text
             print(Name)
     if week == '週次':
         pass
     else:
         print("第幾週",week)
     for item in link.find_all('a'):
         print("連結",item.get('href'))
     if count == '統計時間':
         pass
     else:
         print("統計時間 = ",count)
     for item in tralier_url.find_all('a'):
         print("預告片連結 ",item.get('href'))
     for item in rate:
         rate = item.find('h6')
         if rate == None:
             pass
         else :
             rate = item.find('h6').get('data-num')
             print("評價 = ",rate,'\n')

info_obj_year = objSoup_year.find_all('div','tr')
print("年度票房榜")
for item in info_obj_year:
     Name = item.find_all('div','rank_txt')
     Rank_newnum = item.find_all('div','td')[0]
     Rank_newnum = Rank_newnum.text
     Rank_updown= item.find_all('div','td')[1].get('class')
     Rank_oldnum = item.find_all('div','td')[2]
     Rank_oldnum = Rank_oldnum.text
     link = item.find_all('div','td')[3]
     upload_date = item.find_all('div','td')[4].text
     tralier_url = item.find_all('div','td')[5]
     rate = item.find_all('div','td starwithnum')
     for item in Name:
         if Name == []:
             pass
         else:
             Name = item.text
             print(Name)
     if Rank_newnum == '本週':
         pass
     else:
          print("本週排名",Rank_newnum)
     if Rank_oldnum == '上週':
         pass
     elif Rank_oldnum == '':
         print("上週 未進榜")
     else:
          print("上週排名",Rank_oldnum)
     if Rank_updown == ['td','updown'] or '上週排名':
         pass
     elif Rank_updown == ['td','new']:
         print("新進榜")
     elif Rank_updown == ['td','down']:
         print("排名下降") 
     else:
         print("排名升高")     
     R1 = item.find('dd')
     if R1 == None:
         pass
     else:
         R2 = item.find('h2')
         eName = item.find('h3')
         introduction = item.find('dd').span.text.strip()
         print("中文名子",R2.text)
         print("英文名字",eName.text)
         print("介紹",introduction)
     for item in link.find_all('a'):
         print("連結",item.get('href'))
     if upload_date == '上映日期':
         pass
     else:
         print("上映日期",upload_date)     
     for item in tralier_url.find_all('a'):
         print("預告片網址",item.get('href'))
     for item in rate:
         rate = item.find('h6')
         if rate == None:
             pass
         else :
             rate = item.find('h6').get('data-num')
             print("評價 = ",rate,'\n')

info_obj_30 = objSoup_30.find_all('div','tr')
print("30天內上映電影網友期待榜")
for item in info_obj_30:
    Name = item.find_all('div','rank_txt')
    Rank_num = item.find_all('div','td')[0].text
    link = item.find_all('div','td')[1]
    upload_date = item.find_all('div','td')[2].text
    tralier_url = item.find_all('div','td')[3]
    wait_people = item.find_all('div','td')[4]
    wait_people_num = wait_people.find('h6')
    wait_people_ch = wait_people.find('h5')
    wait_people_vote = wait_people.find('h4')
    for item in Name:
         if Name == []:
             pass
         else:
             Name = item.text
             print(Name)
    R1 = item.find('dd')
    if R1 == None:
         pass
    else:
         R2 = item.find('h2')
         eName = item.find('h3')
         print("中文名字",R2.text)
         print("英文名字",eName.text)
    if Rank_num == '排名':
         pass
    else:
          print("30天內排名",Rank_num)
    for item in link.find_all('a'):
         print("連結",item.get('href'))
    if upload_date == '上映日期':
         pass
    else:
         print("上映日期",upload_date)
    for item in tralier_url.find_all('a'):
         print("預告片網址",item.get('href'))
    if wait_people_num == None:
        pass
    else:
        if wait_people_ch == None:
            pass
        else:
            if wait_people_vote == None:
                pass
            else:
                print(wait_people_num.text,wait_people_ch.text,",",wait_people_vote.text,"\n")

info_obj_365 = objSoup_365.find_all('div','tr')
for item in info_obj_365:
    Name = item.find_all('div','rank_txt')
    Rank_num = item.find_all('div','td')[0].text
    link = item.find_all('div','td')[1]
    upload_date = item.find_all('div','td')[2].text
    tralier_url = item.find_all('div','td')[3]
    wait_people = item.find_all('div','td')[4]
    wait_people_num = wait_people.find('h6')
    wait_people_ch = wait_people.find('h5')
    wait_people_vote = wait_people.find('h4')
    for item in Name:
         if Name == []:
             pass
         else:
             Name = item.text
             print(Name)
    R1 = item.find('dd')
    if R1 == None:
         pass
    else:
         R2 = item.find('h2')
         eName = item.find('h3')
         print("中文名字",R2.text)
         print("英文名字",eName.text)
    if Rank_num == '排名':
         pass
    else:
          print("排名",Rank_num)
    for item in link.find_all('a'):
         print("連結",item.get('href'))
    if upload_date == '上映日期':
         pass
    else:
         print("上映日期",upload_date)
    for item in tralier_url.find_all('a'):
         print("預告片網址",item.get('href'))
    if wait_people_num == None:
        pass
    else:
        if wait_people_ch == None:
            pass
        else:
            if wait_people_vote == None:
                pass
            else:
                print(wait_people_num.text,wait_people_ch.text,",",wait_people_vote.text,"\n")

info_obj_satisfy = objSoup_satisfy30.find_all('div','tr')
for item in info_obj_satisfy:
    Name = item.find_all('div','rank_txt')
    Rank_num = item.find_all('div','td')[0].text
    link = item.find_all('div','td')[1]
    upload_date = item.find_all('div','td')[2].text
    tralier_url = item.find_all('div','td')[3]
    rate = item.find_all('div','td starwithnum')
    for item in Name:
         if Name == []:
             pass
         else:
             Name = item.text
             print(Name)
    R1 = item.find('dd')
    if R1 == None:
         pass
    else:
         R2 = item.find('h2')
         eName = item.find('h3')
         print("中文名字",R2.text)
         print("英文名字",eName.text)
    if Rank_num == '排名':
         pass
    else:
          print("排名",Rank_num)
    for item in link.find_all('a'):
         print("連結",item.get('href'))
    if upload_date == '上映日期':
         pass
    else:
         print("上映日期",upload_date)
    for item in tralier_url.find_all('a'):
         print("預告片網址",item.get('href'))
    for item in rate:
         rate = item.find('h6')
         if rate == None:
             pass
         else :
             rate = item.find('h6').get('data-num')
             print("評價 = ",rate,'\n')         


for i in range(2021,2008,-1):
    url_change =str(i)
    url_satisfy_standard ='https://movies.yahoo.com.tw/chart.html?cate=rating&search_year='
    url_satisfy_year = url_satisfy_standard+url_change
    moviehtml_satisfy = requests.get(url_satisfy_year)
    objSoup_satisfy_year = bs4.BeautifulSoup(moviehtml_satisfy.text,'lxml')
    info_obj_satisfy_year = objSoup_satisfy_year.find_all('div','tr')
    movieNum = 0
    for item in info_obj_satisfy_year:
        Name = item.find_all('div','rank_txt')
        Rank_num = item.find_all('div','td')[0].text
        link = item.find_all('div','td')[1]
        upload_date = item.find_all('div','td')[2].text
        tralier_url = item.find_all('div','td')[3]
        rate = item.find_all('div','td starwithnum')
        for item in Name:
            if Name == []:
                pass
            else:
                Name = item.text
                print(Name)
        R1 = item.find('dd')
        if R1 == None:
            pass
        else:
            R2 = item.find('h2')
            eName = item.find('h3')
            print("中文名字",R2.text)
            print("英文名字",eName.text)
        if Rank_num == '排名':
            pass
        else:
            print("排名",Rank_num)
        for item in link.find_all('a'):
            print("連結",item.get('href'))
        if upload_date == '上映日期':
            pass
        else:
            print("上映日期",upload_date)
        for item in tralier_url.find_all('a'):
            print("預告片網址",item.get('href'))
        for item in rate:
            rate = item.find('h6')
            if rate == None:
                pass
            else :
                rate = item.find('h6').get('data-num')
                print("評價 = ",rate,'\n')