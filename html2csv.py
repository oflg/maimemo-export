import codecs
import csv
import os

# pip install beautifulsoup4
from bs4 import BeautifulSoup

# 欧陆词典导出 html 文件，放入 src 文件夹内
src = './src/2022恋词考研英语真题5500词.html'

file = open(src, encoding='utf-8')
soup = BeautifulSoup(file, 'html.parser')
tr = soup.tbody.find_all('tr')

with codecs.open("./dist/"+os.path.splitext(os.path.split(src)[1])[0]+".csv", "w", "utf_8_sig") as csvfile:
    writer = csv.writer(csvfile)
    for i, val in enumerate(tr):
        writer.writerows(
            [[val.find_all('td')[1].get_text(), val.find_all('td')[3].get_text()]])
file.close()
