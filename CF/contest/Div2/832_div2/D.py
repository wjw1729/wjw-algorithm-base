from collections import defaultdict
import bisect


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



n, q = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

pre = [0] * (n + 1)
presum=[0]*(n+1)
idx=defaultdict(list)
for i in range(1, n + 1):
    pre[i] = pre[i - 1] ^ a[i - 1]

    tmp=(i-1)%2
    if idx[pre[i]]==[]:
        idx[pre[i]]=[[],[]]
    idx[pre[i]][tmp].append(i-1)
    presum[i]=presum[i-1]+a[i-1]



for _ in range(q):

    def solve():
        l, r = [int(x) for x in input().split()]
        l-=1
        r-=1
        if pre[r+1]^pre[l]!=0:
            print(-1)
        else:
            if (r-l+1)%2==1:
                if presum[r+1]-presum[l]==0:
                    print(0)
                else:
                    print(1)

            else:
                if presum[r+1]-presum[l]==0:
                    print(0)
                    return
                if a[l]==0 or a[r]==0:
                    print(1)
                    return
                c=pre[l]#[l,r]内奇数长度区间异或为0是否存在
                tmp = (l - 1) % 2
                j=bisect.bisect_right(idx[c][1-tmp],l-1)


                check= (idx[c][1-tmp][j]<=r) if j<len(idx[c][1-tmp]) else False

                if check:
                    print(2)
                else:
                    print(-1)

    solve()




