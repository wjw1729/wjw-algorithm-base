"""
author:wjw
分析：找到最大值，以此为起点，像右寻找第二大的值，计算区间内需要的填水量。直到右边处理完。对左半边同理。
"""


class Solution:
    def trap(self, height) -> int:
        n = len(height)
        ans = 0

        if height == []:
            return ans
        max_value = max(height)
        max_index = height.index(max_value)

        while max_index < n - 1:
            second_value_right = max(height[max_index + 1:])
            second_index_right = max_index + 1 + height[max_index + 1:].index(second_value_right)
            for i in range(max_index + 1, second_index_right):
                ans += second_value_right - height[i]
                print(second_value_right - height[i])

            max_index = second_index_right

        max_value = max(height)
        max_index = height.index(max_value)
        while max_index > 0:
            second_value_left = max(height[:max_index])
            second_index_left = height[:max_index].index(second_value_left)

            for i in range(second_index_left, max_index):
                ans += second_value_left - height[i]
                print(second_value_left - height[i])

            max_index = second_index_left

        return ans


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
height = [2, 1, 2]
res = Solution().trap(height)
print(res)
