"""
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
class binaryindexTree3:
    def __init__(self,n):
        self.c=[0]*(n+1)
        self.a=[0]*(n+1)
        self.n=n

    def lowbit(self,x):
        return x & -x

    def update(self,x,val):
        self.a[x]=val

        while x<self.n+1:
            self.c[x]=max(self.c[x],val)
            x+=self.lowbit(x)

    def query(self,l,r):
        res=self.a[r]
        while r>=l:
            res=max(res,self.a[r])
            r-=1
            while r-self.lowbit(r)>=l:
                r-=self.lowbit(r)
                res=max(self.c[r],res)

        return res


class intervaltreemin:
    def __init__(self, a):
        self.a = a
        n = len(a)
        self.d = [0] * 4 * n
        self.build(0,n-1,1)

    # 递归建树
    def build(self, s, t, p):  # (s,t为原数组中的区间，p为二叉树节点编号)

        if s == t:
            self.d[p] = self.a[s]
            return
        m = s + (t - s) // 2
        self.build(s, m, p * 2)
        self.build(m + 1, t, p * 2 + 1)
        self.d[p] = min(self.d[p * 2], self.d[p * 2 + 1])

    # 区间查询
    def query(self, l, r, s, t, p):
        if l <= s and t <= r:
            return self.d[p]
        m = s + (t - s) // 2

        res = float('inf')
        if l <= m:
            res = min(self.query(l, r, s, m, p * 2), res)
        if r > m:
            res = min(res, self.query(l, r, m + 1, t, p * 2 + 1))
        return res


class intervaltreemax:
    def __init__(self, a):
        self.a = a
        n = len(a)
        self.d = [0] * 4 * n
        self.build(0, n - 1, 1)

    def build(self, s, t, p):  # (s,t为原数组中的区间，p为二叉树节点编号)

        if s == t:
            self.d[p] = self.a[s]
            return
        m = s + (t - s) // 2
        self.build(s, m, p * 2)
        self.build(m + 1, t, p * 2 + 1)
        self.d[p] = max(self.d[p * 2], self.d[p * 2 + 1])

    # 区间查询
    def query(self, l, r, s, t, p):
        if l <= s and t <= r:
            return self.d[p]
        m = s + (t - s) // 2

        res = -float('inf')
        if l <= m:
            res = max(self.query(l, r, s, m, p * 2), res)
        if r > m:
            res = max(res, self.query(l, r, m + 1, t, p * 2 + 1))
        return res


def friends(a, b):

    segta = intervaltreemax(a)
    segtb = binaryindexTree3(n)
    for i in range(n):
        #segta.update(i+1,a[i])
        segtb.update(i+1,-b[i])

    for l in range(n):
        for r  in range(l,n):
            print(l,r,-segtb.query(l+1,r+1))




    ans = 0
    for i in range(n):
        l = i
        r = n - 1
        lans = -1
        while l <= r:
            mid = (l + r + 1) // 2
            tmp = segta.query(i, mid,0,n-1,1) + segtb.query(i+1, mid+1)
            if tmp >= 0:
                r = mid - 1
                if tmp == 0:
                    lans = mid
            else:
                l = mid + 1

        if lans != -1:
            l = i
            r = n - 1
            rans = -1
            while l <= r:
                mid = (l + r + 1) // 2
                tmp = segta.query(i, mid,0,n-1,1) + segtb.query(i+1, mid+1)
                if tmp > 0:
                    r = mid - 1
                else:
                    l = mid + 1
                    if tmp == 0:
                        rans = mid

            if rans != -1:
                ans += rans - lans + 1

    return ans


n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

res = friends(a, b)
print(res)
