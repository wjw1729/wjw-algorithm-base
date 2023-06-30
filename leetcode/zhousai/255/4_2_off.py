"""
author:wjw
分析：取数+数组的划分。+递归。
"""


class Solution:
    def recoveryArray(self, n, sums):
        sums.sort()
        ans = []

        for i in range(n, 1, -1):
            d = sums[1] - sums[0]

            left = right = 0
            s, t = list(), list()
            used = set()

            while True:

                while left < (1 << i) and left in used:
                    left += 1

                if left == (1 << i):
                    break

                s.append(sums[left])
                used.add(left)

                while right in used or sums[right] != sums[left] + d:
                    right += 1

                t.append(sums[right])
                used.add(right)

            if 0 in s:
                ans.append(d)
                sums = s
            else:
                ans.append(-d)
                sums = t

        ans.append(sums[0] + sums[1])
        return ans


n = 3
sums = [-3, -2, -1, 0, 0, 1, 2, 3]
res = Solution().recoveryArray(n, sums)
print(res)
