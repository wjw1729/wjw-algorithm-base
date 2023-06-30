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

class binaryTree:
    def __init__(self,n):
        self.c=[0]*(n+1)
        self.n=n

    def lowbit(self,x):
        return x &-x

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



n,m,q=[int(x) for  x in input().split()]

matrix=[]
total=0
for _ in range(n):
    matrix.append(list(input()))
    total+=matrix[-1].count('*')


bint=binaryTree(m*n)


for j in range(m):
    for i in range(n):
        if matrix[i][j]=='*':
            idx=j*n+i+1
            bint.update(idx,1)


for _ in range(q):
    x,y=[int(x) for x in input().split()]
    x-=1
    y-=1
    idx = y * n + x + 1
    if matrix[x][y]=='*':
        matrix[x][y]='.'
        bint.update(idx,-1)
        total-=1
    else:
        bint.update(idx,1)
        matrix[x][y]='*'
        total+=1

    res=total-bint.query(total)

    print(res)
