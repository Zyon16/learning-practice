function o(n) {
    t = '',
    ['66', '72', '6f', '6d', '43', '68', '61', '72', '43', '6f', '64', '65']['forEach'](function(n) {
        t += unescape('%u00' + n)
    });
    var t, e = t;
    return String.fromCharCode(n)
}

function h(n, t) {
    t = t || u();
    for (var e = (n = n['split'](''))['length'], r = t['length'], a = 'charCodeAt', i = 0; i < e; i++)
        n[i] = o(n[i][a](0) ^ t[(i + 10) % r][a](0));
    return n['join']('')
}

function v(t) {
    t = encodeURIComponent(t)['replace'](/%([0-9A-F]{2})/g, function(n, t) {
        return o('0x' + t)
    });
    try {
        return btoa(t)
    } catch (n) {
        //return z[W1][K1](t)[U1](Z1)
        return Buffer['from'](t)['toString']('base64')
    }
}

function y(n, t, e) {
    for (var r = void 0 === e ? 2166136261 : e, a = 0, i = n['length']; a < i; a++)
        r = (r ^= n['charCodeAt'](a)) + ((r << 1) + (r << 4) + (r << 7) + (r << 8) + (r << 24));
    return t ? ('xyz' + (r >>> 0)['toString'](16) + 'abcd')['substr'](-16) : r >>> 0
}


function a_make(t){
    var r = new Date() - (-208||0) - 1661224081041
    var a = []
    Object.keys(t['params'])['forEach'](function(n) {
        if (n == 'analysis')
            return !1;
        t['params']['hasOwnProperty'](n) && a['push'](t['params'][n])
    })
    a = a['sort']()['join']('')
    a = v(a)
    a = (a += '@#' + t['url']['replace'](t['baseURL'], '')) + ('@#' + r) + ('@#' + 3)
    return a
}

function d_make(){
    return y('qimai@2022&Technology',1)
}

function get_analysis(t){
    return v(h(a_make(t),d_make()))
}

var t = {
    "url": "/rank/index",
    "method": "get",
    "headers": {
        "common": {
            "Accept": "application/json, text/plain, */*"
        },
        "delete": {},
        "get": {},
        "head": {},
        "post": {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        "put": {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        "patch": {
            "Content-Type": "application/x-www-form-urlencoded"
        }
    },
    "params": {
        "brand": "free",
        "device": "iphone",
        "country": "cn",
        "genre": "36",
        "date": "2022-11-20",
        "page": 2,
        "is_rank_index": 1,
        "snapshot": "19:42:05"
    },
    "baseURL": "https://api.qimai.cn",
    "transformRequest": [
        null
    ],
    "transformResponse": [
        null
    ],
    "timeout": 15000,
    "withCredentials": true,
    "xsrfCookieName": "XSRF-TOKEN",
    "xsrfHeaderName": "X-XSRF-TOKEN",
    "maxContentLength": -1,
    "maxBodyLength": -1
}

//console.log(a_make(t))
//console.log(get_analysis(t))

module.exports = {get:get_analysis}

