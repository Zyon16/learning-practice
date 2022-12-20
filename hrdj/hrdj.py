import os
import execjs
import requests
import json

os.environ["NODE_PATH"] = os.path.join('../' + "/node_modules")


class HRDJ:
    def __init__(self):
        self.__js = self.__js_load()
        self.token = None

        self.header = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ja;q=0.5",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Length": "137",
            "Content-Type": "application/json",
            "Host": "user.hrdjyun.com",
            "Origin": "https://www.hh1024.com",
            "Pragma": "no-cache",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56"
        }

    def __js_load(self):
        with open('./hrdj.js') as f:
            js_code = f.read()

        return execjs.compile(js_code)

    def __get_form(self, account: str, pswd: str) -> dict:
        return self.__js.call('getForm', account, pswd)

    def __post(self, api, header=None, data=None, params=None):
        if not header:
            header = self.header

        res = requests.post(api, headers=header, data=data, params=params)

        if res.status_code == 200:
            res_json = res.json()
            if res_json['status'] == 0:
                return {'status': 0, 'msg': 'OK', 'data': res_json['data']}
            else:
                return {'status': 1, 'msg': f'status:{res_json["status"]}-{res_json["message"]}', 'data': {}}
        else:
            return {'status': 2, 'msg': f'{res.status_code}-请求失败', 'data': {}}

    def login(self, account: str, pswd: str) -> str:
        api = 'https://user.hrdjyun.com/wechat/phonePwdLogin'

        # res = requests.post(url=api, data=json.dumps(self.__get_form(account, pswd)), headers=self.header)
        res = self.__post(api, data=json.dumps(self.__get_form(account, pswd)))
        if res['status'] == 0:
            self.token = res['data']['token']
            return '登录成功'
        else:
            return '登录失败'

    def get_items(self, date) -> dict | list:
        if self.token:
            api = 'https://ucp.hrdjyun.com:60359/api/dy'

            form = {
                'param': self.__js.call('getParams',date),
                'sign': self.__js.call('getSign', date),
                'tenant': '1',
                'token': self.token,
                'timestamp': str(self.__js.call('getTime'))
            }
            res = self.__post(api, data=json.dumps(form))

            if res['status'] == 0:
                return res['data']
            else:
                return res
        else:
            return {'status':3,'msg':'未登录'}

if __name__ == '__main__':
    hr = HRDJ()
    #hr.login('15375250723', 'p15375250723')
    hr.token = 'OpqHUDy9nTkJG6HK3em4bZwh6bcj+4Xcr8kIvDymrZdzdibcvngdAQ=='
    i = hr.get_items('2022-11-30')
    print(i)
