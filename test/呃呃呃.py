# By：仰晨
# 文件名：呃呃呃
# 时 间：2023/4/9 0:53
import requests
from bs4 import BeautifulSoup

url = 'https://www.douyin.com/user/MS4wLjABAAAAcOogp8WSlLvXNTPUg9b9brwWXQj76F9qeckY4T4w3kOzyuAMP-BFj2SbGqwIYwSZ?vid=7219194157544377637'

res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
p_tag = soup.find('p', class_='iQKjW6dr')

if p_tag:
    print(p_tag.text)
else:
    print(res.text)
