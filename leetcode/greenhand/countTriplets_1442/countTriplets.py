"""
author:wjw
分析：三指针，空间复杂度低，时间复杂度高。空间复杂度低
"""


class Solution:
    def countTriplets(self, arr) -> int:
        n = len(arr)
        ans = []
        for i in range(n):

            a = 0

            for j in range(i + 1, n):
                a = a ^ arr[j - 1]

                b = 0
                for k in range(j, n):
                    b = b ^ arr[k]

                    if a == b:
                        ans.append([i, j, k])

        return len(ans)


arr = [1, 1, 1, 1, 1]
arr = [1, 3, 5, 7, 9]
arr = [2, 3]
arr = [7, 11, 12, 9, 5, 2, 7, 17, 22]
res = Solution().countTriplets(arr)
print(res)
