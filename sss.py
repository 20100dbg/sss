import asyncore
import socket

class EchoHandler(asyncore.dispatcher_with_send):

    def handle_read(self):
        data = self.recv(8192)
        if data:
            self.send(data)

class EchoServer(asyncore.dispatcher):

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)

    def handle_accept(self):
        pair = self.accept()
        if pair is not None:
            sock, addr = pair
            print 'Incoming connection from %s' % repr(addr)
            handler = EchoHandler(sock)

server = EchoServer('localhost', 8080)
asyncore.loop()



hote = 'localhost'
port = 31337


#type_message
#1 : handshake
#2 : message
#3 : ping
#4 : disconnect

if not server:
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((hote, port))
	
	while True:
	    data = sock.recv(1024)

	sock.close()



def handle_data(data):

	tab = data.split('|')

	if tab[0] == 1: #handshake
		return

	if tab[0] == 2: #message
		return
	
	if tab[0] == 3: #ping
		return
	
	if tab[0] == 4: #disconnect
		return
	