# china_daily-scraper

This is a web scraper for the famous chinese newspaper 'China Daily'. The aim of this project is to get information about 
certain topics from different perspectives. So I started by analyzing which news are relevant in China.

Keep in mind that this scraper takes into considerations the english version of the newspaper 
(SO HANDLE THE INFORMATION WITH CARE).

## ADVICE & IP STUFF

This script is intended to work from google colab by default, since you dont use your IP when using this service.

If you want to run the script locally, be aware that, thanks to the many requests, 
out IP can be blocked by the newspaper site. In this case, we would want some kind of IP protection. 

I tried to protect my IP by generating a random number in each request and using that number to sleep the script....
but this is a poor way of protecting my IP...


## WHAT WE NEED TO INSTALL

In either case, we nedd to install SELENIUM. So,  we run in the console:
    
    !pip install selenium
    !apt-get update 
    !apt install chromium-chromedriver

If we are running the script locally, we need the PATH to the chromedriver.exe

more info: https://selenium-python.readthedocs.io/installation.html#drivers

## USING THE SCRIPT

The main function is:
    
    china_daily_scraper(topic, PATH)

-Where the topic is the topic we want to search about. There are going to be news related with this topic. 

-The PATH is the path to the webdriver (chromedriver.exe if using chrome). By default (if we run the script in colab), 
 the PATH its a given parameter. 


The main function returns a PANDAS dataframe with every article found related with the topic inserted.

