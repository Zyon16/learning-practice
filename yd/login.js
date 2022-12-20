const crypto = require('crypto-js')

function getForm(account,pswd){
    return {
        action:'login',
        txtusername: account,
        txtpassword: crypto.MD5(pswd).toString()
    }
}