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
            }, "$:/plugins/oflg/fishing/fishingrod/[all[shadows+tiddlers]tag[?]prefix["+name+"/]]": {
                "title": "$:/plugins/oflg/fishing/fishingrod/[all[shadows+tiddlers]tag[?]prefix["+name+"/]]",
                "caption": name
            }, "$:/plugins/oflg/fishing-cannedfish/"+name+"/SearchWord": {
                "title": "$:/plugins/oflg/fishing-cannedfish/"+name+"/SearchWord",
                "tags": "$:/tags/QuestionTemplate",
                "word": "Canned fish",
                "text": """<$reveal
            state=<<folded-state>>
            type="match"
            text="hide"
            animate="yes"
        >
            {{!!word}}
        </$reveal>

    <span
        class="tc-fish-title"
    >
        <$reveal
            state=<<folded-state>>
            type="nomatch"
            text="hide"
            animate="yes"
        >
            <main style="width:100%;overflow:hidden;"> 
                <iframe id={{!!word}}
                    title={{!!word}}
                    height="700px"
                    width="100%"
                    src={{{[{!!word}encodeuricomponent[]addprefix[https://www.iciba.com/word?w=]]}}}
                    frameborder=0
                    seamless="seamless"
                    style="margin:-130px 0 -60px 0;"
                    marginheight="0"
                    marginwidth="0"
                />
            </main>
        </$reveal>
    </span>"""
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
                    name+"/SearchWord}}"

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
            "version": "0.0.1",
            "type": "application/json",
            "text": text
        }]

        dataJson = json.dumps(twPlugin, ensure_ascii=False)

        with open('./fishing/'+name+'.json', 'w', encoding='UTF-8') as f:
            data = 'some data to be written to the file'
            f.write(dataJson)
            print(name)

# %%
