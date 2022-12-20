const cryptojs = require('crypto-js')

let generateSaltSign = function(e) {
    const navigator = {
        appVersion:'5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56'
    }

    let t = cryptojs.MD5(navigator.appVersion).toString()
      , r = "" + (new Date).getTime()
      , i = r + parseInt(10 * Math.random(), 10);
    return {
        ts: r,
        bv: t,
        salt: i,
        sign: cryptojs.MD5("fanyideskweb" + e + i + "Ygy_4c=r#e#4EX^NUGUc5").toString()
    }
};




function getIt(text){
    let n = text
    , r =generateSaltSign(n)
    , i = n.length;

    let need = {
        salt : r.salt,
        sign : r.sign,
        lts :r.ts,
        bv :r.bv
    }
    
    return need
}

module.exports = {get:getIt}



