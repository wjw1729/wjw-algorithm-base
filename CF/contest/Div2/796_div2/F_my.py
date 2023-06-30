
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


class segtree:
    def __init__(self, a):
        self.a = a
        n = len(a)
        self.d = [0] * 4 * n
        self.b = [0] * 4 * n

    def build(self, s, t, p):

        if s == t:
            self.d[p] = self.a[s]
            return
        m = s + (t - s) // 2
        self.build(s, m, p * 2)
        self.build(m + 1, t, p * 2 + 1)
        self.d[p] = self.d[p * 2] + self.d[p * 2 + 1]

    # 区间修改
    def update(self, l, r, s, t, p):
        if l <= s and t <= r:
            self.d[p] = 0
            self.b[p] = 1
            return

        m = s + (t - s) // 2
        if self.b[p] and s != t:
            self.d[p * 2] = 0
            self.d[p * 2 + 1] = 0
            self.b[p * 2] = 1
            self.b[p * 2 + 1] = 1
            self.b[p] = 0

        if l <= m:
            self.update(l, r, s, m, p * 2)
        if r > m:
            self.update(l, r, m + 1, t, p * 2 + 1)

        self.d[p] = self.d[p * 2] + self.d[p * 2 + 1]

    # 区间查询
    def query(self, l, r, s, t, p):
        if l <= s and t <= r:
            return self.d[p]
        m = s + (t - s) // 2

        if self.b[p]:
            self.d[p * 2] = 0
            self.d[p * 2 + 1] = 0

            self.b[p * 2] = 1
            self.b[p * 2 + 1] = 1
            self.b[p] = 0

        res = 0
        if l <= m:
            res += self.query(l, r, s, m, p * 2)
        if r > m:
            res += self.query(l, r, m + 1, t, p * 2 + 1)
        return res


t = int(input())

for _ in range(t):
    n, m = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]

    c = [a[i] - b[i] for i in range(n)]

    segt = segtree(c)
    segt.build(0, n - 1, 1)
    check = True
    for _ in range(m):
        l, r = [int(x) for x in input().split()]
        l -= 1
        r -= 1
        tmp = segt.query(l, r, 0, n - 1, 1)
        if tmp != 0:
            check = False
            break
        else:
            segt.update(l, r, 0, n - 1, 1)

    if check:
        print('YES')
    else:
        print('NO')