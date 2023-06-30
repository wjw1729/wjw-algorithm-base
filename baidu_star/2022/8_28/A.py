
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
"""
class RangeQueryIdx:
    def __init__(self,array,func,func_eq):
        limit=len(array)
        self.array=array
        self.func=func
        self.func_eq=func_eq
        self.row=limit.bit_length()
        self.tab=[[0 for _ in range(limit)] for _ in range(self.row)]

        self.tab[0]=list(range(limit))

        for i in range(1,self.row):
            for j in range(limit-2**i+1):
                self.tab[i][j]=self._apply_func(self.tab[i-1][j],self.tab[i-1][j+2**(i-1)])


    def _apply_func(self,l,r):
        val_l=self.array[l]
        val_r=self.array[r]
        if val_l==val_r:
            return self.func_eq(l,r)

        return l  if self.func(val_l,val_r)== val_l else r


    def index(self,l,r):
        i=0 if r-l==0 else (r-l+1).bit_length()-1
        return self._apply_func(self.tab[i][l],self.tab[i][r-2**i+1])

    def query(self,l,r):
        return self.array[self.index(l,r)]
"""


n,q,k,xx=[int(x) for x in input().split()]
a=[int(x) for x in input().split()]

presum=[0]*(n+1)
for i in range(1,n+1):
    presum[i]=presum[i-1]+a[i-1]

b=[0]*(n-k+1)

for l in range(n-k+1):
    b[l]=int((presum[l+k]-presum[l])>=xx)


c=[0]*(n-k+2)
for i in range(1,n-k+2):
    c[i]=c[i-1]+b[i-1]
print(presum)
print(b)
print(c)

for _ in range(q):
    l,r=[int(x) for x in input().split()]
    l-=1
    r-=1
    if r-l+1<=k:
        #print(presum[r+1]-presum[l])
        if presum[r+1]-presum[l]>=xx:
            print('Y')
        else:
            print('N')
    else:
        ans=c[r+1-k+1]-c[l]
        #print(ans)
        if ans>0:
            print('Y')
        else:
            print('N')

