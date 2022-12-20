import os
import execjs
import requests


os.environ["NODE_PATH"] = os.getcwd()+"/node_modules"

def get_decrypt(res):
    with open('en.js',encoding='utf-8') as f:
        js_code = f.read()
    #print(res)
    js = execjs.compile(js_code)
    newRes = js.call('getRes', res)
    return newRes


def main():
    api = 'https://www.endata.com.cn/API/GetData.ashx'
    data = {
        'startTime': '2022-12-01',
        'MethodName': 'BoxOffice_GetMonthBox'
    }
    header = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ja;q=0.5",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 Edg/108.0.0.0"
    }


    res = requests.post(api,headers=header,data=data)
    if res.status_code == 200:
        return get_decrypt(res.text)

if __name__ == '__main__':
    print(main())



