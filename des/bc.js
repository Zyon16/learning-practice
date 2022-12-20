//DES文章重出现的某小网站逆向源码
let CryptoJS = require('crypto-js')

function rndString() {
    for (var e = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXTZabcdefghiklmnopqrstuvwxyz", t = "", n = 0; n < 16; n++) {
        var a = Math.floor(Math.random() * e.length);
        t += e.substring(a, a + 1)
    }
    return t
}
function desEncrypt(e, t) {
    var n = CryptoJS.enc.Utf8.parse(t);
    return CryptoJS.DES.encrypt(e, n, {
        mode: CryptoJS.mode.ECB,
        padding: CryptoJS.pad.Pkcs7
    }).toString()
}

const login_data = {
    "username": "asda551313",
    "password": "assd45646",
    "captcha": ""
}

console.log(desEncrypt(JSON.stringify(login_data),rndString()))

