import requests

def get_cookie():
    api = 'http://127.0.0.1:5620/business-demo/invoke?group=ths&action=getCookie'
    res = requests.get(api)

    return res.json()['data']

def get_info(page):
    
    api = f'http://q.10jqka.com.cn/index/index/board/all/field/zdf/order/desc/page/{page}/ajax/1/'
    headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54",
        "Cookie":f"v={get_cookie()}"
    }

    res = requests.get(api,headers=headers)

    print(res.text)

if __name__ == '__main__':
    get_info(1)