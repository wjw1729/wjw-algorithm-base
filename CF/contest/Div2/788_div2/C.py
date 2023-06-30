
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


class DisjoinUnion():
    def __init__(self,n):
        self.parent=list(range(n))
        self.rank=[1]*n

    def find(self,x):
        if self.parent[x]==x:
            return x
        else:
            return self.find(self.parent[x])

    def union(self,x,y):
        fx,fy=self.find(x),self.find(y)
        if fx==fy:
            return
        if self.rank[fx]<self.rank[fy]:
            fx,fy=fy,fx

        self.parent[fy]=fx
        self.rank[fx]+=self.rank[fy]


def numofpermutations(a,b,d):

    mod=10**9+7
    dsu=DisjoinUnion(n)
    vis=[0]*n
    sz=[0]*n

    for x,y in zip(a,b):
        dsu.union(x-1,y-1)

    for x in d:
        if x!=0:
            vis[dsu.find(x-1)]=1

    for i in range(n):
        sz[dsu.find(i)]+=1

    for i in range(n):
        if sz[dsu.find(i)]==1:
            vis[i]=1


    ans=1
    for i in range(n):
        if not vis[dsu.find(i)]:
            ans*=2
            ans%=mod
            vis[dsu.find(i)]=1




    return ans


t=int(input())

for _ in range(t):
    n=int(input())
    a=[int(x) for x in input().split()]
    b=[int(x) for x in input().split()]
    d=[int(x) for x in input().split()]

    res=numofpermutations(a,b,d)
    print(res)
