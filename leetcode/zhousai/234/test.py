class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:

        def minsum(x):

            if x + index - n + 1 >= 1:
                right = (2 * x + index - n + 1) * (n - index) // 2
            else:
                right = (x + 1) * x // 2 + (n - x - index)

            if x - index >= 1:
                left = (2 * x - index) * (index + 1) // 2
            else:
                left = (1 + x) * x // 2 + index + 1 - x

            return left + right - x

        ans=minsum(3)

        return ans

n = 4
index = 2
maxSum = 6
res=Solution().maxValue(n,index,maxSum)
print(res)

