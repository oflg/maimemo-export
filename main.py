import codecs
import csv
import sqlite3

conn = sqlite3.connect("./src/maimemo.db")
cursor = conn.cursor()

# 单词本的名称
name = "2022恋词考研英语真题5500词"

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
conn.close()

# csv，用于导入 List 背单词
with codecs.open("./dist/"+name+"-无中文.csv", "w", "utf_8_sig") as csvfile:
    writer = csv.writer(csvfile)
    for i, val in enumerate(result):
        writer.writerows([[val[0], "无中文"]])

# txt，用于导入欧陆词典
with codecs.open("./dist/"+name+".txt", "w", "utf_8_sig") as txtfile:
    for i, val in enumerate(result):
        txtfile.write(val[0]+"\n")