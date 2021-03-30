import codecs
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

    # csv，用于导入 List 背单词，我一般配合单词书背，所以不需要中文解释
    # with codecs.open("./dist/" + name + "-无中文.csv", "w",
    #                  "utf_8_sig") as csvfile:
    #     writer = csv.writer(csvfile)
    #     for i, val in enumerate(result):
    #         writer.writerows([[val[0], "无"]])

    # txt，用于导入欧陆词典
    with codecs.open("./dist/" + name + ".txt", "w", "utf_8_sig") as txtfile:
        for i, val in enumerate(result):
            txtfile.write(val[0] + "\n")


if __name__ == "__main__":
    if os.path.exists("./maimemo.db"):
        for i, j in enumerate(sys.argv[1:]):
            generate(i, j)
    else:
        print("maimemo.db 不存在，请下载 release 中的 maimemo.db 文件并放入该文件夹下")
