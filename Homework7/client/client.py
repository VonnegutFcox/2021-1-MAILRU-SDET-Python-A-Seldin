import socket
import json
import settings


class Client:
    def __init__(self, host, port):
        self.port = port
        self.host = host
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.settimeout(0.1)
        self.client.connect((host, int(port)))

    def method_post(self, request):
        self.client.send(request)

    def method_get(self):
        total = []
        while True:
            if data := self.client.recv(4096):
                total.append(data.decode())
            else:
                self.client.close()
                break
        data = ''.join(total).splitlines()
        return data
