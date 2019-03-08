import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((hote, port))

while True:
    data = sock.recv(1024)

sock.close()