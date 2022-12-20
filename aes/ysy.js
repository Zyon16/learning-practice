let crypto = require('crypto-js')


function __getData(t) {
    var e = t.data
      , n = t.type
      , a = t.param
      , r = t.key
      , o = JSON.parse(JSON.stringify(e));
    return "Base64" === n ? a.forEach((function(t) {
        o[t] = btoa(o[t])
    }
    )) : a.forEach((function(t) {
        var e = o[t];
        r = crypto.enc.Latin1.parse(r);
        var n = r
          , a = crypto.AES.encrypt(e, r, {
            iv: n,
            mode: crypto.mode.CBC,
            padding: crypto.pad.ZeroPadding
        });
        o[t] = a.toString()
    }
    )),
    o
}

function getData(account,pswd,redomStr){
    return __getData({
        "data": {
        "username": account,
        "password": pswd,
        "redomStr": redomStr
        },
        "key": "password.yunjy.y",
        "param": [
            "password"
        ]
    })
}


console.log(getData('15312341234','asda1348315135153'))