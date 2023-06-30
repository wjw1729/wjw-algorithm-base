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


t = int(input())
for _ in range(t):
    def solve():
        n, m = [int(x) for x in input().split()]
        mat = []
        cnt = 0
        for i in range(n):
            mat.append([int(x) for x in input().split()])
            cnt += mat[i].count(1)

        if cnt % n != 0:
            return -1, []

        t = cnt // n

        col = [set() for _ in range(m)]

        row = [set() for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    col[j].add(i)
                else:
                    row[i].add(j)

        ans = []

        for i in range(n):

            if len(row[i]) > t:
                cnt1 = len(row[i]) - t
                tmp = set()
                for j in row[i]:
                    for ii in col[j]:
                        if len(row[ii]) < t:
                            ans.append((i, ii, j))
                            # row[i].remove(j)
                            tmp.add(j)
                            col[j].remove(ii)
                            row[ii].add(j)
                            cnt1 -= 1
                            break
                    if cnt1 == 0:
                        break
                for x in tmp:
                    row[i].remove(x)

        return 1, ans


    res = solve()

    if res[0] == -1:
        print(-1)
    else:
        print(len(res[1]))
        for x in res[1]:
            print(*[y + 1 for y in x])
