
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





n = int(input())
a = [int(x) for x in input().split()]
g = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = [int(x) for x in input().split()]
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)

rootxorsum = [-1] * n
rootxorsum[0] = a[0]
stack = [(0, -1)]
routes = [0]
used = [False] * n

while stack:
    u, p = stack.pop()
    if rootxorsum[u] == -1:
        rootxorsum[u] = rootxorsum[p] ^ a[u]

    for v in g[u]:
        if v == p:
            continue
        stack.append((v, u))
        routes.append(v)

ans = 0
f = [set() for _ in range(n)]
for pos in routes[::-1]:
    f[pos].add(rootxorsum[pos])

    for npos in g[pos]:
        if not used[npos]:
            continue

        if len(f[pos]) < len(f[npos]):
            f[pos], f[npos] = f[npos], f[pos]
        find = False
        for x in f[npos]:
            if x ^ a[pos] in f[pos]:
                find = True
                ans += 1
                break
        f[pos] |= f[npos]
        if find:
            f[pos] = set()
            break

    used[pos] = True

print(ans)
