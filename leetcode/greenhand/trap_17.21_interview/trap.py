"""
author:wjw
分析：
"""


class Solution:
    def trap(self, height) -> int:
        n = len(height)
        ans = 0
        max_value = max(height)
        max_index = height.index(max_value)

        second_value_right = max(height[max_index + 1:])
        second_index_right = max_index + 1 + height[max_index + 1:].index(second_value_right)

        while second_index_right < n - 1:
            for i in range(max_index + 1, second_index_right):
                ans += second_value_right - height[i]
                print(second_value_right - height[i])

            max_value = second_value_right
            max_index = second_index_right

            second_value_right = max(height[max_index + 1:])
            second_index_right = max_index + 1 + height[max_index + 1:].index(second_value_right)

        max_value = max(height)
        max_index = height.index(max_value)

        second_value_left = max(height[:max_index - 1])
        second_index_left = height[:max_index - 1].index(second_value_left)

        while second_index_left > 0:
            for i in range(second_index_left, max_index):
                ans += second_value_left - height[i]
                print(second_value_left - height[i])

            max_value = second_value_left
            max_index = second_index_left

            second_value_left = max(height[:max_index])
            second_index_left = height[:max_index].index(second_value_left)

        return ans


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
res = Solution().trap(height)
print(res)
