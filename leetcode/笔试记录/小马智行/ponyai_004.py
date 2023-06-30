"""
author:wjw
分析：单调栈。存储与每个点与(0,h)的斜率。
时间复杂度:O(n)

"""


n, h = [int(x) for x in input().strip().split()]

heights = [int(x) for x in input().strip().split()]


class Solution:
    def maxOccluder(self, n, h, heights):
        def slope(i):
            return (heights[i] - h) / (i + 1)

        lines = []
        stack = []
        ans = []
        for i in range(n):
            k = slope(i)
            lines.append(k)
            while stack and lines[stack[-1]] < k:
                stack.pop()
            if not stack:
                ans.append(0)
            else:
                ans.append(stack[-1] + 1)
            stack.append(i)

        return ans


res = Solution().maxOccluder(n, h, heights)
for i in res:
    print(i)
