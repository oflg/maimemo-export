#!/usr/bin/env python
#! -*- coding:utf-8 -*-
'''''' '''''' '''''' '''''' '''''' '''''' '''''' '''''' '''''
   create time: 20210331
   author: ourongxing
   e-mail: orongxing@gmail.com
   github: https://github.com/ourongxing
''' '''''' '''''' '''''' '''''' '''''' '''''' '''''' '''''' ''

import argparse
import codecs
import csv
import os
import sqlite3
import sys
from sqlite3.dbapi2 import ProgrammingError


class Generate(object):
    def __init__(self):
        self.dict = {}
        # 数据库
        self.conn = sqlite3.connect("maimemo.db")
        # 词典 dict
        with open("./EnWords.csv", 'r', encoding="utf-8") as f:
            reader = csv.reader(f)
            rows = [row for row in reader]
            for word in rows:
                self.dict[word[0]] = word[1]

    def exportAll(self, type):
        with open("./墨墨背单词词库名.txt", "r", encoding='utf-8') as f:
            list = f.readlines()
        for i, j in enumerate(list):
            list[i] = list[i].strip('\n')
        self.export(list, type)

    def export(self, list, type):
        conn = self.conn
        cursor = conn.cursor()
        for num, book in enumerate(list):
            sql = """
            SELECT vc_vocabulary
            FROM VOC_TB
            INNER JOIN (
            SELECT title,voc_id,chapter_id,`order`
            FROM BK_VOC_TB V
            INNER JOIN BK_CHAPTER_TB C ON V.chapter_id= C.id AND V.book_id IN (
                SELECT original_id FROM BK_TB WHERE name = '%s' ) ) AS tmp ON VOC_TB.original_id = tmp.voc_id
            ORDER BY `order`
            """ % book
            cursor.execute(sql)
            result = cursor.fetchall()
            self.generate(num, book, result, type)
        cursor.close()
        conn.close()

    def generate(self, num, book, result, type):
        if (result == []):
            print(str(num + 1) + " 未找到：" + book)
            return
        else:
            print(str(num + 1) + " 生成成功：" + book)

        if type == "csv":
            with codecs.open("./dict/csv/" + book + ".csv", "w",
                             "utf_8_sig") as csvfile:
                writer = csv.writer(csvfile)
                for word in result:
                    writer.writerows([[word[0], self.dict.get(word[0])]])
        elif type == "txt":
            with codecs.open("./dict/txt/" + book + ".txt", "w",
                             "utf_8_sig") as txtfile:
                for word in result:
                    txtfile.write(word[0] + "\n")
        else:
            with codecs.open("./dict/csv/" + book + ".csv", "w",
                             "utf_8_sig") as csvfile:
                writer = csv.writer(csvfile)
                for word in result:
                    writer.writerows([[word[0], self.dict.get(word[0])]])
            with codecs.open("./dict/txt/" + book + ".txt", "w",
                             "utf_8_sig") as txtfile:
                for word in result:
                    txtfile.write(word[0] + "\n")


if __name__ == "__main__":
    if os.path.exists("maimemo.db") == False:
        print("maimemo.db 不存在，请下载 release 中的 maimemo.db 文件并放入该文件夹下")
        sys.exit(0)

    #获取命令行传入的参数
    parser = argparse.ArgumentParser(
        description='用于生成适用于 List 背单词，不背单词，欧陆词典等的自定义词库')
    parser.add_argument('-t',
                        '--type',
                        help='导出的文件类型',
                        type=str,
                        default='both',
                        choices=['csv', 'txt', 'both'])
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-a', '--all', help='导出墨墨背单词所有词库', action="store_true")
    group.add_argument('-l',
                       '--list',
                       nargs='*',
                       help='词库名，可多个，与其他选项配合使用时，该选项必须放在最后')
    args = parser.parse_args()

    g = Generate()
    if args.all:
        g.exportAll(args.type)
    elif args.list == None:
        print("必须输入一个词库名称，使用 -l 词库名")
    else:
        g.export(args.list, args.type)
