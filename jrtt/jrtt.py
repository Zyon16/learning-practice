import requests

def get_list(channel=None):
    def get_url(c=None):
        params = {
            'group':'jrtt',
            'action':'getUrl',
            'channel': c if c else ''
        }
        return requests.get('http://127.0.0.1:5620/business-demo/invoke',params=params).json()['data']

    s = requests.session()
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76"

    }

    res = s.get(url=get_url(channel),headers=headers)
    res_json = res.json()
    return res_json['data']


if __name__ == "__main__":
    print(get_list())
