
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

from collections import defaultdict

t=int(input())
for _ in range(t):
    n,q=[int(x) for x in input().split()]
    a=[int(x) for x in input().split()]

    def solve():
        im={c:i+1 for i,c in enumerate(a)}
        idxmap=defaultdict(list)
        ans=[0]*q
        for ii in range(q):
            i,k=[int(x) for x in input().split()]
            idxmap[k].append((ii,i))
        s=[0]*(n+1)
        pre=a[0]
        cnt=q
        for j in range(1,n):
            tmp=max(pre,a[j])
            s[im[tmp]]+=1
            if j in idxmap:
                for ii,i in idxmap[j]:
                    ans[ii]=s[i]
                    cnt-=1
            pre=tmp
            if pre==n:
                break
            if cnt==0:
                break
        if cnt>0:
            for k,v in idxmap.items():
                if k>j:
                    for ii,i in v:
                        if im[n]==i:
                            ans[ii]=s[i]+k-j
                        else:
                            ans[ii]=s[i]

        for c in ans:
            print(c)

    solve()


