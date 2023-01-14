function guid() {
    function S4() {
          return (((1+Math.random())*0x10000)|0).toString(16).substring(1);
    }
    return (S4()+S4()+"-"+S4()+"-"+S4()+"-"+S4()+"-"+S4()+S4()+S4());
}

var client = new SekiroClient("ws://127.0.0.1:5620/business-demo/register?group=ths&clientId=" + guid());

client.registerAction("getCookie",function(request, resolve,reject ){
    resolve(encypt());
})