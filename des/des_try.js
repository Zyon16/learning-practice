let crypto = require('crypto-js')

function desEncrypt(desKey,desIv,desMsg){
    let key = crypto.enc.Utf8.parse(desKey),
        iv = crypto.enc.Utf8.parse(desIv),
        msg = crypto.enc.Utf8.parse(desMsg),
        encrypted = crypto.DES.encrypt(msg,key,{
            iv:iv,
            mode:crypto.mode.CBC,
            padding:crypto.pad.Pkcs7
        });
    return encrypted.toString()
}

console.log(desEncrypt('asd4a5d7adz','zxjgcjahsgbdhj','Hello World!'))
