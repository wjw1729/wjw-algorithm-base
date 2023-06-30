from collections import defaultdict

# ---------------------------------------- fast io ----------------------------------------
import os, sys
from io import BytesIO, IOBase

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")
# ---------------------------------------- fast io ----------------------------------------

class binaryindextree:
    def __init__(self,n):
        self.n=n
        self.c=[0]*(1+n)

    def lowbit(self,x):
        return x&-x

    def update(self,x,val):

        while x<self.n+1:
            self.c[x]+=val
            x+=self.lowbit(x)

    def query(self,x):
        res=0
        while x>0:
            res+=self.c[x]
            x-=self.lowbit(x)

        return res



n,q=[int(x) for  x in input().split()]
row=defaultdict(int)
col=defaultdict(int)
rbint=binaryindextree(n)
cbint=binaryindextree(n)

for _ in range(q):
    qry=[int(x) for x  in input().split()]

    if qry[0]==1:
        if row[qry[1]]==0:
            rbint.update(qry[1],1)
        if col[qry[2]]==0:
            cbint.update(qry[2],1)
        row[qry[1]]+=1
        col[qry[2]]+=1


    elif qry[0]==2:
        row[qry[1]] -= 1
        col[qry[2]] -= 1

        if row[qry[1]]==0:
            rbint.update(qry[1],-1)
        if col[qry[2]]==0:
            cbint.update(qry[2],-1)

    else:

        x0,y0,x1,y1=qry[1:]

        check=(x1-x0+1==(rbint.query(x1)-rbint.query(x0-1))) or (y1-y0+1==(cbint.query(y1)-cbint.query(y0-1)))

        if check:
            print('YES')
        else:
            print('NO')

