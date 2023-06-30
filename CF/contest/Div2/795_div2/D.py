
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

def maxgeqsum(a):
    for i in range(n-1):
        if a[i]>0 and a[i+1]>0:
            return False

    if all(x<=0 for x  in a):
        return True



    presum=[0]*(n+1)
    for i in range(1,n+1):
        presum[i]=presum[i-1]+a[i-1]



    posidx=[]
    for i in range(n):
        if a[i]>0:
            posidx.append(i)

    m=len(posidx)


    def judge(i,j):
        if max(a[i],a[j])<presum[j+1]-presum[i]:
            return False
        return True

    pre=[]
    for i in range(1,m):
        if not judge(posidx[i - 1], posidx[i]):
            return False
        for idx in pre:
            if not judge(idx,posidx[i]):
                return False

        if a[posidx[i-1]]>a[posidx[i]]:
            pre.append(posidx[i-1])






    return True



t=int(input())

for _ in range(t):
    n=int(input())
    a=[int(x) for x in input().split()]
    res=maxgeqsum(a)
    if res:
        print('YES')
    else:
        print('NO')
