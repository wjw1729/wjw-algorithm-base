"""
author:wjw
分析：从后往前找到第一个非逆序index，将nums[index:]调整为比当前大的最小排列.
    for example:  [1,3,5,4,2]中，index为3的索引，比当前大的最小排列为4235，（比3大的最小数4提前，其他数按顺序排列即可）
"""
import bisect


class Solution:
    def nextPermutation(self, nums):
        n = len(nums)

        if nums == sorted(nums, reverse=True):
            nums.sort()
        else:

            for i in reversed(range(n - 1)):
                if nums[i] < nums[i + 1]:
                    index = i
                    indexnum = nums[i]
                    break

            temp = sorted(nums[index:])
            next_index = bisect.bisect_right(temp, indexnum)
            head = temp.pop(next_index)
            nums[index:] = [head] + temp


nums = [3, 2, 1]
Solution().nextPermutation(nums)
print(nums)
