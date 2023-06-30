from functools import lru_cache
from collections import  defaultdict



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
        if x==self.parent[x]:
            return x
        return  self.find(self.parent[x])

    def union(self,x,y):
        fx,fy=self.find(x),self.find(y)

        if fx==fy:
            return

        if self.rank[fx]<self.rank[fy]:
            fx,fy=fy,fx
        self.parent[fy]=fx
        self.rank[fx]+=self.rank[fy]




mod = 998244353
f = [0] * 101
f[0] = 1


def fact(n):
    if f[n] != 0:
        return f[n]
    f[n] = n * f[n - 1]
    return f[n]


for i in range(101):
    fact(i)


def cni(n, i):
    return f[n] // (f[n - i] * f[i])


def solve(pls):
    #samecolor = [[False] * n for _ in range(n)]
    length = [[0] * n for _ in range(n)]

    for i in range(n):
        x0, y0 = pls[i]
        for j in range(i + 1, n):
            x1, y1 = pls[j]
            length[j][i] = length[i][j] = abs(x1 - x0) + abs(y1 - y0)


    dsu=DisJoinUnion(n)


    vis = set()


    for i in range(n):
        if i in vis:
            continue
        for j in range(i + 1, n):
            if j in vis:
                continue

            d0 = length[i][j]
            check = True
            tmp = set()
            for k in range(n):
                if k == i or k == j:
                    continue

                if length[i][k] == d0 == length[j][k]:
                    tmp.add(k)
                    continue

                if length[i][k] <= d0 or length[j][k] <= d0:
                    check = False
                    break

            if check:
                vis |= {i, j}
                vis |= tmp
                dsu.union(i,j)
                for c in tmp:
                    dsu.union(i,c)

    ols=defaultdict(int)
    for i in range(n):
        fi=dsu.find(i)
        if dsu.rank[fi]>1:
            ols[fi]+=1

    ols=list(ols.values())
    m=len(ols)
    res = sum(ols)

    ans = cni(n, n - res) * fact(n - res) % mod

    @lru_cache(None)
    def dfs(res,i):
        if i == m:
            return 1

        res1 = 0

        a = cni(res, 1)
        b = cni(res, ols[i]) * f[ols[i]]
        res -= 1
        res1 += a * dfs(res,i + 1)
        res += 1
        res -= ols[i]
        res1 += b * dfs(res,i + 1)
        res1 %= mod

        return res1

    ans *= dfs(res,0)
    ans %= mod

    return ans


n = int(input())

pls = []
for _ in range(n):
    pls.append([int(x) for x in input().split()])

res = solve(pls)
print(res)
