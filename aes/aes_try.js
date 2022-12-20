let crypto = require('crypto-js')

function aesEncrypt(aesMsg,aesKey,aesIv){
    let key = crypto.enc.Utf8.parse(aesKey),
        iv = crypto.enc.Utf8.parse(aesIv),
        msg = crypto.enc.Utf8.parse(aesMsg),
        encrypted = crypto.AES.encrypt(msg,key,{
            iv:iv,
            mode:crypto.mode.CBC,
            padding:crypto.pad.Pkcs7
        })
    return encrypted.toString()
}

function aesDecrypt(aesMsg,aesKey,aesIv){
    let key = crypto.enc.Utf8.parse(aesKey),
        iv = crypto.enc.Utf8.parse(aesIv),
        encrypted = crypto.AES.decrypt(aesMsg,key,{
            iv:iv,
            mode:crypto.mode.CBC,
            padding:crypto.pad.Pkcs7
        })
    return encrypted.toString(crypto.enc.Utf8)
}

console.log(aesEncrypt('HELLO WORLD','0123456789abcdef','0123456789abcdef'))
console.log(aesDecrypt('u9CkJDGEw0frLa/SQ51GOg==','0123456789abcdef','0123456789abcdef'))