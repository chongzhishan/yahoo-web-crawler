#!/usr/bin/env python
# coding: utf-8

# # 爬蟲一：查詢豆瓣上“正在上映的電影”

# In[2]:


import pprint
import requests
from lxml import etree

HEADERS = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
    'Refer':'https://movie.douban.com/'
}

url = 'https://movie.douban.com/cinema/nowplaying/'
response = requests.get(url, headers=HEADERS)


text = response.text

html = etree.HTML(text)
ul = html.xpath("//ul[@class='lists']")[0]
lis = ul.xpath('./li')
movies = []
for li in lis:
    title = li.xpath('@data-title')[0]
    score = li.xpath('@data-score')[0]
    release = li.xpath('@data-release')[0]
    duration = li.xpath('@data-duration')[0]
    region = li.xpath('@data-region')[0]
    director = li.xpath('@data-director')[0]
    actors = li.xpath('@data-actors')[0]
    thumbnail = li.xpath('.//img/@src')[0]
    movie = {
        '电影名':title,
        '评分':score,
        "上映时间":release,
        '片长':duration,
        '制片国家':region,
        '导演':director,
        '演员表':actors,
        '海报':thumbnail
    }
    movies.append(movie)
pprint.pprint(movies)

with open('豆瓣正在上映.txt', 'w', encoding='utf-8') as movie_file:
    for movie in movies:
        movie_file.write('电影名：' + movie['电影名'] + '\n')
        movie_file.write('评分：' + movie['评分'] + '\n')
        movie_file.write('上映时间：' + movie['上映时间'] + '\n')
        movie_file.write('片长：' + movie['片长'] + '\n')
        movie_file.write('制片国家：' + movie['制片国家'] + '\n')
        movie_file.write('导演：' + movie['导演'] + '\n')
        movie_file.write('演员表：' + movie['演员表'] + '\n')
        movie_file.write('海报：' + movie['海报'] + '\n')
        movie_file.write('\n')


# # 爬蟲二：查詢豆瓣上“評分前75的電影”

# In[1]:


import re
import urllib.request
import urllib.error
import time

#import urllib2
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
class DouBanSpider(object):
    """类的简要说明
    本类主要用于抓取豆瓣前75的电影名称

    Attributes:
        page: 用于表示当前所处的抓取页面
        cur_url: 用于表示当前争取抓取页面的url
        datas: 存储处理好的抓取到的电影名称
        _top_num: 用于记录当前的top号码
    """

    def __init__(self):
        self.page = 1
        self.cur_url = "http://movie.douban.com/top250?start={page}&filter=&type="
        self.datas = []
        self._top_num = 1
        print("豆瓣電影爬蟲準備就緒...")

    def get_page(self, cur_page):
        """
        根据当前页码爬取网页HTML
        Args:
            cur_page: 表示当前所抓取的网站页码
        Returns:
            返回抓取到整个页面的HTML(unicode编码)
        Raises:
            URLError:url引发的异常
        """
        url = self.cur_url
        time.sleep(3)

        try:
            #print(cur_page)
            page = (cur_page - 1) * 25
            #print(page)
            url = url.format(page=page)
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
            }
            request = urllib.request.Request(url, headers=headers)
            my_page = urllib.request.urlopen(request).read().decode('utf-8')

            print("請求第{}頁，url地址是：{}".format(cur_page,url))

            #print(my_page)
        #urllib.error.URLError  #urllib.request.urlopen.URLError
        except urllib.error.URLError as e:
            if hasattr(e, "code"):
                print("The server couldn't fulfill the request.")
                print("Error code: %s" % e.code)
            elif hasattr(e, "reason"):
                print("We failed to reach a server. Please check your url and read the Reason")
                print("Reason: %s" % e.reason)
        return my_page


    def find_title(self, my_page):
        """
        通过返回的整个网页HTML, 正则匹配前100的电影名称
        Args:
            my_page: 传入页面的HTML文本用于正则匹配
        """
        temp_data = []
        #<span class="title">.*</span>
        #class="">[\s]+<span class="title">(.*?)</span>
        #<span.*?class="title">(.*?)</span>
        movie_items = re.findall(r'<span.*?class="title">(.*?)</span>', my_page, re.S)
        for index, item in enumerate(movie_items):
            if item.find("&nbsp") == -1:
                temp_data.append("Top" + str(self._top_num) + " " + item)
                self._top_num += 1
        self.datas.extend(temp_data)

    def start_spider(self):
        """
        爬虫入口, 并控制爬虫抓取页面的范围
        """
        while self.page <= 3:

            my_page = self.get_page(self.page)
            self.find_title(my_page)
            self.page += 1


def main():
    print(
    """
    ######################################
           豆瓣電影評分前75的爬蟲
    ######################################
    """)
    my_spider = DouBanSpider()
    my_spider.start_spider()
    for item in my_spider.datas:
        print(item)
    print("豆瓣爬蟲爬取結束...")


if __name__ == '__main__':
    main()

