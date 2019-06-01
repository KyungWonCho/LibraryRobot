import io
import socket
import time
from picamera import PiCamera
import serial

HOST, PORT, BUFSIZE = 'localhost', 5000, 1024

cam=PiCamera()
#ser=serial.Serial('/dev/ttyACM0', 9600)
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

for i in range(5):
    '''
    ser.write(b'm')
    ser.write(b'100a')
    time.sleep(0.100)      ## 얼마나 기달리냐??
    '''
    cam.start_preview()
    time.sleep(1)
    cam.capture('image.jpg')
    cam.stop_preview()
    with open('image.jpg','rb') as inf:
        imagedata=inf.read()
    
    print(len(imagedata)/BUFSIZE)

    if len(imagedata)%BUFSIZE==0:
        if (len(imagedata)//BUFSIZE)<1000:
            sock.sendall(('0'+str(len(imagedata)//BUFSIZE)).encode('UTF-8'))
        else:
            sock.sendall(str(len(imagedata)//BUFSIZE).encode('UTF-8'))
    else:
        if (len(imagedata)//BUFSIZE+1)<1000:
            sock.sendall(('0'+str(len(imagedata)//BUFSIZE+1)).encode('UTF-8'))
        else:
            sock.sendall(str(len(imagedata)//BUFSIZE+1).encode('UTF-8'))
    while imagedata:
        senddata=imagedata[:BUFSIZE]
        imagedata=imagedata[BUFSIZE:]
        sock.sendall(senddata)
'''
bcom=sock.recv(BUFSIZE)
com+=bcom.decode('UTF-8')

with open('books.txt','w') as inf:
    inf.write(com)
'''
class book:
    first=''
    second=''
    third=''
    width=0             # 아마도 width는 모터 회전수 기준으로??
    def __init__(self, first, second, third, width):
        self.first=first
        self.second=second
        self.third=third
        self.width=width

def comp(a, b):
    if a.first==a.second:
        if b.first==b.second:
            return c.first<c.second
        return b.first<b.second
    return a.first<a.second

database=open('data.txt', 'r')

datanum=int(database.readline())
datamap=dict()

for i in range(datanum):
    data=database.readline()
    datal=data.split()
    print(len(datal))
    if len(datal)==4:
        bookdata=book(datal[1], datal[2], '', int(datal[3]))
    else:
        bookdata=book(datal[1], datal[2], datal[3], int(datal[4]))
    datamap[datal[0]]=bookdata

bookinfo=open('books.txt','r')
num=int(bookinfo.readline())
books=[]

for i in range(num):
    books.append(datamap[(bookinfo.readline())[0:-1]])

for a in books:
    print(a.first, a.second, a.third, a.width)
'''
for i in range(num):
    ser.write(b'm')
    ser.write(b'0a')
    for j in range(0, num-i-1):
        if comp(books[j], books[j+1]):
            ser.write(b'm')
            pos=0
            for k in range(0, j):
                pos+=books[k].width
            ser.write((str(pos)+'a').encode('UTF-8'))
            delay(pos)      ## 얼마나 기달리냐??
            ser.write(b'o')
            ser.write((str(books[j].width)+'a').encode('UTF-8'))
            delay(1000)     ## 열려라 참깨
            ser.write(b'p')
            delay(3000)     ## 움직여라!
            ser.write(b'm')
            pos+=books[j].width+books[j+1].width
            ser.write((str(pos)+'a').encode('UTF-8'))
            delay(books[j].width+books[j+1].width)       ## 얼마나 기달리냐???
            ser.write(b'q')
            ser.write((str(books[j].width)+'a').encode('UTF-8'))        ## 벌려
            delay(1000)
            ser.write(b'r')                             ##넣어
            delay(3000)
            books[j], books[j+1] = books[j+1], books[j]
'''
sock.close()
