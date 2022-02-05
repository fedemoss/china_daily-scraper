# -*- coding: utf-8 -*-
"""
@author: mossney


This is a web scraper for the famous chinese newspaper 'China Daily'. The aim of this project is to get information about 
certain topics from different perspectives. So I started by analyzing which news are relevant in China.

Keep in mind that this scraper takes into considerations the english version of the newspaper 
(SO HANDLE THE INFORMATION WITH CARE).

------- ADVICE & IP STUFF

This script is intended to work from google colab by default, since you dont use your IP when using this service.

If you want to run the script locally, be aware that, thanks to the many requests, 
out IP can be blocked by the newspaper site. In this case, we would want some kind of IP protection. 

I tried to protect my IP by generating a random number in each request and using that number to sleep the script....
but this is a poor way of protecting my IP...


------- WHAT WE NEED TO INSTALL

In either case, we nedd to install SELENIUM. So,  we run in the console:
    
    !pip install selenium
    !apt-get update 
    !apt install chromium-chromedriver

If we are running the script locally, we need the PATH to the chromedriver.exe

more info: https://selenium-python.readthedocs.io/installation.html#drivers


-------- USING THE SCRIPT

The main function is:
    
    china_daily_scraper(topic, PATH)

-Where the topic is the topic we want to search about. There are going to be news related with this topic. 

-The PATH is the path to the webdriver (chromedriver.exe if using chrome). By default (if we run the script in colab), 
 the PATH its a given parameter. 


The main function returns a PANDAS dataframe with every article found related with the topic inserted.


"""

#General info of a page
def articles_finder(soup):
  news = soup.findAll(name = 'span', attrs = {'class' : 'intro'})
  newspaper = []
  link = []
  title = []
  date = []
  time = []
  for item in news:
    newspaper.append('China Daily')
    link.append(item.find('a')['href'])
    title.append(item.find('a').text)
    date.append(item.find('b').text.split(")")[1].split(' ')[1])
    time.append(item.find('b').text.split(")")[1].split(' ')[2])
  general_dict = {'Newspaper': newspaper, 'Title': title, 'Date': date, 'Time': time, 'Link': link}
  df = pd.DataFrame(general_dict)
  return df

#Number of pages
def pages_number(url):
  driver.get(url)
  time.sleep(2)
  html = driver.page_source
  soup = BS(html, 'html.parser')
  pages = int(soup.find(attrs= {'class': 'pageno'}).text.split('/')[1])
  return pages
  
#Content
def give_me_content(soup):
  paragraphs = soup.find(attrs={'id':'Content'}).find_all('p')

  content = []
  for p in paragraphs:
    content.append(p.text)

  content = " ".join(content)
  return content

def china_daily_scraper(topic, PATH='chromedriver'):
  import numpy as np
  import pandas as pd
  import time
  from bs4 import BeautifulSoup as BS
  from selenium import webdriver
  chrome_options = webdriver.ChromeOptions()
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')
  driver = webdriver.Chrome(PATH, chrome_options=chrome_options)

  topic.replace(' ','+')
  url = 'http://newssearch.chinadaily.com.cn/en/search?query={}'.format(topic)

  #iterate through every page
  pages = pages_number(url)
  df = []
  for i in range(pages-1):
    driver.get(url)
    time.sleep(2)
    html = driver.page_source
    soup = BS(html, 'html.parser')  
    df.append(articles_finder(soup))

    driver.find_element_by_css_selector('.next').click() #Next page

  df = pd.concat(df,ignore_index=True)
  #Content of every new
  links = df['Link']
  content = []
  for url in links:
    driver.get(url)
    time.sleep(2)
    html = driver.page_source
    soup = BS(html, 'html.parser')
    content.append(give_me_content(soup))
    time.sleep(np.random.uniform(0.5,1)) #Acting as a normal user

  df['Content'] = content

  return df