import os
from client import runClient
from server import runServer

if __name__ == "__main__":
    pid = os.fork()

    if pid == 0:
        runServer()
    else:
        runClient()
