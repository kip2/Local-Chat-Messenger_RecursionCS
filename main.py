import sys
from client import clientSocketUDP
from server import serverSocketUDP
from time import sleep

if __name__ == "__main__":
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