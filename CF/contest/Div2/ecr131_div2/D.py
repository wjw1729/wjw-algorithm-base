
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


def solve(a,p):
    check=False

    def dfs(i):
        nonlocal check

        if i==n:
            check=True
            return

        if check:
            return

        if a[i]!=0:
            dfs(i+1)

        for j in range(p[i][0],p[i][1]+1):
            if j not in vis:
                a[i]=j
                vis.add(j)
                dfs(i+1)
                if check:
                    return

                a[i]=0
                vis.remove(j)

    dfs(0)
    if check:
        return a


t=int(input())

for _ in range(t):
    n=int(input())
    b=[int(x) for x in input().split()]

    a=[0]*n
    p=[[1,n] for _ in range(n)]

    vis=set()
    for i in range(n):
        if b[i]==0:
            p[i][0]=i+2

        else:
            p[i][0]=(i+1)//(b[i]+1)+1
            p[i][1]=(i+1)//b[i]
            if p[i][0]==p[i][1]:
                a[i]=p[i][0]
                vis.add(a[i])
    res=solve(a,p)
    print(*res)




