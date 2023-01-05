import os
import execjs
import requests
import json

#os.environ["NODE_PATH"] = os.getcwd()+"/node_modules"

class ExecJs:
    def __init__(self):
        self.js = self.__get_js()

    def __get_js(self):
        with open('gjyb.js', encoding='utf-8') as f:
            js_code = f.read()

        return execjs.compile(js_code)

    def get_post_info(self,page,area):
        return self.js.call('get_post',page,area)
    def get_data(self,data):
        return self.js.call('get_data',data)

def get_info(page,area):
    js = ExecJs()
    api = 'https://fuwu.nhsa.gov.cn/ebus/fuwu/api/nthl/api/CommQuery/queryFixedHospital'
    headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ja;q=0.5",
        "Cache-Control": "no-cache",
        "Content-Type": "application/json",
        "contentType": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54"
    }
    post_info = js.get_post_info(page,area)
    post_info_headers = post_info['headers']
    headers.update({
        'x-tif-paasid':'undefined',
        'channel':post_info['headers']['channel'],
        'x-tif-timestamp':str(post_info_headers['x-tif-timestamp']),
        'x-tif-signature':post_info_headers['x-tif-signature'],
        'x-tif-nonce':post_info_headers['x-tif-nonce']

    })
    form = json.loads(post_info['data'])
    form['data']['timestamp']= str(form['data']['timestamp'])
    form = json.dumps(form)

    res = requests.post(api,headers=headers,data=form)
    res_json = res.json()
    return js.get_data(res_json)




if __name__ == "__main__":
    print(get_info(1,"340600"))
