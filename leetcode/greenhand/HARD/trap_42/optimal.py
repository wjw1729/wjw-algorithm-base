"""
author:wjw
分析：左右两边具有对称性，将右半边反转，之后极为左半边的情况。定义求取左半边积水的函数即可
pre记录在该点前的最大值。
"""


def watersum(height):
    n = len(height)
    if n < 2:
        return 0
    ans = 0
    pre = height[0]
    for i in range(1, n):
        if height[i] < pre:
            ans += pre - height[i]
        else:
            pre = height[i]
    return ans


class Solution:
    def trap(self, height):
        n = len(height)
        ans = 0

        if n == 0:
            return 0

        max_height = max(height)
        max_index = height.index(max_height)

        h1 = height[:max_index + 1]
        h2 = list(reversed(height[max_index:]))

        ans += watersum(h1)
        ans += watersum(h2)

        return ans


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# height = [4, 2, 0, 3, 2, 5]
# height = [5, 2, 3, 0, 2, 4]

res = Solution().trap(height)
print(res)
