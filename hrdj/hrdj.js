const crypto = require('crypto-js')

function getTime(){
    return (new Date()).getTime()
}

function P(n) {
    var e = [], t = "";
    for (var a in n)
        e.push(n[a]);
    for (var i = 0; i < e.length; i++)
        t += e[i] + "";
    return t += "JzyqgcoojMiQNuQoTlbR5EBT8TsqzJ", t
}

function S(n) {
    for (var e = Object.keys(n).sort(), t = {}, a = 0; a < e.length; a++)
        t[e[a]] = n[e[a]];
    return t
}

function md5(text){
    return crypto.MD5(text).toString()
}

function getSig(e){
    return md5(P(S(e)))
}

function k(text){
    return crypto.SHA256(text).toString()
}

function E(n, e) {
    return k("param=" + JSON.stringify(n) + "&timestamp=" + e + "&tenant=1&salt=" + 'kbn%&)@<?FGkfs8sdf4Vg1*+;`kf5ndl$')
}

function getParams(date) {
    params = {
        no:'dy009',
        data:{
            categoryName: "",
            days:1,
            dyCatName:"",
            startDay:date,
            type:1
        }
    }
    return params
}

function getSign(date){
    params = getParams(date)
    return E(params,new Date().getTime())
}

function getForm(account,pswd){
    let form = {
        phoneNum: account,
        pwd: md5(pswd),
        t: new Date().getTime().toString(),
        tenant: 1
    }

    form.sig = getSig(form)

    return form
}

console.log(E('{"no":"dy0009","data":{"days":1,"type":1,"dyCatName":"","categoryName":"","startDay":"2022-11-30"}}',1669875616353))
