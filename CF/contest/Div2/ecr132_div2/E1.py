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


n = int(input())
a = [int(x) for x in input().split()]

g = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = [int(x) for x in input().split()]
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)

ans = 0

f = [set() for _ in range(n)]
used = [False] * n

stack = deque()
stack.append((0, -1))
routes = [0]
while stack:
    u, p = stack.pop()
    for v in g[u]:
        if v != p:
            stack.append((v, u))
            routes.append(v)

for pos in routes[::-1]:
    f[pos].add(a[pos])
    for npos in g[pos]:
        if not used[npos]:
            continue

        find = False
        for x in f[npos]:
            if x in f[pos]:
                find = True
                ans += 1
                break
        if find:
            f[pos] = set()

            break
        for x in f[npos]:
            f[pos].add(x ^ a[pos])


    used[pos] = True

print(ans)
