
// 1
!function(){
    const ws = new WebSocket('ws://127.0.0.1:7788');
    window.wsHook = ws;
    ws.onopen = function(e){
        ws.send('CONNECTED')    //建议注释
    }
    ws.onmessage = function(e){
        ws.send(JSON.stringify(n.body))
    }
}();


//2 推荐
//放在代码头部
!function(){
    const ws = new WebSocket('ws://127.0.0.1:7788');
    window.wsHook = ws;
    ws.onopen = function(e){
        ws.send('CONNECTED')
    }
}();

//放在解密代码后
window.wsHook.send(JSON.stringify(n.body))
