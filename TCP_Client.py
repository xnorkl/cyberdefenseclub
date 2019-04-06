import socket, sys


def connect(hostname, port):

	socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socket1.connect((hostname, port))

	while 1:
		data = input(">>>")  # must be encoded before sent to server
		if data == "exit":
			break
		else:
			socket1.sendall(data.encode())

	socket1.close()
	sys.exit()


connect("127.0.0.1", 123)