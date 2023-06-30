
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

class segtree:
    def __init__(self,start,end):
        self.start=start
        self.end=end
        self.cnt=self.total=0
        self._left=self._right=None

    @property
    def mid(self):
        return (self.start+self.end)//2

    @property
    def left(self):
        self._left=self._left or segtree(self.start,self.mid)
        return self._left

    @property
    def right(self):
        self._right=self._right or segtree(self.mid+1,self.end)
        return self._right


    def pushup(self):
        if self.cnt>0:
            self.total=plsx[self.end+1]-plsx[self.start]
        else:
            self.total =self.left.total+self.right.total


    def update(self,l,r,val):
        if l<=self.start and self.end<=r:
            self.cnt+=val
            self.pushup()
            return

        if l<=self.mid:
            self.left.update(l,r,val)

        if r>self.mid:
            self.right.update(l,r,val)

        self.pushup()


n=int(input())
plsx=set()


edges=[]
for _ in range(n):
    x1,y1,x2,y2=[int(x) for x  in input().split()]
    plsx.add(x1)
    plsx.add(x2)
    edges.append((y1,x1,x2,1))
    edges.append((y2,x1,x2,-1))

plsx=list(plsx)
plsx.sort()
pxmap={c:i for i,c  in enumerate(plsx)}
edges.sort()

m=len(plsx)
segt=segtree(0,m-1)
ans=0
pre=None
for y,x1,x2,k in edges:
    if pre!=None:
        ans+=(y-pre)*length
    segt.update(pxmap[x1],pxmap[x2]-1,k)
    length=segt.total

    pre=y

print(ans)














