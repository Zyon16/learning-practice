import requests
import json

form = {
    "brand": "free",
    "device": "iphone",
    "country": "cn",
    "genre": "36",
    "date": "2022-11-20",
    "page": 2,
    "is_rank_index": 1,
    "snapshot": "19:42:05"
}


res = requests.post(url='http://localhost:8081/getIt',data=json.dumps(form),headers={"content-type": "application/json"})
res_json = res.json()
print(res_json['analysis'])


test = {
    "code": 10000,
    "msg": "\u6210\u529f",
    "timeData": [
        {
            "id": "5839748",
            "btn": "01:31",
            "up_num": "24",
            "down_num": "0",
            "new_num": "1",
            "out_num": "1",
            "date": "2022-11-23",
            "param": "01:31:03",
            "clear": ""
        },
        {
            "id": "5839758",
            "btn": "01:46",
            "up_num": "0",
            "down_num": "19",
            "new_num": "1",
            "out_num": "1",
            "date": "2022-11-23",
            "param": "01:46:04",
            "clear": ""
        },
        {
            "id": "5839770",
            "btn": "02:49",
            "up_num": "67",
            "down_num": "87",
            "new_num": "2",
            "out_num": "2",
            "date": "2022-11-23",
            "param": "02:49:04",
            "clear": ""
        },
        {
            "id": "5839899",
            "btn": "04:46",
            "up_num": "0",
            "down_num": "127",
            "new_num": "2",
            "out_num": "2",
            "date": "2022-11-23",
            "param": "04:46:04",
            "clear": ""
        },
        {
            "id": "5839954",
            "btn": "05:47",
            "up_num": "53",
            "down_num": "68",
            "new_num": "1",
            "out_num": "1",
            "date": "2022-11-23",
            "param": "05:47:03",
            "clear": ""
        },
        {
            "id": "5840022",
            "btn": "07:50",
            "up_num": "0",
            "down_num": "81",
            "new_num": "4",
            "out_num": "4",
            "date": "2022-11-23",
            "param": "07:50:03",
            "clear": ""
        },
        {
            "id": "5840038",
            "btn": "08:48",
            "up_num": "88",
            "down_num": "61",
            "new_num": "1",
            "out_num": "1",
            "date": "2022-11-23",
            "param": "08:48:04",
            "clear": ""
        },
        {
            "id": "5840159",
            "btn": "09:35",
            "up_num": "91",
            "down_num": "91",
            "new_num": "3",
            "out_num": "3",
            "date": "2022-11-23",
            "param": "09:35:03",
            "clear": ""
        },
        {
            "id": "5840246",
            "btn": "11:50",
            "up_num": "91",
            "down_num": "72",
            "new_num": "5",
            "out_num": "5",
            "date": "2022-11-23",
            "param": "11:50:04",
            "clear": ""
        },
        {
            "id": "5840388",
            "btn": "14:54",
            "up_num": "90",
            "down_num": "72",
            "new_num": "4",
            "out_num": "4",
            "date": "2022-11-23",
            "param": "14:54:04",
            "clear": ""
        }
    ],
    "is_logout": 0
}