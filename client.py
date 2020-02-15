import threading
import socket


class Client:

    def __init__(self,
                 server_host,
                 server_port_tcp=5555,
                 server_port_udp=4444,
                 client_port_tcp=1235):
        self.server_message = []
        self.client_tcp = ("0.0.0.0", client_port_tcp)
        self.lock = threading.Lock()
        self.server_listener = SocketThread(self.client_tcp,
                                            self,
                                            self.lock)
        self.server_listener.start()
        self.server_udp = (server_host, server_port_udp)
        self.server_tcp = (server_host, server_port_tcp)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.connect(self.server_tcp)

    def send(self, message):
        self.server_socket.send(message.encode())

    def parse_data(self):
        print(self.get_messages())

    def get_messages(self):
        message = self.server_message
        self.server_message = []
        return set(message)


class SocketThread(threading.Thread):
    def __init__(self, addr, client, lock):
        threading.Thread.__init__(self)
        self.client = client
        self.lock = lock
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(addr)

    def run(self):
        while True:
            data, addr = self.sock.recvfrom(1024)
            self.lock.acquire()
            try:
                self.client.server_message.append(data)
            finally:
                self.lock.release()

    def stop(self):
        self.sock.close()


if __name__ == "__main__":
    client = Client('localhost')
    while True:
        pass
        # client.server_socket.send('lalala '.encode())
