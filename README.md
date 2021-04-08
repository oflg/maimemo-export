# maimemo-export
用于导出墨墨背单词的词库，并生成适用于 List 背单词，欧陆词典，不背单词等的自定义词库。
仓库内已经导出墨墨背单词所有自带词库（暂不包括云词库），多达 900 种词库，可以在仓库中选择需要的词库下载（[下载单个文件的方法](https://blog.csdn.net/u010801439/article/details/81478592)），也可以去 [蓝奏云（密码:666）](https://busiyi.lanzous.com/b00ogbelc) 下载打包好的文件。
- csv 格式用于导入 List 背单词，自带中文解释
- txt 格式用于导入欧陆词典或不被单词，无中文解释

注：中文解释并非导出自墨墨背单词，而是使用 ECDICT 的数据，暂时无法做到与单词书上一致。
## Usage
> 由于 maimemo.db 和 stardict.db 太大，无法放入仓库中，你可以在 [release](https://github.com/ourongxing/maimemo-export/releases/tag/v1.0.0) 中下载并放入文件夹内，这是非常重要的两个数据库文件。
```shell
> python main.py -h
usage: main.py [-h] [-t {csv,txt,both}] [-a | -l [LIST [LIST ...]]]

用于生成适用于 List 背单词，不背单词，欧陆词典等的自定义词库

optional arguments:
  -h, --help            show this help message and exit
  -t {csv,txt,both}, --type {csv,txt,both}
                        导出的文件类型
  -a, --all             导出墨墨背单词所有词库
  -l [LIST [LIST ...]], --list [LIST [LIST ...]]
                        词库名，可多个，与其他选项配合使用时，该选项必须放在最后
```
## Thanks
1. 导出方法来自于 [怎么把墨墨背单词里的词库导出来？ - 你说什么的回答](https://www.zhihu.com/question/392654371/answer/1345899232)
2. 词典来自于 [skywind3000/ECDICT](https://github.com/skywind3000/ECDICT)
3. 词库来自于 [墨墨背单词](https://www.maimemo.com/)

## Buy something to eat for the kitten
如果我所做的事对你有所帮助，欢迎给小猫买点吃的。

也可以去 [这篇回答](https://www.zhihu.com/question/392654371/answer/1808941219) 下点点赞。

![](https://orxing-top.oss-cn-chengdu.aliyuncs.com/img/download%20%281%29.gif?x-oss-process=style/base_webp)
## License
MIT © ourongxing
