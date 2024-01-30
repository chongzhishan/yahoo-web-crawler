# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 09:05:38 2021

@author: Wei Sel
"""
# use IMDB website to find information of movie and actor
# use IMDBPY package which is easier than scrap with hand

# In[ Load ]:

import imdb

# In[ main function ]:

def top250_movie(  ):
    ia = imdb.IMDb()
    # 前250名電影
    print('Top 250 movie List')
    top = ia.get_top250_movies()
    for i in range(0,len(top)):
        print(str(i+1)+'. '+top[i]['title']+": "+top[i].movieID)

def bottom100_movie(  ):
    ia = imdb.IMDb()
    # 最後100名電影
    print('\nLast 100 movie List')
    bottom = ia.get_bottom100_movies()
    for i in range(0,len(bottom)):
        print(str(i+1)+'. '+bottom[i]['title']+": "+bottom[i].movieID)

def search_movie(  ):
    
    # importing the module
    import imdb
    
    # creating instance of IMDb
    ia = imdb.IMDb()
      
    # Input movie name
    # Eat Pray Love
    movie_name = input("Please input movie name:")
    # Search movie
    movie = ia.search_movie(movie_name)
    
    # Movie list
    for i in range(0,len(movie)):
        print(movie[i].movieID+": "+movie[i]['title'])
    
    # Insert movie ID from the list above(mainly the first one)
    movie_ID = input("Please input movie id:")
    
    # Get the movie information
    movie_result = ia.get_movie(movie_ID)
    # movie_result.keys()
    ia.update(movie_result)
    
    try:
        # 評分
        print('Rating:',movie_result['rating'])
        
        # 釋放年份
        print('Release year:',movie_result['year'])
        
        # 電影導演
        print('Directors:', end = '')
        for director in movie_result['directors']:
            print(director['name']+' ', end = '')
        
        # 電影種類
        print('Genres:', end = '')
        # print the genres of the movie
        for genre in movie_result['genres']:
            print(genre+' ', end = '')
        
        # 電影演員與角色
        print("\nActor as role:")
        if movie_result:
             movieID = movie_result.movieID
             movie = ia.get_movie(movieID)
             if movie:
                 cast = movie.get('cast')
                 topActors = 5
                 for actor in cast[:topActors]:
                     print( "{0} as {1}".format(actor['name'], actor.currentRole))
                     
        # 電影時長
        # Get hours with floor division
        hours = int(movie_result['runtime'][0]) // 60
        # Get additional minutes with modulus
        minutes = int(movie_result['runtime'][0]) % 60
        # Create time as a string
        time_string = "{} hour {} minute".format(hours, minutes)
        print('Runtime:',time_string)
        
        # 電影製作公司
        print('Production companies:')
        for i in range(0,len(movie_result['production companies'])):
            print(i+1,': ',end='')
            print(movie_result['production companies'][i])
            
        # 國家
        print('Countries:')
        for i in range(0,len(movie_result['countries'])):
            print(i+1,': ',end='')
            print(movie_result['countries'][i])
            
        # ID
        print('ImdbID:',movie_result['imdbID'])
        
        # 票房
        print('Box office:')
        print('Budget:',movie_result['box office']['Budget'])
        print('Opening Weekend United States:',movie_result['box office']['Opening Weekend United States'])
        print('Cumulative Worldwide Gross:',movie_result['box office']['Cumulative Worldwide Gross'])
        # 投票總數
        print('Votes:',movie_result['votes'])
        # 劇情介紹（太長所以先註解）
        # print('plot outline:',movie_result['plot outline'])
            
        # 劇情大綱（太長所以先註解）
        #print('plot:',movie_result['plot'])
        
        # 電影使用語言
        print('Language:',end='')
        for i in range(0,len(movie_result['language'])):
            print(movie_result['language'][i]+' ',end='')
        
        # 能得到的電影資訊
        # ia.get_movie_infoset()
        
        # 電影所得獎項(去前5個)
        kr = ia.get_movie(movie_ID, info=['awards'])
        print("Awards numbers:",len(kr['awards']))
        for i in range(0,min(5,len(kr['awards']))):
            print('Award: '+kr['awards'][i]['award'])
            print('Year:',kr['awards'][i]['year'])
            print('Result: '+kr['awards'][i]['result'])
            print('Category: '+kr['awards'][i]['category'])
            print('Notes: '+kr['awards'][i]['notes'])
            print('To: ',end='')
            for j in range(0,len(kr['awards'][i]['to'])):
                print(kr['awards'][i]['to'][j],end='')
            print('\n')

        
        # 電影語錄（取前3句）
        ar = ia.get_movie(movie_ID, info=['quotes'])
        print('Top 3 quotes:')
        for i in range(0,3):
            print(ar['quotes'][i])
        
        # 電影推薦（不一定有）
        br = ia.get_movie(movie_ID, info=['recommendations'])
        print('Recommendations:')
        print(br['recommendation'])

          
        # 電影關鍵詞（取前10筆）
        cr = ia.get_movie(movie_ID, info=['keywords'])
        print('Top 10 keywords:')
        for i in range(0,9):
            print(cr['keywords'][i]+' ',end='')
        
        # 電影metascore分數
        dr = ia.get_movie(movie_ID, info=['critic reviews'])
        print('Metascore:',dr['metascore'])
        
        # 電影影評（隨機3筆）
        er = ia.get_movie(movie_ID, info=['reviews'])
        for i in range(0,2):
            print('Review '+str(i))
            print('author:',er['reviews'][i]['author'])
            print('date:',er['reviews'][i]['date'])
            print('content:',er['reviews'][i]['content'])
            print("\n")
        
        # 電影標語
        fr = ia.get_movie(movie_ID, info=['taglines'])
        print('Tagline:')
        for i in range(0,len(fr['taglines'])):
            print(i+1,'. ',end='')
            print(fr['taglines'][i])
        
        # 電影投票分佈
        i = imdb.IMDb(accessSystem='http')
        movie = i.get_movie(movie_ID)
        i.update(movie, 'vote details')
        print('Demographics:')
        movie['demographics']
        
    except:
        print("-")
def search_actor(  ):
    ia = imdb.IMDb()
    
    # Input actor name
    # Test: Leonardo DiCaprio
    people_name = input("Please input actor name:")
    # Search actor
    people = ia.search_person(people_name)
    # List actor
    for person in people:
       print(person.personID+": "+person['name'])
    # Input actor ID in above list (mainly the first)
    actor_ID = input("Please input actor id:")
    # Get information of the actor
    actor_result = ia.get_person(actor_ID)
    
    try:
        # 演員工作
        jobs=[]
        for job in actor_result['filmography'].keys():
            print('# Job: ', job)
            jobs.append(job)
            for movie in actor_result['filmography'][job]:
                print('\t%s %s (role: %s)' % (movie.movieID, movie['title'], movie.currentRole))
        
        # 曾經獲得獎項
        kr = ia.get_person(actor_ID, info=['awards'])
        print("Awards numbers:",len(kr['awards']))
        print('\n')
        for i in range(0,min(len(kr['awards']),5)):
            print('Award',i+1)
            print('To: '+actor_result['name'])
            print('Year:',kr['awards'][i]['year'])
            print('Result: '+kr['awards'][i]['result'])
            print('Prize: '+kr['awards'][i]['prize'])
            print('Movies: '+kr['awards'][i]['movies']['title'])
            print('Category: '+kr['awards'][i]['category'])
            print('Award: '+kr['awards'][i]['award'])
            print('\n')
            
        
        # 最近演繹的作品
        try:
            last = actor_result['filmography']['actor'][0]
        except:
            last = actor_result['filmography']['actress'][0]    
        print(people_name,'Latest movie:',last['title'])
        print('Year:',last['year'])
        print('Kind:',last['kind'])
        print('Status:',last['status'])
    except:
        print("-")
    
tokenDict = {
    "1": top250_movie,
    "2": bottom100_movie,
    "3": search_movie,
    "4": search_actor
    }

print('1.Top 250 movie')
print('2. Bottom 100 movie')
print('3. Search movie')
print('4. Search actor')
# Look up the function to call for each word, then call it
ans = input("Please enter 1 to 4:")
functionToCall = tokenDict[ans]
functionToCall()

# =============================================================================
# 
# # In[ Movie Search ]:    
# 
# # importing the module
# import imdb
# 
# # creating instance of IMDb
# ia = imdb.IMDb()
#   
# # Input movie name
# # Eat Pray Love
# movie_name = input("Please input movie name:")
# # Search movie
# movie = ia.search_movie(movie_name)
# 
# # Movie list
# for i in range(0,len(movie)):
#     print(movie[i].movieID+": "+movie[i]['title'])
# 
# # Insert movie ID from the list above(mainly the first one)
# movie_ID = input("Please input movie id:")
# 
# # Get the movie information
# movie_result = ia.get_movie(movie_ID)
# # movie_result.keys()
# ia.update(movie_result)
# 
# try:
#     # 評分
#     print('Rating:',movie_result['rating'])
#     
#     # 釋放年份
#     print('Release year:',movie_result['year'])
#     
#     # 電影導演
#     print('Directors:', end = '')
#     for director in movie_result['directors']:
#         print(director['name']+' ', end = '')
#     
#     # 電影種類
#     print('Genres:', end = '')
#     # print the genres of the movie
#     for genre in movie_result['genres']:
#         print(genre+' ', end = '')
#     
#     # 電影演員與角色
#     print("\nActor as role:")
#     if movie_result:
#          movieID = movie_result.movieID
#          movie = ia.get_movie(movieID)
#          if movie:
#              cast = movie.get('cast')
#              topActors = 5
#              for actor in cast[:topActors]:
#                  print( "{0} as {1}".format(actor['name'], actor.currentRole))
#                  
#     # 電影時長
#     # Get hours with floor division
#     hours = int(movie_result['runtime'][0]) // 60
#     # Get additional minutes with modulus
#     minutes = int(movie_result['runtime'][0]) % 60
#     # Create time as a string
#     time_string = "{} hour {} minute".format(hours, minutes)
#     print('Runtime:',time_string)
#     
#     # 電影製作公司
#     print('Production companies:')
#     for i in range(0,len(movie_result['production companies'])):
#         print(i+1,': ',end='')
#         print(movie_result['production companies'][i])
#         
#     # 國家
#     print('Countries:')
#     for i in range(0,len(movie_result['countries'])):
#         print(i+1,': ',end='')
#         print(movie_result['countries'][i])
#         
#     # ID
#     print('ImdbID:',movie_result['imdbID'])
#     
#     # 票房
#     print('Box office:')
#     print('Budget:',movie_result['box office']['Budget'])
#     print('Opening Weekend United States:',movie_result['box office']['Opening Weekend United States'])
#     print('Cumulative Worldwide Gross:',movie_result['box office']['Cumulative Worldwide Gross'])
#     # 投票總數
#     print('Votes:',movie_result['votes'])
#     # 劇情介紹（太長所以先註解）
#     # print('plot outline:',movie_result['plot outline'])
#         
#     # 劇情大綱（太長所以先註解）
#     #print('plot:',movie_result['plot'])
#     
#     # 電影使用語言
#     print('Language:',end='')
#     for i in range(0,len(movie_result['language'])):
#         print(movie_result['language'][i]+' ',end='')
#     
#     # 能得到的電影資訊
#     # ia.get_movie_infoset()
#     
#     # 電影所得獎項(去前5個)
#     kr = ia.get_movie(movie_ID, info=['awards'])
#     print("Awards numbers:",len(kr['awards']))
#     for i in range(0,min(5,len(kr['awards']))):
#         print('Award: '+kr['awards'][i]['award'])
#         print('Year:',kr['awards'][i]['year'])
#         print('Result: '+kr['awards'][i]['result'])
#         print('Category: '+kr['awards'][i]['category'])
#         print('Notes: '+kr['awards'][i]['notes'])
#         print('To: ',end='')
#         for j in range(0,len(kr['awards'][i]['to'])):
#             print(kr['awards'][i]['to'][j],end='')
#         print('\n')
# 
#     
#     # 電影語錄（取前3句）
#     ar = ia.get_movie(movie_ID, info=['quotes'])
#     print('Top 3 quotes:')
#     for i in range(0,3):
#         print(ar['quotes'][i])
#     
#     # 電影推薦（不一定有）
#     br = ia.get_movie(movie_ID, info=['recommendations'])
#     print('Recommendations:')
#     print(br['recommendation'])
# 
#       
#     # 電影關鍵詞（取前10筆）
#     cr = ia.get_movie(movie_ID, info=['keywords'])
#     print('Top 10 keywords:')
#     for i in range(0,9):
#         print(cr['keywords'][i]+' ',end='')
#     
#     # 電影metascore分數
#     dr = ia.get_movie(movie_ID, info=['critic reviews'])
#     print('Metascore:',dr['metascore'])
#     
#     # 電影影評（隨機3筆）
#     er = ia.get_movie(movie_ID, info=['reviews'])
#     for i in range(0,2):
#         print('Review '+str(i))
#         print('author:',er['reviews'][i]['author'])
#         print('date:',er['reviews'][i]['date'])
#         print('content:',er['reviews'][i]['content'])
#         print("\n")
#     
#     # 電影標語
#     fr = ia.get_movie(movie_ID, info=['taglines'])
#     print('Tagline:')
#     for i in range(0,len(fr['taglines'])):
#         print(i+1,'. ',end='')
#         print(fr['taglines'][i])
#     
#     # 電影投票分佈
#     i = imdb.IMDb(accessSystem='http')
#     movie = i.get_movie(movie_ID)
#     i.update(movie, 'vote details')
#     print('Demographics:')
#     movie['demographics']
#     
# except:
#     print("-")
# 
# 
#     
# # In[ Actor Search ]:    
# 
# ia = imdb.IMDb()
# 
# # Input actor name
# # Test: Leonardo DiCaprio
# people_name = input("Please input actor name:")
# # Search actor
# people = ia.search_person(people_name)
# # List actor
# for person in people:
#    print(person.personID+": "+person['name'])
# # Input actor ID in above list (mainly the first)
# actor_ID = input("Please input actor id:")
# # Get information of the actor
# actor_result = ia.get_person(actor_ID)
# 
# try:
#     # 演員工作
#     jobs=[]
#     for job in actor_result['filmography'].keys():
#         print('# Job: ', job)
#         jobs.append(job)
#         for movie in actor_result['filmography'][job]:
#             print('\t%s %s (role: %s)' % (movie.movieID, movie['title'], movie.currentRole))
#     
#     # 曾經獲得獎項
#     kr = ia.get_person(actor_ID, info=['awards'])
#     print("Awards numbers:",len(kr['awards']))
#     print('\n')
#     for i in range(0,min(len(kr['awards']),5)):
#         print('Award',i+1)
#         print('To: '+actor_result['name'])
#         print('Year:',kr['awards'][i]['year'])
#         print('Result: '+kr['awards'][i]['result'])
#         print('Prize: '+kr['awards'][i]['prize'])
#         print('Movies: '+kr['awards'][i]['movies']['title'])
#         print('Category: '+kr['awards'][i]['category'])
#         print('Award: '+kr['awards'][i]['award'])
#         print('\n')
#         
#     
#     # 最近演繹的作品
#     try:
#         last = actor_result['filmography']['actor'][0]
#     except:
#         last = actor_result['filmography']['actress'][0]    
#     print(people_name,'Latest movie:',last['title'])
#     print('Year:',last['year'])
#     print('Kind:',last['kind'])
#     print('Status:',last['status'])
# except:
#     print("-")
# 
# # In[ Top and Bottom Movie ]:    
# 
# # 前250名電影
# print('Top 250 movie List')
# top = ia.get_top250_movies()
# for i in range(0,len(top)):
#     print(str(i+1)+'.'+top[i]['title']+": "+top[i].movieID)
# 
# # 最後100名電影
# print('\nLast 100 movie List')
# bottom = ia.get_bottom100_movies()
# for i in range(0,len(bottom)):
#     print(str(i+1)+'.'+bottom[i]['title']+": "+bottom[i].movieID)
#     
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# =============================================================================
