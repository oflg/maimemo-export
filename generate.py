import codecs
import csv
import os
import sqlite3
import sys


def generate(num, name):
    db = sqlite3.connect("maimemo.db")
    cursor = db.cursor()
    sql = """
    SELECT vc_vocabulary
    FROM VOC_TB
    INNER JOIN (
    SELECT title,voc_id,chapter_id,`order`
    FROM BK_VOC_TB V
    INNER JOIN BK_CHAPTER_TB C ON V.chapter_id= C.id AND V.book_id IN (
        SELECT original_id FROM BK_TB WHERE name = '%s' ) ) AS tmp ON VOC_TB.original_id = tmp.voc_id
    ORDER BY `order`
    """ % name
    cursor.execute(sql)
    result = cursor.fetchall()
    db.close()
    if (result == []):
        print(str(num + 1) + " 未找到：" + name)
        return
    else:
        print(str(num + 1) + " 生成成功：" + name)

    with codecs.open("./dict/csv/" + name + ".csv", "w",
                     "utf_8_sig") as csvfile:
        writer = csv.writer(csvfile)
        for word in result:
            writer.writerows([[word[0], dict.get(word[0])]])

    # txt，用于导入欧陆词典，不背单词
    with codecs.open("./dict/txt/" + name + ".txt", "w",
                     "utf_8_sig") as txtfile:
        for i, val in enumerate(result):
            txtfile.write(val[0] + "\n")


if __name__ == "__main__":
    # 获取词典
    dict = {}
    with open("./EnWords.csv", 'r', encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = [row for row in reader]
        for word in rows:
            dict[word[0]] = word[1]

    # 用于一键导出所有词库
    with open("./墨墨背单词词库名.txt", "r", encoding='utf-8') as f:
        data = f.readlines()
    for i, j in enumerate(data):
        generate(i, j.strip('\n'))

    # if os.path.exists("./maimemo.db"):
    #     for i, j in enumerate(sys.argv[1:]):
    #         generate(i, j)
    # else:
    #     print("maimemo.db 不存在，请下载 release 中的 maimemo.db 文件并放入该文件夹下")
