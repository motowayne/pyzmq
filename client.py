#!/usr/bin/env python
import zmq
import json
import inspect


def whoami():
    return inspect.stack()[1][3]

class ZmqClient():
    def __init__(self):
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect("tcp://localhost:5555")
        self.socket = socket

    def __del__(self):
        pass

    def start(self):
        print self.getPackEnvList()
        self.setPackEnv("Hisi3519")
        self.uploadLibs(["infile", "infile2"])
        self.pack()

    def createRequest(self, method, params={}):
        request = {"Method":method, "CID":1}
        if params:
            request.update(params)
        return request

    def sendRequest(self, method, params={}):
        request = self.createRequest(method, params)
        self.socket.send_json(request)
        reply = self.socket.recv()
        return reply

    def getPackEnvList(self):
        return self.sendRequest(whoami())

    def setPackEnv(self, packEnv):
        self.sendRequest(whoami(), {"Params":packEnv})

    def uploadLibs(self, files):
        request = self.createRequest(whoami())

        socket = self.socket
        socket.send_json(request, zmq.SNDMORE)
        for filename in files:
            with open(filename) as f:
                socket.send(f.read(), zmq.SNDMORE)

        socket.send("")
        socket.recv()

    def pack(self):
        pass

def main():
    client = ZmqClient()
    client.start()


if __name__ == '__main__':
    main()
