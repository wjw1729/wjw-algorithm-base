class SegTree:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.total = 0
        self._left = self._right = None

    @property
    def mid(self):
        return (self.start + self.end) // 2

    @property
    def left(self):
        self._left = self._left or SegTree(self.start, self.mid)
        return self._left

    @property
    def right(self):
        self._right = self._right or SegTree(self.mid + 1, self.end)
        return self._right



    def update(self, l, r):

        if l <= self.start and self.end <= r:
            self.total = self.end-self.start+1

            return

        if l <= self.mid:
            self.left.update(l, r)
        if r > self.mid:
            self.right.update(l, r)

        self.total = self.left.total+ self.right.total

    def query(self):
        return self.total
