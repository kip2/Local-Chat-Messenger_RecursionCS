import sys
from client import clientSocketUDP
from server import serverSocketUDP

if __name__ == "__main__":
    print("=========================")
    print("-------------------------")
    print("        CHAT  ROOM       ")
    print("-------------------------")
    print("=========================")

    name = input("Enter your name:")
    while True:
        message = input("Write your message!:> ")
        if message == "exit":
            clientSocketUDP(name, message)
            sys.exit()
        else: 
            clientSocketUDP(name, message)