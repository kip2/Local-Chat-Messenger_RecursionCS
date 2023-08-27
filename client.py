import socket
import os
from time import sleep
from chatMessage import createClientMessage

def waitingMessage():
    print("   .   ")
    print("   .   ")
    print("   .   ")
    sleep(1)
    print("Receive message!")
    print()
    sleep(1)

def clientSocketUDP(name, message):

    sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

    server_address = './data/udp_socket_file'

    address = './data/udp_client_socket_file'

    sock.bind(address)


    # clientのチャットメッセージを作成
    message = createClientMessage(name, message)

    try:
        print("\n=== sending message ===")
        print(message)
        print("=== sending message ===\n")

        sent = sock.sendto(message.encode('utf-8'), server_address)

        print("waiting to receive")
        data, server = sock.recvfrom(4096)

        # メッセージを受け取りにインタラクティブさを出すために数秒まつ
        waitingMessage()

        # 受け取ったメッセージを表示する
        print("======= received message ========")
        print(data.decode("utf-8"))
        print("======= received message ========\n")
    except ConnectionRefusedError:
        print("No response from the server.")
    finally:
        sock.close()
        os.remove(address)
