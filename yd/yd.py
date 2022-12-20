import execjs
import os
import requests

os.environ["NODE_PATH"] = os.getcwd() + "/node_modules"


def get_it(text: str) -> dict:
    with open('./yd.js') as f:
        js_code = f.read()

    js = execjs.compile(js_code)  # 这里同样可以使用cwd参数指定解释环境
    return js.call('getIt', text)


def translate(text: str) -> str:
    api = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

    header = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ja;q=0.5",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Length": "252",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "OUTFOX_SEARCH_USER_ID=-1592407075@10.112.57.88; OUTFOX_SEARCH_USER_ID_NCOO=2043557013.325027;",
        #"Cookie":"",
        "Host": "fanyi.youdao.com",
        "Origin": "https://fanyi.youdao.com",
        "Pragma": "no-cache",
        "Referer": "https://fanyi.youdao.com/",
        "sec-ch-ua": "\"Microsoft Edge\";v=\"107\", \"Chromium\";v=\"107\", \"Not=A?Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56",
        "X-Requested-With": "XMLHttpRequest"
    }

    form = {
        "i": text,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTlME"
    }
    result = get_it(text)
    header['Cookie'] += f'___rl__test__cookies={result["lts"]}'
    form.update(result)

    res = requests.post(url=api, data=form, headers=header)
    res_json = res.json()
    try:
        return res_json['translateResult'][0][0]['tgt']
    except KeyError:
        return res_json


if __name__ == '__main__':
    print(translate('你好'))
