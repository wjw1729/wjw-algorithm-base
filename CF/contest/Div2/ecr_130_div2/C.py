
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



def acnum(s):

    ca=[0]*(s.count('a'))
    cc=[0]*(s.count('c'))

    bnum=0
    i=0
    j=0
    for c in s:
        if c=='a':
            ca[i]=bnum
            i+=1
        elif c=='b':
            bnum+=1

        else:
            cc[j]=bnum
            j+=1

    return ca,cc





def solve():
    cnt1=[0]*3
    cnt2=[0]*3

    for c in s:
        cnt1[ord(c)-ord('a')]+=1

    for c in t:
        cnt2[ord(c)-ord('a')]+=1

    if cnt1!=cnt2:
        return False

    ss=s.replace('b','')
    tt=t.replace('b','')
    if ss!=tt:
        return False


    sa,sc=acnum(s)
    ta,tc=acnum(t)

    if all(sa[i]<=ta[i] for i in range(len(sa))):
        pass
    else:
        return  False

    if all(sc[i]>=tc[i] for i  in range(len(sc))):
        pass
    else:
        return False

    return True








q=int(input())

for _ in range(q):
    n=int(input())
    s=input()
    t=input()

    res=solve()
    if res:
        print('YES')
    else:
        print('NO')
