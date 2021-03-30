# maimemo-export
用于导出墨墨背单词的词库，并生成可导入 List 背单词的自定义词库。
## 快速使用
> 由于 maimemo.db 数据库文件太大，无法放入仓库中，你可以在 release 中下载后放入文件夹中。

gengerate.py 脚本支持多个参数，生成可导入欧陆词典的 txt 文件。
```shell
python generate.py 词库名称1 词库名称2 ...
```
html2csv.py 脚本也支持多个参数，将欧陆词典导出的 html 文件转换为可导入 List 背单词的 csv 文件，最好统一放入 dict 文件夹中。
```shell
python html2csv.py 欧陆词典导出的文件1 欧陆词典导出的文件2 ...
```
生成的所有文件都在 dict 文件夹中，所有纯单词的 txt 文件都已经导出

欧陆词典导出的方法可以查看 [该文章](还没写)，希望大家一起协作，为 List 背单词增加词库，欢迎 Pull requests，毕竟我一个人的时间有限。