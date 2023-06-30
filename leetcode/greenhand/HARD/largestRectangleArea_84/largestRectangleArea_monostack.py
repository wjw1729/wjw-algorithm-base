"""
author；wjw
分析：使用两个单调栈维护i左边最近的小于高度heights[i]的栈和右边小于heights[i]的最近的。
"""


class Solution:
    def largestRectanleArea(self, heights):
        n = len(heights)

        left = [0] * n
        right = [0] * n

        mono_stack = []
        for i in range(n):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                mono_stack.pop()
            left[i] = mono_stack[-1] if mono_stack else -1
            mono_stack.append(i)

        mono_stack = []
        for i in range(n - 1, -1, -1):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                mono_stack.pop()
            right[i] = mono_stack[-1] if mono_stack else n
            mono_stack.append(i)

        ans = max([(right[i] - left[i] - 1) * heights[i] for i in range(n)])
        return ans


heights = [2, 1, 5, 6, 2, 3]
res = Solution().largestRectanleArea(heights)
print(res)
