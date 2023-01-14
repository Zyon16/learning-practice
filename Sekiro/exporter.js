function guid() {
    function S4() {
        return (((1 + Math.random()) * 0x10000) | 0).toString(16).substring(1);
    }

    return (S4() + S4() + "-" + S4() + "-" + S4() + "-" + S4() + "-" + S4() + S4() + S4());
}

var client = new SekiroClient("ws://127.0.0.1:5620/business-demo/register?group=ws-group-2&clientId=" + guid());

client.registerAction("clientTime", function (request, resolve, reject) {
    resolve("SekiroTest：" + new Date());
});

client.registerAction("executeJs", function (request, resolve, reject) {
    var code = request['code'];
    if (!code) {
        reject("need param:{code}");
        return;
    }

    code = "return " + code;

    console.log("executeJs: " + code);

    try {
        var result = new Function(code)();
        resolve(result);
    } catch (e) {
        reject("error: " + e);
    }

});