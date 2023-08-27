import os
import socket
import json
from chatMessage import createChatMessage

def serverSocketUDP():
    
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

    # config.jsonよりパイプのアドレスの読みこみ
    config = json.load(open("config.json"))
    filepath = config['server_filepath']
    # すでにパイプが存在する場合は削除
    if os.path.exists(filepath):
        os.remove(filepath)
    # 名前付きパイプの作成
    os.mkfifo(filepath)

    server_address = filepath
    
    try:
        os.unlink(server_address)
    except FileNotFoundError:
        pass

    print('starting up on {}'.format(server_address))

    sock.bind(server_address)

    # 終了フラグ
    FLAG = True

    try:
        while FLAG:
            print("\nwaiting to receive message")
            # 受け取ったデータとパイプのアドレス
            data, address = sock.recvfrom(4096)

            # exitなら終了フラグを立てる
            if data == b"exit": FLAG = False

            # 受け取ったデータのバイト値とパイプのアドレス表示
            print('received {} bytes from {}'.format(len(data), address))
            
            # chat message
            message = createChatMessage().encode("utf-8")

            if data:
                sent = sock.sendto(message, address)
                print('sent {} bytes back to {}'.format(sent, address))
    except KeyboardInterrupt:
        os.remove(filepath)
        pass
    os.remove(filepath)


if __name__ == "__main__":
    serverSocketUDP()