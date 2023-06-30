class segtree:
    def __init__(self, start, end, m):
        self.m = m
        self.start = start
        self.end = end
        self.total = m
        self.t1 = m*(self.end-self.start+1)
        self._left = self._right = None

    @property
    def mid(self):
        return (self.start + self.end) // 2

    @property
    def left(self):
        self._left = self._left or segtree(self.start, self.mid, self.m)
        return self._left

    @property
    def right(self):
        self._right = self._right or segtree(self.mid + 1, self.end, self.m)
        return self._right

    def update(self, x, val):
        if x == self.start and self.end == x:
            self.total -= val
            self.t1 = self.total
            return

        if x <= self.mid:
            self.left.update(x, val)

        if x > self.mid:
            self.right.update(x, val)

        self.total = max(self.left.total, self.right.total)
        self.t1 = self.left.t1 + self.right.t1

    def query(self, val):
        if self.total >= val:
            if self.start == self.end:
                return self.start

            if self.left.total >= val:
                return self.left.query(val)

            elif self.right.total >= val:
                return self.right.query(val)

    def scater(self, mr):

        if self.end <= mr:
            return self.t1


        res=self.left.scater(mr)
        if self.right.start <= mr:
            res += self.right.scater(mr)

        return res


class BookMyShow:

    def __init__(self, n: int, m: int):
        self.m = m
        self.n = n
        self.ls = [m] * n
        self.segt = segtree(0, n - 1, m)

    def gather(self, k: int, maxRow: int):
        idx = self.segt.query(k)
        print(idx,'1')
        if idx == None or idx > maxRow:
            return []
        else:
            tmp = self.m - self.ls[idx]
            self.ls[idx] -= k
            self.segt.update(idx, k)

            return [idx, tmp]

    def scatter(self, k: int, maxRow: int) -> bool:

        tmp = self.segt.scater(maxRow)
        print(tmp)
        if tmp < k:
            return False


        while k>0:
            idx = self.segt.query(1)
            cs=min(self.ls[idx],k)
            self.segt.update(idx,cs)
            self.ls[idx]-=cs
            k-=cs

        return True

ops=["BookMyShow","scatter","gather","gather","gather","scatter"]
inps=[[5,9],[2,2],[7,2],[4,1],[6,2],[2,1]]

n=len(ops)
for i in range(n):
    if i==0:
        bms = BookMyShow(*inps[0])
    elif ops[i]=='gather':
        ans = bms.gather(*inps[i])
        print(ans)

    else:
        ans = bms.scatter(*inps[i])
        print(ans)




