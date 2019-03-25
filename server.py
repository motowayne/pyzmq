#!/usr/bin/env python
import zmq

class ZmqServer():
    def __init__(self):
        context = zmq.Context()
        socket = context.socket(zmq.REP)
        socket.bind("tcp://*:5555")
        self.socket = socket

    def __del__(self):
        pass

    def start(self):
        socket = self.socket
        packEnv = ""
        while True:
            message = socket.recv_json()
            print "Receive message %s"%message
            reply = []
            if message["Method"] == "getPackEnvList":
                reply = ["S3LM", "HiSi3519"]
            elif message["Method"] == "setPackEnv":
                packEnv = message["Params"]
                print "Select pack env %s"%packEnv
            elif message["Method"] == "uploadLibs":
                count = 0
                while True:
                    message = socket.recv()
                    if not message:
                        print "Receive end!"
                        break
                    count += 1
                    with open("outfile%s"%count, "wb") as f:
                        f.write(message)
            socket.send(str(reply))


def main():
    server = ZmqServer();
    server.start()


if __name__ == '__main__':
    main()
