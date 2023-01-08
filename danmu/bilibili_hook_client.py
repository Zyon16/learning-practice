import asyncio
# encoding: utf-8
import asyncio
import websockets


async def echo(websocket):
    # 使用WebSocket在客户端和服务器之间建立全双工双向连接后，就可以在连接打开时调用send()方法。
    message = 'CONNECTED'
    # 发送数据
    await websocket.send(message)
    return True


async def recv_msg(websocket):
    while 1:
        # 接收数据
        recv_text = await websocket.recv()
        print(recv_text)


async def main_logic(websocket, path):
    # await echo(websocket)
    await recv_msg(websocket)


start_server = websockets.serve(main_logic, '127.0.0.1', 7788)
loop = asyncio.get_event_loop()
loop.run_until_complete(start_server)
loop.run_forever()
