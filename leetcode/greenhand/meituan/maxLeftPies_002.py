"""
author:wjw
分析：逆序+成堆.
"""


class Solution:
    def maxLeftPiles(self, piles, pickout):
        n = len(piles)
        left = [i for i in range(n)]
        right = [i for i in range(n)]
        gather = [0] * n

        localmax = 0
        ans = []
        for pick in pickout[::-1]:
            index = pick - 1

            ans.append(localmax)

            l, r = index, index
            gather[index] = piles[index]

            if index - 1 >= 0 and gather[index - 1] > 0:
                gather[index] += gather[index - 1]
                l = left[index - 1]

            if index + 1 < n and gather[index + 1] > 0:
                gather[index] += gather[index + 1]
                r = right[index + 1]

            right[l] = r
            left[r] = l

            gather[l] = gather[index]
            gather[r] = gather[index]

            localmax = max(localmax, gather[index])

        return ans[::-1]


piles = [3, 2, 4, 4, 5]
pickout = [4, 3, 5, 2, 1]
res = Solution().maxLeftPiles(piles, pickout)
print(res)
