"""
author:wjw
分析：二分法+判断函数（判断x的序列是否>=k）
"""


class Solution:
    def findKthNumber(self, m, n, k):

        def afterk(x):
            count=(x//n)*n
            for i in range(x//n+1, m + 1):
                count += x//i

            return count >= k

        left, right = 1, m * n

        while left < right:
            mid = (left + right) // 2
            if afterk(mid):
                right = mid
            else:
                left = mid + 1

        return left


m = 3
n = 3
k = 5
res = Solution().findKthNumber(m, n, k)
print(res)
