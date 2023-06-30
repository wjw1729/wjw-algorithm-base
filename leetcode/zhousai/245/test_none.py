from functools import lru_cache


class Solution:
    def findIntegers(self, n: int) -> int:

        @lru_cache(None)
        def odd(i):
            if i == 1:
                return 1

            if i == 0:
                return 0

            if '11' not in bin(i+1) and i % 2 == 0:
                return even(i >> 1) - 1
            else:
                return even(i >> 1)

        @lru_cache(None)
        def even(i):
            if i == 0:
                return 1
            if i == 1:
                return 1

            return odd(i >> 1) + even(i >> 1)

        return (odd(n) , even(n))


res = Solution().findIntegers(2)
print(res)
