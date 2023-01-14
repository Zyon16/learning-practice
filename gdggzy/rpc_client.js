window.rpcClient.registerAction("getPost", function (request, resolve, reject) {
    let pageNum = request.page;
    if(!pageNum){
        pageNum = 1;
    }

    const c = 'k8tUyS$m',
        l = window.lK(16),
        a = Date.now(),
        formData = {
            dataType:"",
            openConvert:true,
            pageNo:pageNum,
            pageSize:10,
            projectType:"",
            publishEndTime:"",
            publishStartTime:"",
            secondType:"A",
            siteCode:"44",
            thirdType:"",
            total:0,
            type:"trading-type"
        },
        d = window.Sg({
            p: window.QC.stringify(FormData, {
                allowDots: !0
            }),
            t: a,
            n: l,
            k: c
        });

    resolve(JSON.stringify({
        "headers":{
            "X-Dgi-Req-Nonce":l,
            "X-Dgi-Req-Signature":d.toString(),
            "X-Dgi-Req-Timestamp":a
        },
        "form":formData
    }))

});