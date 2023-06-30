from types import GeneratorType


def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to

    return wrappedfunc
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

import math

n = int(input())
g = [[] for _ in range(n)]
d = [-1] * n
ll = int(math.log2(n))
an = [[0] * (ll + 1) for _ in range(n)]


@bootstrap
def dfs(u, p):
    d[u] = d[p] + 1
    an[u][0] = p

    for i in range(1, ll + 1):
        an[u][i] = an[an[u][i - 1]][i - 1]

    for v in g[u]:
        if v == p:
            continue
        yield dfs(v, u)

    yield


def lca(u, v):
    if d[u] < d[v]:
        u, v = v, u

    for i in range(ll, -1, -1):
        if d[u] - d[v] >= 2 ** i:
            u = an[u][i]

    for i in range(ll, -1, -1):
        if an[u][i] != an[v][i]:
            u = an[u][i]
            v = an[v][i]

    return u if u == v else an[u][0]



def solve(k, p):
    p.sort(key=lambda x: -d[x])
    vis = set()
    m = len(p)

    for i in range(m):
        if lca(p[0], p[i]) == p[i]:
            vis.add(i)

    f = 0
    for i in range(m):
        if i in vis:
            f += 1
        else:
            break

    if f == m:
        return True

    for i in range(f, m):
        if lca(p[f], p[i]) == p[i]:
            vis.add(i)

    if len(vis) < m:
        return False

    return d[lca(p[0], p[f])] <= d[p[-1]]


for _ in range(n-1):
    u, v = [int(x) for x in input().split()]
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)


dfs(0,0)

q = int(input())
for _ in range(q):
    k = int(input())
    p = [int(x)-1 for x in input().split()]

    if solve(k, p):
        print('YES')
    else:
        print('NO')
