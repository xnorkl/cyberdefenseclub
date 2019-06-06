import socket
import base64
import os
from Crypto.Cipher import AES

port = 8081
host = "localhost"
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
msg = base64.b64encode(b'gitgud')
s.sendto(msg, (host, port))

def get_message():
    msg = input()
    return msg

def encryptmsg(key,msg):
    obj = AES.new('key123', AES.MODE_CFB, "This is an IV456")
    enc_msg = obj.encrypt(msg)
    return enc_msg

def get_transkey():
    os.urandom(16)



    
