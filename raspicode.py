import io
import socket
import time
from picamera import PiCamera
import serial

HOST, PORT, BUFSIZE = 'localhost', 5000, 1024

cam=PiCamera()
ser=serial.Serial('/dev/ttyACM0', 9600)
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

for i in range(4):
    ser.write(b'm')
    ser.write(str(i).encode('UTF-8'))
    time.sleep(5)
    
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

bcom=sock.recv(BUFSIZE)
com+=bcom.decode('UTF-8')
with open('books.txt','w') as inf:
    inf.write(com)

class book:
    first=''
    second=''
    third=''
    width=0
    idx=0
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

sorted_books=books[:]

for i in range(num):
    for j in range(0, num-i-1):
        if comp(sorted_books[j], sorted_books[j+1]):
            sorted_books[j], sorted_books[j+1] = sorted_books[j+1], sorted_books[j]

for i in range(num):
    books[sorted_books[i].idx].idx=i

x=0

for i in range(num):
    if (books[i].idx)==i:
        continue
    for j in range(i+1, num):
        if (books[j].idx)==i:
            print(j, '->', i)
            ser.write(b'm')
            ser.write(str(j).encode('UTF-8'))
            time.sleep((j-x)*4.5)
            ser.write(b'a')
            ser.write(str(books[j].width).encdoe('UTF-8'))
            time.sleep(3.5+books[j].width*0.5)
            ser.write(b'm')
            ser.write(b'4')
            time.sleep((4-j)*4.5)
            ser.write(b'b')
            time.sleep(4)
            ser.write(b'm')
            ser.write(str(i).encode('UTF-8'))
            time.sleep((4-i)*4.5)
            ser.write(b'a')
            ser.write(str(books[i].width).encdoe('UTF-8'))
            time.sleep(3.5+books[i].width*0.5)
            ser.write(b'm')
            ser.write(str(j).encode('UTF-8'))
            time.sleep((j-i)*4.5)
            ser.write(b'b')
            time.sleep(4)
            ser.write(b'm')
            ser.write(b'4')
            time.sleep((4-j)*4.5)
            ser.write(b'a')
            ser.write(str(books[j].width).encdoe('UTF-8'))
            time.sleep(3.5+books[j].width*0.5)
            ser.write(b'm')
            ser.write(str(i).encode('UTF-8'))
            time.sleep((4-i)*4.5)
            ser.write(b'b')
            time.sleep(4)
            temp=books[j]
            del(books[j])
            books.insert(i, temp)
    x=i

sock.close()
