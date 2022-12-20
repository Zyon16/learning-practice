const analysis = require('./qm')
const express = require('express')
const bodyParser = require('body-parser')

const app = express()
app.use(bodyParser.urlencoded({extended:false}))
app.use(bodyParser.json())

const get_analysis = analysis.get

app.post('/getIt', function (req, res) {
    const data = req.body
    console.log(data)
    let t = {
        "url": "/rank/index",
        "method": "get",
        "headers": {
            "common": {
                "Accept": "application/json, text/plain, */*"
            },
            "delete": {},
            "get": {},
            "head": {},
            "post": {
                "Content-Type": "application/x-www-form-urlencoded"
            },
            "put": {
                "Content-Type": "application/x-www-form-urlencoded"
            },
            "patch": {
                "Content-Type": "application/x-www-form-urlencoded"
            }
        },
        "params": {
            "brand": "",
            "device": "",
            "country": "",
            "genre": "",
            "date": "",
            "page": 1,
            "is_rank_index": 1,
            "snapshot": ""
        },
        "baseURL": "https://api.qimai.cn",
        "transformRequest": [
            null
        ],
        "transformResponse": [
            null
        ],
        "timeout": 15000,
        "withCredentials": true,
        "xsrfCookieName": "XSRF-TOKEN",
        "xsrfHeaderName": "X-XSRF-TOKEN",
        "maxContentLength": -1,
        "maxBodyLength": -1
    }
    t["params"] = data

    let result = {
        "msg":"DONE",
        "analysis":get_analysis(t)
    }

    res.send(result)
 })


const server = app.listen(8081, function () {

    const host = server.address().address
    const port = server.address().port

    console.log("应用实例，访问地址为 http://%s:%s", host, port)

})
