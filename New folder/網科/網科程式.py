title_arr1 = []
title_href1 = []
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
browser = webdriver.Chrome('chromedriver',options=options)
url = 'http://www.atmovies.com.tw/home/'#atmovie首頁
browser.get(url)
time.sleep(2)
tag1 = browser.find_element_by_id('parallelismLoader')
print(tag1.tag_name)
time.sleep(2)
tag2 = browser.find_elements_by_tag_name('iframe')
for tag in tag2:
  print(tag.get_attribute('src'))
#經由上面得查詢結果，可以得到這網址是連接電影資訊的主要網址，因此以之作
#為查詢"http://www.atmovies.com.tw/james-parallelism/newfilm.html"
url= 'http://www.atmovies.com.tw/james-parallelism/newfilm.html'
browser.get(url)
time.sleep(2)
tag3 = browser.find_elements_by_tag_name('a')
for tag in tag3:
    print(tag.get_attribute('href'))
    title_href1.append(tag.get_attribute('href'))
tag4 = browser.find_elements_by_tag_name('img')
for tag in tag4:
    print(tag.get_attribute('alt'))
    title_arr1.append(tag.get_attribute('alt'))
dists = {"title":title_arr1 ,
      "herf": title_href1,}
df = pd.DataFrame(dists) 
df2 = df.drop(df.index[25])
print(df2)
df2.to_csv("電影資訊(勿用Excel開啟).csv", index=True, encoding="utf8")
df2.to_json("電影資訊.json")









