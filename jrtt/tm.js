// ==UserScript==
// @name         今日头条-RPC
// @namespace    https://sz134055.github.io/
// @version      0.1
// @description  今日头条-RPC
// @author       sz134055
// @match        https://www.toutiao.com/*
// @icon         https://sz134055.github.io/images/avatar.png
// @grant        none
// @require      https://sekiro.virjar.com/sekiro-doc/assets/sekiro_web_client.js
// ==/UserScript==

(function() {
    'use strict';
    function guid() {
        function S4() {
            return (((1 + Math.random()) * 0x10000) | 0).toString(16).substring(1);
        }
    
        return (S4() + S4() + "-" + S4() + "-" + S4() + "-" + S4() + "-" + S4() + S4() + S4());
    }
    
    var client = new SekiroClient("ws://127.0.0.1:5620/business-demo/register?group=jrtt&clientId=" + guid());

    client.registerAction("getUrl", function (request, resolve, reject) {
        var channelId = request.channel;
        if (!channelId){
            channelId = 0;
        }
        var urlParams = {
            url:'https://www.toutiao.com/api/pc/list/feed?min_behot_time='+Math.round(new Date().getTime()/1000)+'&refresh_count=5&category=pc_profile_recommend&aid=24&app_name=toutiao_web&channel_id='+channelId
        }


        resolve(""+urlParams.url+"&_signature="+window.byted_acrawler.sign(urlParams));
    });
    
})();