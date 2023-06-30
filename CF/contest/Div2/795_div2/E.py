
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


class DisJoinUnion:
    def __init__(self,n):
        self.n=n
        self.parent=list(range(n))
        self.rank=[1]*n
        self.groups=n

    def find(self,x):
        if self.parent[x]==x:
            return x
        return self.find(self.parent[x])



    def union(self,x,y):
        fx,fy=self.find(x),self.find(y)

        if fx==fy:
            return

        if self.rank[fx]<self.rank[fy]:
            fx,fy=fy,fx

        self.rank[fx]+=self.rank[fy]
        self.parent[fy]=fx
        self.groups-=1



def findgroups(pls):
    pls.sort(key=lambda x:x[1])

    dsu = DisJoinUnion(n)


    hp=[[],[]]
    for c,l,r,i in pls:

        for j in hp[1-c]:
            if j[0]<l:
                continue

            dsu.union(j[1],i)

        if len(hp[1-c]):
            hp[1-c]=[max(hp[1-c])]


        hp[c].append((r,i))


    return dsu.groups





t=int(input())
for _ in range(t):
    n=int(input())
    pls=[]
    for i in range(n):
        c,l,r=[int(x) for x in input().split()]
        pls.append((c,l,r,i))


    res=findgroups(pls)
    print(res)
        