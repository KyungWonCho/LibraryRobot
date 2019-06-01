import io

class book:
    full=""
    first=""
    second=""
    third=""
    idx=0
    def __init__(self, name, count):
        self.idx=count
        self.full=name
        i=0
        while i<len(name):
            if name[i]>'z':
                break
            i+=1
        self.first=name[0:i]
        self.second=name[i:]
        i=0
        while i<len(self.second):
            if self.second[i]=='v':
                break
            i+=1
        if i==len(self.second):
            return
        self.third=self.second[i:]
        self.second=self.second[:i]

def comp(a,b):
    if a.first==b.first:
        if b.first==b.second:
            return a.third>b.third
        return a.second>b.second
    else:
        return a.first>b.first
infofile = open('books.txt','r')

num=int(infofile.readline())

books=[]

for i in range(num):
    books.append(book(infofile.readline()[0:-1], i))

sorted_books=books[:]

for i in range(num):
    for j in range(0, num-i-1):
        if comp(sorted_books[j], sorted_books[j+1]):
            sorted_books[j], sorted_books[j+1] = sorted_books[j+1], sorted_books[j]

for i in range(num):
    books[sorted_books[i].idx].idx=i

for i in range(num):
    if (books[i].idx)==i:
        continue
    for j in range(i+1, num):
        if (books[j].idx)==i:
            print(j, '->', i)
            temp=books[j]
            del(books[j])
            books.insert(i, temp)
