import base64
import socket
from enum import Enum

p = 8081
m = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

class Verbosity(Enum):
    NONE = 0
    SOME = 1
    FULL = 2

def prompt(port):
    reply = "Receiving prompt on port {0}".format(port) 
    return reply

def bind_udp_port(port,maxbytes):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("",port))
    datagram = s.recvfrom(maxbytes)
    return datagram
    
def get_networkinfo(gram):
    # find network info from a message
    netinfo = gram[1]
    return netinfo

def decrypt_data(data):
    # take a byte, then decrypt & return a string
    msg = str(base64.b64decode(data))
    return msg

def format_message(datagram,verbosity):   
    # type checking
    if not isinstance(verbosity, Verbosity):
        raise TypeError('verbosity must be an instance of Verbosity')

    # flatten datagram and decrypt data
    data, addr = datagram
    ip, port = addr
    ip = ip.strip("'")
    msg = decrypt_data(data)
    text = msg[1:].strip("'") 
    if verbosity.value == 1:
        message = "{0}:{1} > {2}".format(ip,port,text)
    elif verbosity.value == 2:
        message = "{0}:{1} > {2}\n{3}".format(ip,port,text,data)
    else:
        message = "> {0}".format(text)
    return message

def gethex_data(msg):
    # take string and return the hex value 
    hex = ":".join("{:02x}".format(ord(c)) for c in msg)
    return hex

# use this for debugging for now
while 1:
    dgram = bind_udp_port(p,m)
    print(prompt(p))
    print(format_message(dgram, Verbosity.FULL))
    print(format_message(dgram, Verbosity.SOME))
    print(format_message(dgram, Verbosity.NONE))


