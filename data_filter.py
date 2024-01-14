import csv
import pandas as pd
from bs4 import BeautifulSoup

with open('../data/raw_data/web_data.html', 'r') as file:
    web_data = file.read()
print('read data from web_data.html')

soup1 = BeautifulSoup(web_data, 'html.parser')

timestamp = []
title = []
link = []

time = soup1.find_all('time', {'class': 'LatestNews-timestamp'})
for t in time:
    timestamp.append(t.text)
timestamp_cleaned = [string.strip() for string in timestamp]

news = soup1.find_all('a', {'class': 'LatestNews-headline'})
for n in news:
    title.append(n.get('title'))
    link.append(n.get('href'))

symbol = []
stockPosition = []
changePct = []

sym = soup1.find_all('span', {'class': "MarketCard-symbol"})
for s in sym:
    symbol.append(s.text)
position = soup1.find_all('span', {'class': 'MarketCard-stockPosition'})
for p in position:
    stockPosition.append(p.text)
percent = soup1.find_all('span', {'class': 'MarketCard-changesPct'})
for p in percent:
    changePct.append(p.text)

LastestNews = [symbol, stockPosition, changePct, timestamp_cleaned, title, link]
print('LastestNews list is created')

market_data_dict = {'marketCard_symbol': symbol, 'marketCard_stockPosition': stockPosition, 'marketCard_changePct': changePct}
market_data_df = pd.DataFrame(market_data_dict)
market_data_df.to_csv('../data/processed_data/market_data.csv', index=False)

news_data_dict = {'LatestNews-timestamp': timestamp_cleaned, "title": title, "link": link}
news_data_df = pd.DataFrame(news_data_dict)
news_data_df.to_csv('../data/processed_data/news_data.csv', index=False)

print('csv files created')
