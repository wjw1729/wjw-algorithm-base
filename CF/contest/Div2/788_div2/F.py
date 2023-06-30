import sys
sys.setrecursionlimit(2000)



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




mod = 10 ** 9 + 7
comb = [[-1] * (1001) for _ in range(1001)]


def nCi(n, i):
    if i == 0:
        comb[n][i] = 1
        return 1
    if n == 0:
        comb[n][i] = 0
        return 0
    if comb[n][i] != -1:
        return comb[n][i]

    comb[n][i] = (nCi(n - 1, i) + nCi(n - 1, i - 1)) % mod
    return comb[n][i]

for i in range(1001):
    nCi(1000,i)

def compute(x):
    f = [[-1 for _ in range(2001)] for _ in range(61)]

    def dfs(idx, k, r):
        if k > 2000:
            k = 2000
        if k < 0:
            return 0
        if idx == -1:
            return 1

        if f[idx][k] != -1:
            return f[idx][k]

        ans = 0
        cb = int((z & (1 << idx)) > 0)
        for i in range(cb, n + 1, 2):
            bcb = int((r & (1 << idx)) > 0)

            ans += nCi(n,i) * dfs(idx - 1, 2 * (k - i + bcb), r)
            ans %= mod

        f[idx][k] = ans
        return f[idx][k]

    res = dfs(60, 0, x)
    return res



n,l,r,z=[int(x) for x in input().split()]
ans = (compute(r) - compute(l - 1) + mod) % mod
print(ans)
