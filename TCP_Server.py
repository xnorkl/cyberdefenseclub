import socket, sys

def listen(port):

	socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socket1.bind(("127.0.0.1", port))
	socket1.listen(1)
	connection, address = socket1.accept() #connection is socket object

	while 1:
		data = connection.recv(1024).decode()
		if not data:
			break
		print(">>>{}".format(data))

	connection.close()
	sys.exit()


listen(123)