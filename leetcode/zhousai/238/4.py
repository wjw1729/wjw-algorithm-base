"""
author:wjw
分析：更新restrictions中的高度限制信息。推导之间的最大高度关系式。
时间复杂度:O(mlogm)。直接做在时间和空间复杂度上都会超出。
"""


class Solution:
    def maxBuilding(self, n: int, restrictions) -> int:

        m = len(restrictions)

        heighthash = {}

        for i, h in restrictions:
            heighthash[i - 1] = h

        left = {}
        indexs = list(heighthash.keys())
        indexs.sort()

        for i in range(m):
            if i == 0:
                left[indexs[i]] = min(indexs[i], heighthash[indexs[i]])
            else:
                left[indexs[i]] = min(left[indexs[i - 1]] + indexs[i] - indexs[i - 1], heighthash[indexs[i]])

        right = {}

        for i in range(m - 1, -1, -1):
            if i == m - 1:
                right[indexs[i]] = heighthash[indexs[i]]
                continue
            right[indexs[i]] = min(right[indexs[i + 1]] + indexs[i + 1] - indexs[i], heighthash[indexs[i]])

        for idx in indexs:
            heighthash[idx] = min(left[idx], right[idx])

        best = 0
        for i in range(m):
            if i == 0:
                best = max(best, (heighthash[indexs[i]] + indexs[i]) // 2)
            else:
                best = max(best, (heighthash[indexs[i]] + heighthash[indexs[i - 1]] + indexs[i] - indexs[i - 1]) // 2)

        if n - 1 not in heighthash:
            best = max(best, heighthash[indexs[-1]] + n - 1 - indexs[-1] if indexs else n - 1)
        return best


n = 10
restrictions = [[5, 3], [2, 5], [7, 4], [10, 3]]
n = 5
restrictions = [[2, 1], [4, 1]]
n = 6
restrictions = []
res = Solution().maxBuilding(n, restrictions)
print(res)
