import io
import socket
import time
from picamera import PiCamera
import serial

HOST, PORT, BUFSIZE = 'localhost', 5000, 1024
'''
cam=PiCamera()
ser=serial.Serial('/dev/ttyACM0', 9600)
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

time.sleep(10)
for i in range(3):
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
'''
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
    if a.first==b.first:
        if a.second==b.second:
            return a.third<b.third
        return a.second<b.second
    return a.first<b.first

database=open('data.txt', 'r')

datanum=int(database.readline())
datamap=dict()

print('read database')

for i in range(datanum):
    data=database.readline()
    print(data[0:-1])
    datal=data.split()
    if len(datal)==4:
        bookdata=book(datal[1], datal[2], '', int(datal[3]))
    else:
        bookdata=book(datal[1], datal[2], datal[3], int(datal[4]))
    datamap[datal[0]]=bookdata

print('read books')

bookinfo=open('books.txt','r')
num=int(bookinfo.readline())
print(num)
books=[]

for i in range(num):
    x=(bookinfo.readline())[0:-1]
    books.append(datamap[x])
    print(x, books[i].first, books[i].second, books[i].third)
    books[i].idx=i

sorted_books=books[:]

for i in range(num):
    for j in range(0, num-i-1):
        if not comp(sorted_books[j], sorted_books[j+1]):
            sorted_books[j], sorted_books[j+1] = sorted_books[j+1], sorted_books[j]

for i in range(num):
    books[sorted_books[i].idx].idx=i
    print(sorted_books[i].first, sorted_books[i].second, sorted_books[i].third)

x=0

for i in range(num):
    if (books[i].idx)==i:
        continue
    for j in range(i+1, num):
        if (books[j].idx)==i:
            print(j, '->', i)
            '''
            ser.write(b'm')
            ser.write(str(j).encode('UTF-8'))
            time.sleep((j-x)*4.5)
            ser.write(b'a')
            ser.write(str(books[j].width).encode('UTF-8'))
            time.sleep(6+books[j].width*0.5)
            ser.write(b'm')
            ser.write(b'3')
            time.sleep((3-j)*4.5)
            ser.write(b'b')
            time.sleep(6)
            ser.write(b'm')
            ser.write(str(i).encode('UTF-8'))
            time.sleep((3-i)*4.5)
            ser.write(b'a')
            ser.write(str(books[i].width).encode('UTF-8'))
            time.sleep(6+books[i].width*0.5)
            ser.write(b'm')
            ser.write(str(j).encode('UTF-8'))
            time.sleep((j-i)*4.5)
            ser.write(b'b')
            time.sleep(6)
            ser.write(b'm')
            ser.write(b'3')
            time.sleep((3-j)*4.5)
            ser.write(b'a')
            ser.write(str(books[j].width).encode('UTF-8'))
            time.sleep(6+books[j].width*0.5)
            ser.write(b'm')
            ser.write(str(i).encode('UTF-8'))
            time.sleep((3-i)*4.5)
            ser.write(b'b')
            time.sleep(6)
            '''
            temp=books[j]
            del(books[j])
            books.insert(i, temp)
            break
    x=i

#sock.close()
