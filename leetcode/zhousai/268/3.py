from collections import defaultdict
class RangeFreqQuery:

    def __init__(self, arr):
        self.pre = [defaultdict(int)]
        total = defaultdict(int)

        for num in arr:
            total[num] += 1
            self.pre.append(total.copy())

    def query(self, left: int, right: int, value: int) -> int:
        print(self.pre[right + 1][value])
        print(self.pre[left][value])
        return self.pre[right + 1][value] - self.pre[left][value]


rangeFreqQuery = RangeFreqQuery([12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56])
print(1)

