import socket
import io
import time

HOST='localhost'
PORT=5005
BUFSIZE=1024

sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(1)
conn, addr = sock.accept()

print('accepted')

imagedata=b''

cnt=int((conn.recv(BUFSIZE)).decode('UTF-8'))

while cnt:
    recvdata=conn.recv(BUFSIZE)
    if recvdata==b'':
        break
    imagedata+=recvdata
    cnt-=1

print('image recieved')

with open('copyimg.jpg', 'wb') as inf:
    inf.write(imagedata)

print('command send')
senddata='seokminchul'.encode('UTF-8')
conn.send(senddata)

conn.close()
sock.close()
