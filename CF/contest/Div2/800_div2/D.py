from collections import deque


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

def solve():



    child=[[] for _ in range(n+1)]

    for i in range(2,n+1):
        child[p[i]].append(i)

    seq=[]
    q=deque()
    q.append(1)
    while q:
        u=q.popleft()
        seq.append(u)
        for v in child[u]:
            q.append(v)

    ans=[0]*(n+1)
    now=[0]*(n+1)

    for i in seq[::-1]:

        if len(child[i])==0:
            ans[i]=1
            now[i]=c[i][1]

        else:
            for v in child[i]:
                ans[i]+=ans[v]
                now[i]+=now[v]

        if now[i]>c[i][1]:
            now[i]=c[i][1]
        if now[i]<c[i][0]:
            now[i]=c[i][1]
            ans[i]+=1

    return ans[1]







t=int(input())
for _ in range(t):
    n=int(input())
    p=[0,0]+[int(x) for x  in input().split()]
    c=[[0,0]]
    for _ in range(n):
        c.append([int(x) for x  in input().split()])

    res=solve()
    print(res)



