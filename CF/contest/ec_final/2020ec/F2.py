
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

n1,n2=[int(x) for x  in input().split()]

xls=defaultdict(list)
yls=defaultdict(list)
res1=['0']*n1
res2=['0']*n2

for i in range(n1):
    x,y=[int(x) for  x in input().split()]
    xls[x].append((y,i))
    yls[y].append((x,i))

for i in range(n2):
    x, y = [int(x) for x in input().split()]
    xls[x].append((y, i+n1))
    yls[y].append((x, i+n1))


for k,v in xls.items():
    v.sort()

    for i in range(1,len(v)):
        if v[i][1]<n1 and v[i-1][1]>=n1:
            res1[v[i][1]]='1'
            res2[v[i-1][1]-n1]='1'
        if v[i][1]>=n1 and v[i-1][1]<n1:
            res2[v[i][1]-n1]='1'
            res1[v[i-1][1]]='1'


for k,v in yls.items():
    v.sort()

    for i in range(1,len(v)):
        if v[i][1]<n1 and v[i-1][1]>=n1:
            res1[v[i][1]]='1'
            res2[v[i-1][1]-n1]='1'
        if v[i][1]>=n1 and v[i-1][1]<n1:
            res2[v[i][1]-n1]='1'
            res1[v[i-1][1]]='1'


print(''.join(res1))
print(''.join(res2))


