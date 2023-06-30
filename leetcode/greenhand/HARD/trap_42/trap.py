"""
author:wjw
分析：
"""


class Solution:
    def trap(self, height):

        if height == []:
            return 0
        n = len(height)
        ans = 0

        max_height = max(height)
        max_height_index = height.index(max_height)

        max_height_index_left = max_height_index

        if max_height_index != n - 1:
            right = max(height[max_height_index + 1:])
            right_index = max_height_index + 1 + height[max_height_index + 1:].index(right)

        while max_height_index != n - 1 and right_index != n:

            for i in range(max_height_index + 1, right_index):
                ans += right - height[i]
                print(right - height[i])

            if right_index == n - 1:
                break
            max_height_index = right_index

            right = max(height[max_height_index + 1:])
            right_index = max_height_index + 1 + height[max_height_index + 1:].index(right)

        if max_height_index_left != 0:
            left = max(height[:max_height_index_left])
            left_index = height.index(left)

        while max_height_index_left != 0 and left != 0:
            for i in range(left_index, max_height_index_left):
                ans += left - height[i]
                print(left - height[i])

            if left_index == 0:
                break
            max_height_index_left = left_index
            left = max(height[:max_height_index_left])
            left_index = height.index(left)

        return ans


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
height = [4, 2, 0, 3, 2, 5]
height = [5, 2, 3, 0, 2, 4]
height = [1]
res = Solution().trap(height)
print(res)
