## Sekiro
[官方文档](https://sekiro.virjar.com/sekiro-doc/index.html)

API：
- 查看分组列表：http://127.0.0.1:5620/business-demo/groupList

- 查看分组下队列状态：http://127.0.0.1:5620/business-demo/clientQueue?group=test
    - group参数：需要查看的指定分组名

- 调用转发：http://127.0.0.1:5620/business-demo/invoke?group=test&action=test&param=testparm
    - group参数：同上
    - action参数：需要调用的action名
    - param参数：需要传递的参数，注意这里param是自定义的参数名！也就是说在`action`参数后可以接比如`sign`，Sekiro客户端可以拿到此参数

当前目录下 [sk-rpc](./sk-rpc/) 即为需要用的Sekiro服务端文件
- [sekiro.bat](./sk-rpc/bin/sekiro.bat)为CMD下服务端启动文件
- [sekiro.sh](./sk-rpc/bin/sekiro.sh)为BASH下服务端启动文件

要退出服务端，请按 CTRL+C

[JsClient.js](./JsClient.js) 为客户端注入文件

[exporter.js](./exporter.js) 为暴露RPC服务的代码

[DEMO.html](./DEMO.html)为测试文件，确保服务端打开情况下使用浏览器打开，会启用一个`rpc-test`的`group`，注册的`action`有`clientTime`


