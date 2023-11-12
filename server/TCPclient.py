import socket
import sys


HOST, PORT = "localhost", 9998

while True:
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
      # Connect to server and send data
        sock.connect((HOST, PORT))
        data = input("type message: ")
        sock.sendall(bytes(data + "\n", "utf-8"))
      
        # Receive data from the server and shut down
        received = str(sock.recv(1024), "utf-8")
        print("{}:{} sent: {}".format(HOST, PORT, data))
        print("Received from {}:{}: {}".format(received))