import socketserver
import socket





class TCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        host, port = self.client_address

        print("{}:{} wrote:".format(host, port))
        print(self.data.decode())
        msg = input("type message: ")
        self.request.sendall(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = "localhost", 9998
    with socketserver.TCPServer((HOST, PORT), TCPHandler) as server:
        server.serve_forever()