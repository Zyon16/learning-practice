let nodeRsa = require('node-rsa')

/**
 * 这里仅模拟网站登录表单加密情况
 * 登录时表单中某项加密（如密码password）
 * 数据传递到服务器后
 * 服务器根据保存的私钥解密，保证密码不被泄露
 * 因此这里的两个主要函数为 公钥加密和私钥解密
 */

//使用公钥加密
function rsaEncrypt(pub,msg){
    const pubKey = new nodeRsa(pub,'pkcs8-public')
    return pubKey.encrypt(msg,'base64')
}

//使用私钥解密
function rsaDecrypt(pri,msg){
    const priKey = new nodeRsa(pri,'pkcs8-private')
    return priKey.decrypt(msg,'utf8')
}

//生成密钥
const key = new nodeRsa({b:1024})
//导出公钥
const publicKey = key.exportKey('pkcs8-public')
//导出密钥
const privateKey = key.exportKey('pkcs8-private')
//待加密明文
let text = 'Hello World'
//加密明文
let enText = rsaEncrypt(publicKey,text)
//解密密文
let deText = rsaDecrypt(privateKey,enText)

console.log('公钥：'+publicKey)
console.log('私钥：'+privateKey)
console.log('密文：'+enText)
console.log('明文：'+deText)