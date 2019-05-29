import socket
import io
import time
from picamera import PiCamera

HOST='localhost'
PORT=5005
BUFSIZE=1024

sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

print('connected')

with open('image.jpg','rb') as inf:
    imagedata=inf.read()

print('image loaded')

try:
    if len(imagedata)%BUFSIZE==0:
        sock.sendall(str(len(imagedata)//BUFSIZE).encode('UTF-8'))
    else:
        sock.sendall(str(len(imagedata)//BUFSIZE+1).encode('UTF-8'))
    while imagedata:
        senddata=imagedata[:BUFSIZE]
        imagedata=imagedata[BUFSIZE:]
        sock.sendall(senddata)
    print('sended')

    com=sock.recv(BUFSIZE)
    print(com.decode('UTF-8'))

    sock.close()
except:
    print('error')
    sock.close()

