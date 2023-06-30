from sortedcontainers import SortedList


class Solution:
    def shortestSequence(self, rolls, k: int) -> int:

        f = [0 for _ in range(k)]
        sl = SortedList()
        for i, c in enumerate(f):
            sl.add((c, i))

        for c in rolls[::-1]:
            l ,i= sl[0][0]

            if l == f[c - 1]:
                tmp = f[c - 1] + 1
                sl.remove((tmp - 1, c - 1))
                sl.add((tmp, c - 1))
                f[c-1]+=1

        return min(f) + 1
