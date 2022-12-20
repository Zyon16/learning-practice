import os
import execjs
import requests


os.environ["NODE_PATH"] = os.getcwd()+"/node_modules"

def get_encrypt(account,pswd) -> dict:
    with open('tyy.js') as f:
        js_code = f.read()

    js = execjs.compile(js_code)
    return js.call('getPswd', account,pswd)


def main(account,pswd):
    header = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ja;q=0.5",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 Edg/108.0.0.0"
    }
    res = requests.get(url='https://m.ctyun.cn/account/login',headers=header,params={
        'userName':account,
        'password':get_encrypt(account,pswd),
        'referrer':'wap',
        'mainVersion':'300031500'
    })
    if res.status_code == 200:
        res_json = res.json()
        return res_json
    else:
        return res.text

if __name__ == '__main__':
    print(main('abc123456@163.com','ashdakozxbces'))

