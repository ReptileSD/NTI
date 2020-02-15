import argparse
import socket
import time
from threading import Thread, Lock


class UdpServer(Thread):
    def __init__(self, udp_port, lock):
        Thread.__init__(self)
        self.lock = lock
        self.is_listening = True
        self.udp_port = int(udp_port)
        self.messages = list()

    def run(self):
        self.sock = socket.socket(socket.AF_INET,
                                  socket.SOCK_DGRAM)
        self.sock.bind(("0.0.0.0", self.udp_port))
        self.sock.setblocking(False)
        self.sock.settimeout(5)
        while self.is_listening:
            try:
                data, address = self.sock.recvfrom(1024)
                self.messages.append({address: data})
            except socket.timeout:
                continue
        self.stop()

    def stop(self):
        self.sock.close()


class TcpServer(Thread):
    def __init__(self, tcp_port, lock):
        Thread.__init__(self)
        self.clients = list()
        self.tcp_port = int(tcp_port)
        self.sock = socket.socket(socket.AF_INET,
                                  socket.SOCK_STREAM)
        self.sock.bind(('0.0.0.0', self.tcp_port))
        self.sock.listen(1)
        clients_listener = Thread(target=self.add_clients)
        clients_listener.start()
        self.lock = lock
        self.is_listening = True
        self.messages = list()

    def run(self):
        time_reference = time.time()
        while self.is_listening:
            if time.time() - time_reference >= 600:
                self.messages.clear()
            for conn, address in self.clients:
                data = conn.recv(1024)
                self.messages.append({address: data})
                if self.messages:
                    print(self.messages)
        self.stop()

    def add_clients(self):
        try:
            conn, address = self.sock.accept()
            self.clients.append((conn, address))
        except socket.timeout:
            pass

    def stop(self):
        self.sock.close()


def main_loop(tcp_port, udp_port):
    lock = Lock()
    udp_server = UdpServer(udp_port, lock)
    tcp_server = TcpServer(tcp_port, lock)
    udp_server.start()
    tcp_server.start()
    is_running = True
    while is_running:
        cmd = input()
        if cmd == "quit":
            print("Shutting down  server...")
            udp_server.is_listening = False
            tcp_server.is_listening = False
            is_running = False
    udp_server.join()
    tcp_server.join()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--tcp_port',
                        dest='tcp_port',
                        help='Listening tcp port',
                        default="5555")
    parser.add_argument('--udp_port',
                        dest='udp_port',
                        help='Listening udp port',
                        default="4444")
    args = parser.parse_args()
    main_loop(args.tcp_port, args.udp_port)
