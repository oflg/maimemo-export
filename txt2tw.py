# %%
import os
import json
import datetime

basepath = './dicts/txt_list/'

fileNames = os.listdir(basepath)

for fileName in fileNames:
    name = fileName.replace('.txt', '')

    with open(basepath + fileName, 'r', encoding='UTF-8-sig') as file:
        lines = file.readlines()

        tags = ''
        tiddlers = {
            "$:/plugins/oflg/fishing-cannedfish/"+name+"/readme": {
                "title": "$:/plugins/oflg/fishing-cannedfish/"+name+"/readme",
                "text": "Installation and usage tutorial is available at [[Fishing Manual|https://oflg.github.io/fishing/]].\n\n可在 [[钓鱼手册|https://oflg.github.io/fishing/]] 查看安装使用教程。"
            }, "$:/plugins/oflg/fishing/fishingrod/[[$:/plugins/oflg/fishing-cannedfish/"+name+"]plugintiddlers[]tag[?]]": {
                "title": "$:/plugins/oflg/fishing/fishingrod/[[$:/plugins/oflg/fishing-cannedfish/"+name+"]plugintiddlers[]tag[?]]",
                "type": "application/json",
                "caption": name
            }, "$:/plugins/oflg/fishing-cannedfish/"+name+"/Question": {
                "title": "$:/plugins/oflg/fishing-cannedfish/"+name+"/Question",
                "tags": "$:/tags/QuestionTemplate",
                "word": "fishing",
                "text": """
<$reveal
    state=<<folded-state>>
    type="match"
    text="hide"
    animate="yes"
>
    {{!!word}}
</$reveal>

<$reveal
    state=<<folded-state>>
    type="nomatch"
    text="hide"
    animate="yes"
>
    <span
        class="tc-fish-title"
    >
        <main style="width:100%;overflow:hidden;"> 
            <iframe id={{!!word}}
                title={{!!word}}
                height="700px"
                width="100%"
                src={{{[{!!word}encodeuricomponent[]addprefix[https://quark.sm.cn/api/rest?method=quark_fanyi.dlpage&format=html&schema=v2&entry=top#en/zh/]]}}}
                frameborder=0
                seamless="seamless"
                style="margin:-200px 0 -110px 0;"
                marginheight="0"
                marginwidth="0"
            />
        </main>
    </span>
</$reveal>
"""
            }
        }

        for line in lines:
            if line.startswith('#'):
                tags = '[['+line.strip('#').replace('\n', '')+']] ?'
            else:
                twNow = str(datetime.datetime.utcnow()).replace(
                    '-', '').replace(' ', '').replace(':', '').replace('.', '')
                word = line.replace('\n', '')
                title = name+'/' + twNow
                caption = "{{||$:/plugins/oflg/fishing-cannedfish/" + \
                    name+"/Question}}"

                tiddlers[title] = {
                    "title": title,
                    "tags": tags,
                    "word": word,
                    "created": twNow,
                    "caption": caption,
                }

        text = json.dumps({
            'tiddlers': tiddlers
        }, ensure_ascii=False)

        twPlugin = [{
            "author": "oflg",
            "core-version": ">=5.2.1",
            "dependents": "$:/plugins/oflg/fishing-cannedfish",
            "description": "记忆包",
            "list": "readme",
            "name": name,
            "parent-plugin": "$:/plugins/oflg/fishing-cannedfish",
            "plugin-type": "plugin",
            "source": "https://github.com/oflg/fishing-cannedfish",
            "title": "$:/plugins/oflg/fishing-cannedfish/"+name,
            "version": "0.0.4",
            "type": "application/json",
            "text": text
        }]

        dataJson = json.dumps(twPlugin, ensure_ascii=False)

        with open('/home/oflg/Code/FishingManual/plugins/oflg/fishing-cannedfish/'+name+'.json', 'w', encoding='UTF-8') as f:
            data = 'some data to be written to the file'
            f.write(dataJson)
            print(name)

# %%
