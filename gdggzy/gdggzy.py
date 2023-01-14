import requests
import json

def main(page:int=None):
    page = page if page else 1
    
    def get_post():
        res = requests.get(f'http://127.0.0.1:5620/business-demo/invoke?group=gdggzy&action=getPost&page={page}').json()
        
        return {"headers":res['headers'],'form':res['form']}

    post_info = get_post()
    headers = {
        "Content-Type": "application/json",
        "X-Dgi-Req-App": "ggzy-portal",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76"
    }
    headers.update(post_info['headers'])
    headers['X-Dgi-Req-Timestamp'] = str(headers['X-Dgi-Req-Timestamp'])
    form_load = post_info['form']
    for k,v in form_load.items():
        form_load[k] = str(v)
    
    form_load.update({
        'openConvert':'true',
    })

    res = requests.post(
        url='https://ygp.gdzwfw.gov.cn/ggzy-portal/search/v1/items',
        data=form_load,
        headers=headers
        )

    res_json = res.json()
    return res_json
    return res_json['data']

if __name__ == '__main__':
    print(main())