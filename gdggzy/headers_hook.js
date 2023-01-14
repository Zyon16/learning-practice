var code = function(){
    var org = window.XMLHttpRequest.prototype.setRequestHeader;
    window.XMLHttpRequest.prototype.setRequestHeader = function(k,v){
        if(k == 'X-Dgi-Req-Signature' || k == 'X-Dgi-Req-Nonce'){
            debugger;
        }
        return org.apply(this,arguments);
    }
}
var script = document.createElement('script');
script.textContent = '('+code+')()';
(document.head||document.documentElement).appendChild(script);
script.parentNode.removeChild(script);

const a = Date.now(),
    l = lK(16),
    c = sr([8, 28, 20, 42, 21, 53, 65, 6]);

const d = Sg({
    p: QC.stringify(o.data, {
        allowDots: !0
    }),
    t: a,
    n: l,
    k: c
});

