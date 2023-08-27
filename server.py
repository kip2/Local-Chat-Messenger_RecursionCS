import os
import socket

def serverSocketUDP():
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

    server_address = './data/udp_socket_file'

    try:
        os.unlink(server_address)
    except FileNotFoundError:
        pass

    print('starting up on {}'.format(server_address))

    sock.bind(server_address)

    FLAG = True

    try:
        while FLAG:
            print("\nwaiting to receive message")

            data, address = sock.recvfrom(4096)

            if data == b"exit": FLAG = False

            print('received {} bytes from {}'.format(len(data), address))
            print(data)

            if data:
                sent = sock.sendto(data, address)
                print('sent {} bytes back to {}'.format(sent, address))
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    serverSocketUDP()