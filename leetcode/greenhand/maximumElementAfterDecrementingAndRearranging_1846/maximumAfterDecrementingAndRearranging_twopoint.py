"""
author:wjw
分析：单指针传递。
"""


class Solution:
    def maximumAfterDecrementingAndRearranging(self, arr):
        arr.sort()
        n = len(arr)
        maxvalue = 1
        for i in range(1, n):
            if not (arr[i] == arr[i - 1] and arr[i] <= maxvalue):
                maxvalue += 1

        return maxvalue


arr = [1, 5, 5, 5, 5, 5, 5, 5]
res = Solution().maximumAfterDecrementingAndRearranging(arr)
print(res)
