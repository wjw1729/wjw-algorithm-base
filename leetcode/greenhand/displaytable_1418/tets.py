from sortedcontainers import SortedList

from sortedcontainers import SortedList

import math


class Solution:
    def nthSuperUglyNumber(self, n: int, primes) -> int:
        res = []
        search_ls = SortedList([1])

        while len(res) < n:
            next_ugly = search_ls.pop(0)
            res.append(next_ugly)
            for prime in primes:
                new = next_ugly * prime
                if new not in search_ls:
                    search_ls.add(new)

        return res[n - 1]


n = 12
prime = [2, 7, 13, 19]
# n=10
# prime=[2,5,7,11,13,17,23,29,43,53]
res = Solution().nthSuperUglyNumber(n, prime)
print(res)
