import socket
import base64
# pick a port to accept UDP datagrams and define a buffer size
port = 8081
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# bind the port
s.bind(("", port))
reply = "waiting on port: {0}".format(port)
print(reply)

while 1:
    # accept up to 1024 bytes per datagram
    data, addr = s.recvfrom(1024)
    # decode the message and store it as a string
    msg = str(base64.b64decode(data))
    #hex = ":".join("{:02x}".format(ord(c)) for c in msg)
    # parse the address
    ip, port = addr
    # make our answer readable
    msg = str(msg)
    msg = msg[1:].strip("'")
    ip.strip("'")
    answer = "Received {0} from {1}:{2}".format(msg,ip,port)
    print(answer)

