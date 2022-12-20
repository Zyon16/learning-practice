
let crypto = require('crypto-js')

function parse(t) {
    const Sparse = function(t) {
        for (var e = t.length, n = [], r = 0; r < e; r++)
            n[r >>> 2] |= (255 & t.charCodeAt(r)) << 24 - r % 4 * 8;
        return n
    }
    return Sparse(unescape(encodeURIComponent(t)))
}

function vf(e){
    let a = 24,
        t = "0";
    if (e.length < a)
        for (let r = e.length; r < a; r++)
            e += t;
    else
        e = e.substring(0, a);
    return e
}

function getD(account){
    return {
        sigBytes:24,
        words:parse(vf(account))
    }
    
}

function desEntrypt(desMsg,desKey){
        const encrypted = crypto.TripleDES.encrypt(desMsg,desKey,{
            mode:crypto.mode.ECB,
            padding:crypto.pad.Pkcs7
        });
    return encrypted.toString()
}

function getPswd(account,pswd){
    return encodeURI(desEntrypt(pswd,getD(account)))
}


