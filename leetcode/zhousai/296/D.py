class segtree:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.total = 0
        self.max = 0
        self._left = None
        self._right = None

    @property
    def mid(self):
        return (self.start + self.end) // 2

    @property
    def left(self):
        self._left = self._left or segtree(self.start, self.mid)
        return self._left

    @property
    def right(self):
        self._right = self._right or segtree(self.mid + 1, self.end)
        return self._right

    def update(self, l, r, val):
        if l == self.start and self.end == r:
            self.total += val
            self.max = self.total
            return

        if l <= self.mid:
            self.left.update(l, self.mid, val)
        if r > self.mid:
            self.right.update(self.mid + 1, r, val)

        self.max = max(self.left.max, self.right.max)

    def query(self):
        return self.max


class MyCalendarThree:

    def __init__(self):
        self.segt = segtree(0, 10 ** 9)

    def book(self, start: int, end: int) -> int:
        self.segt.update(start, end - 1, 1)

        return self.segt.query()


obj = MyCalendarThree()
param_1 = obj.book(10,20)
param_1 = obj.book(50,60)
print(param_1)