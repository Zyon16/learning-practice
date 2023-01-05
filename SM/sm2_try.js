const sm2 = require('sm-crypto').sm2

let keypair = sm2.generateKeyPairHex()

publicKey = keypair.publicKey // 公钥
privateKey = keypair.privateKey // 私钥

// 默认生成公钥 130 位太长，可以压缩公钥到 66 位
const compressedPublicKey = sm2.compressPublicKeyHex(publicKey) // compressedPublicKey 和 publicKey 等价
sm2.comparePublicKeyHex(publicKey, compressedPublicKey) // 判断公钥是否等价

// 自定义随机数，参数会直接透传给 jsbn 库的 BigInteger 构造器
// 注意：开发者使用自定义随机数，需要自行确保传入的随机数符合密码学安全
//let keypair2 = sm2.generateKeyPairHex('123123123123123')
//let keypair3 = sm2.generateKeyPairHex(256, SecureRandom)

let verifyResult = sm2.verifyPublicKey(publicKey) // 验证公钥
verifyResult = sm2.verifyPublicKey(compressedPublicKey) // 验证公钥

console.log(verifyResult)

const cipherMode = 1 // 1 - C1C3C2，0 - C1C2C3，默认为1

msgString = 'HELLO WORLD'

let encryptData = sm2.doEncrypt(msgString, publicKey, cipherMode) // 加密结果
let decryptData = sm2.doDecrypt(encryptData, privateKey, cipherMode) // 解密结果

console.log(encryptData)
console.log(decryptData)

//encryptData = sm2.doEncrypt(msgArray, publicKey, cipherMode) // 加密结果，输入数组
//decryptData = sm2.doDecrypt(encryptData, privateKey, cipherMode, {output: 'array'}) // 解密结果，输出数组
