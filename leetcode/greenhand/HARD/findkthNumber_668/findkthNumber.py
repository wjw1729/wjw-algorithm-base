"""
author:wjw
分析：问题可以退化为在（m，n）的表中统计每个数出现的次数。
"""


class Solution:
    def findKthNumber(self, m, n, k):

        count = 0
        for i in range(1, m * n + 1):
            for j in range(1, m + 1):
                if i % j == 0 and (i // j) < n + 1:
                    count += 1

            if count >= k:
                return i


m = 3
n = 3
k = 5
m = 9895
n = 28405
k = 100787757
res = Solution().findKthNumber(m, n, k)
print(res)
