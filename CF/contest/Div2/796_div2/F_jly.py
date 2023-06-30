

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
        self.parent=list(range(n))
        self.rank=[1]*n

    def find(self,x):
        while x!=self.parent[x]:
            self.parent[x]=self.parent[self.parent[x]]
            x=self.parent[x]
        return x

    def union(self,x,y):
        fx,fy=self.find(x),self.find(y)
        if fx==fy:
            return

        self.parent[fy]=fx
        self.rank[fx]+=self.rank[fy]



t = int(input())

for _ in range(t):
    n, m = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]

    sa=[0]*(n+1)
    sb=[0]*(n+1)
    for i in range(1,n+1):
        sa[i]=sa[i-1]+a[i-1]
        sb[i]=sb[i-1]+b[i-1]

    dsu=DisJoinUnion(n+2)

    l=[0]*m
    r=[0]*m
    deg=[2]*m
    g=[[] for _ in range(n+1)]

    for i in range(m):
        l[i],r[i]=[int(x) for x in input().split()]
        l[i]-=1
        g[l[i]].append(i)
        g[r[i]].append(i)

    def dfs(i):
        dsu.union(i+1,i)

        for j in g[i]:
            deg[j]-=1
            if deg[j]==0:
                x=dsu.find(l[j])
                while x<=r[j]:
                    dfs(x)
                    x=dsu.find(x)


    for i in range(n+1):
        if sa[i]==sb[i]:
            dfs(i)

    if dsu.find(0)==n+1:
        print('YES')
    else:
        print('NO')






