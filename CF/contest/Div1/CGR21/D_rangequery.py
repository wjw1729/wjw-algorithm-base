#https://codeforces.com/contest/1696/submission/162281785
import sys
import os
from io import BytesIO, IOBase
from random import shuffle
from _collections import deque
import time

# region fastio
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


if sys.version_info[0] < 3:
    sys.stdin = BytesIO(os.read(0, os.fstat(0).st_size))
else:
    sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)

file = sys.stdin
if os.environ.get('USER') == "loic":
    file = open("data.in")

line = lambda: file.readline().split()
ui = lambda: int(line()[0])
ti = lambda: map(int, line())
li = lambda: list(ti())


#######################################################################

class RangeQueryIdx:
    def __init__(self, array, func, func_eq):
        limit = len(array)
        self.array = array
        self.func = func
        self.func_eq = func_eq
        self.row = limit.bit_length()
        self.tab = [[0 for _ in range(limit)] for _ in range(self.row)]

        self.tab[0] = list(range(limit))
        for e in range(1, self.row):
            for j in range(limit - 2 ** e + 1):
                self.tab[e][j] = self._apply_func(self.tab[e - 1][j], self.tab[e - 1][j + 2 ** (e - 1)])

    def _apply_func(self, l, r):
        val_l = self.array[l]
        val_r = self.array[r]
        if val_l == val_r:
            return self.func_eq(l, r)
        return l if self.func(val_l, val_r) == val_l else r

    ''' 
    l,r inclusive 
    returns the index where function is min/max
    '''

    def index(self, l, r):
        e = 0 if r - l == 0 else (r - l + 1).bit_length() - 1
        return self._apply_func(self.tab[e][l], self.tab[e][r - 2 ** e + 1])

    ''' l,r inclusive '''

    def query(self, l, r):
        return self.array[self.index(l, r)]


def nle(arr):
    res = [-1] * len(arr)

    q = deque()
    pos = 0
    while pos < len(arr):
        if q and arr[pos] < arr[q[-1]]:
            res[q[-1]] = pos
            q.pop()
        else:
            q.append(pos)
            pos += 1

    return res


def nge(arr):
    res = [-1] * len(arr)

    q = deque()
    pos = 0
    while pos < len(arr):
        if q and arr[pos] > arr[q[-1]]:
            res[q[-1]] = pos
            q.pop()
        else:
            q.append(pos)
            pos += 1

    return res


def solve():
    res = 0

    nxt_max = nge(A)
    nxt_min = nle(A)

    rq_min = RangeQueryIdx(A, min, min)
    rq_max = RangeQueryIdx(A, max, min)

    i = 0
    while i < N - 1:
        cur = A[i]
        nxt = A[i + 1]

        if nxt > cur:
            pos = nxt_min[i]
            idx = rq_max.index(i + 1, pos - 1 if pos != -1 else N - 1)
        else:
            pos = nxt_max[i]
            idx = rq_min.index(i + 1, pos - 1 if pos != -1 else N - 1)

        res += 1
        i = idx

    return str(res)


for test in range(1, ui() + 1):
    N = ui()
    A = li()

    print(solve())

file.close()