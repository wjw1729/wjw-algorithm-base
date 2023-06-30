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





def canfindpath(x,indeg):

    q=deque()

    d=[0]*(n+1)

    ans = 0
    for i in range(1,n+1):
        if indeg[i]==0 and a[i-1]<=x:
            q.append(i)
            d[i]=1
            ans=max(ans,d[i])

    def toplogsort(q,indeg):
        nonlocal  ans
        while q:
            u = q.popleft()

            for v in g[u]:
                if a[v - 1] > x:
                    continue
                indeg[v]-=1
                if d[u] + 1 > d[v]:
                    d[v] = d[u] + 1
                    ans=max(ans,d[v])
                    q.append(v)
                if indeg[v] < 0:
                    d[v] = float('inf')
                    ans=float('inf')
                    return

    toplogsort(q,indeg[:])
    for i in range(1,n+1):
        if d[i]>0 or a[i-1]>x:
            continue
        q=deque()
        q.append(i)
        d[i]=1
        ans=max(ans,d[i])
        toplogsort(q,indeg[:])
        if ans>=k:
            return True



    return ans>=k







n,m,k=[int(x) for x in input().split()]
a=[int(x) for x  in input().split()]
g=[[] for _ in range(n+1)]
indeg=[0]*(n+1)

for _ in range(m):
    u,v=[int(x) for x in input().split()]
    g[u].append(v)
    indeg[v]+=1


l=min(a)
r=max(a)

ans=-1
while l<=r:
    mid=(l+r+1)//2
    if canfindpath(mid,indeg[:]):
        ans=mid
        r=mid-1
    else:
        l=mid+1

print(ans)