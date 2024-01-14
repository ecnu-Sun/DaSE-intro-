import requests
from bs4 import BeautifulSoup
import csv

# 新浪国际新闻的URL
url = 'https://news.sina.com.cn/world/'
# 发送请求并获取网页内容
response = requests.get(url)
response.encoding = 'utf-8'
# 解析HTML
soup = BeautifulSoup(response.text, 'html.parser')
# 找到新闻列表
news_list = soup.find_all('div', class_='news-item')
# 用于存储新闻数据的列表
news_data = []
# 遍历新闻列表，提取所需信息
for news in news_list:
    title_tag = news.find('h2')
    if title_tag:
        title = title_tag.get_text().strip()
        link = title_tag.find('a')['href']
        time_tag = news.find('div', class_='time')
        print(title)
        news_time = time_tag.get_text().strip()
        news_data.append([title, news_time, link])
# 将数据保存到CSV文件
with open('sina_news.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['标题', '时间', '链接'])
    for item in news_data:
        writer.writerow(item)