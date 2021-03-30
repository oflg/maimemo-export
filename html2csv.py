import codecs
import csv
import os
import sys

# you need use 'pip install beautifulsoup4'
from bs4 import BeautifulSoup


def generate(num, src):
    try:
        file = open(src, encoding='utf-8')
    except IOError as e:
        print(str(num + 1) + " 未找到：" + os.path.split(src)[1])
        pass
    else:
        soup = BeautifulSoup(file, 'html.parser')
        tr = soup.tbody.find_all('tr')
        with codecs.open(
                "./dist/" + os.path.splitext(os.path.split(src)[1])[0] +
                ".csv", "w", "utf_8_sig") as csvfile:
            writer = csv.writer(csvfile)
            for i, val in enumerate(tr):
                writer.writerows([[
                    val.find_all('td')[1].get_text(),
                    val.find_all('td')[3].get_text()
                ]])
        file.close()
        print(
            str(num + 1) + " 生成成功：" +
            os.path.splitext(os.path.split(src)[1])[0])


if __name__ == "__main__":
    for i, j in enumerate(sys.argv[1:]):
        generate(i, j)
