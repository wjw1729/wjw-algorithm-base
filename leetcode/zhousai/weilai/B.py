from sortedcontainers import SortedDict


class RangeModule:

    def __init__(self):
        self.d = SortedDict()

    def addRange(self, left: int, right: int) -> None:
        right = right - 1
        i = self.d.bisect_left(left - 1)

        while i < len(self.d) and self.d.values()[i] <= right + 1:
            r, l = self.d.items()[i]
            left = min(left, l)
            right = max(right, r)
            self.d.popitem(i)

        self.d[right] = left

    def queryRange(self, left: int, right: int) -> bool:
        right -= 1
        i = self.d.bisect_left(right)

        if i < len(self.d) and self.d.values()[i] <= left:
            return True
        else:
            return False

    def removeRange(self, left: int, right: int) -> None:
        right = right - 1
        i = self.d.bisect_left(left)
        if i >= len(self.d):
            return
        tmpl = self.d.values()[i]
        if tmpl > right:
            return

        while i < len(self.d) and self.d.keys()[i] <= right:
            self.d.popitem(i)

        if i < len(self.d):
            tmpr = self.d.keys()[i]
            self.d[tmpr] = max(right + 1, self.d[tmpr])

        if left - 1 >= tmpl:
            self.d[left - 1] = tmpl