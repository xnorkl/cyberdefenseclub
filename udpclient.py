import socket
import base64
port = 8081
host = "localhost"
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
msg = base64.b64encode(b'gitgud')
s.sendto(msg, (host, port))
