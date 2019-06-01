import socket
import io
import time

HOST='localhost'
PORT=5000
BUFSIZE=1024

sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(1)
conn, addr = sock.accept()

for i in range(5):

    imagedata=b''
    aaaa=conn.recv(4)
    print(aaaa)
    cnt=int((aaaa.decode('UTF-8')))

    while cnt:
        recvdata=conn.recv(BUFSIZE)
        imagedata+=recvdata
        cnt-=1

    with open('copyimage'+str(i)+'.jpg', 'wb') as inf:
        inf.write(imagedata)

    time.sleep(1)
    #process

senddata='seokminchul'.encode('UTF-8')
conn.send(senddata)

conn.close()
sock.close()
