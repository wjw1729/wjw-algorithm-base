"""
author:wjw
分析：a==b,则意味着arr[i]^...^arr[k]=0,且i~k之间j的取值有k-i种。
"""


class Solution:
    def countTriplets(self, arr) -> int:
        n = len(arr)
        ans = 0
        for i in range(n):
            window = 0
            for j in range(i, n):
                window = window ^ arr[j]
                if window == 0:
                    ans += j - i

        return ans


arr = [2, 3, 1, 6, 7]
# arr = [1, 1, 1, 1, 1]
arr = [2, 3]
arr = [1, 3, 5, 7, 9]
res = Solution().countTriplets(arr)
print(res)
