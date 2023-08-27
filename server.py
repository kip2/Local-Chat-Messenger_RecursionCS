import os
import socket
from chatMessage import createChatMessage

def serverSocketUDP():
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

    server_address = './data/udp_socket_file'

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
        pass


if __name__ == "__main__":
    serverSocketUDP()