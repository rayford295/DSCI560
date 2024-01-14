import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = 'https://www.cnbc.com/world/?region=world'
response = requests.get(url)
content = BeautifulSoup(response.text, 'html.parser')
newslist = content.find_all('ul', {'class': 'LatestNews-list'})
for n in newslist:
    latestnews = n.prettify()
    
browser = webdriver.Chrome()
browser.get(url)
time.sleep(2)
marketdata = browser.find_elements(By.XPATH, "//*[@id='market-data-scroll-container']")
for m in marketdata:
    marketbanner = m.get_attribute('outerHTML')
browser.quit()

with open('../data/raw_data/web_data.html', 'w') as file:
    file.write(latestnews)
    file.write(marketbanner)
    
with open('../data/raw_data/web_data.html', 'r') as file:
    for line_num, line in enumerate(file, start=1):
        print(line, end='')
        if line_num == 10:
            break
