import json
import socket
import os
import sys
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

    # config.jsonよりパイプのアドレスの読みこみ
    config = json.load(open("config.json"))
    server_filepath = config['server_filepath']
    client_filepath = config['client_filepath']


    server_address = server_filepath

    # すでにパイプが存在する場合は削除
    if os.path.exists(client_filepath):
        os.remove(client_filepath)

    address = client_filepath

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

def runClient():
    print("=========================")
    print("-------------------------")
    print("        CHAT  ROOM       ")
    print("-------------------------")
    print("=========================")
    print()

    print("Welcome to CHAT ROOM... ")
    print()
    sleep(1)

    name = input("Enter your name:")
    print("Your name is:", name)
    sleep(1)

    while True:
        message = input("Please write your message!: ")
        print("Your message is:", message)
        sleep(1)

        if message == "exit":
            clientSocketUDP(name, message)
            sys.exit()
        else: 
            clientSocketUDP(name, message)