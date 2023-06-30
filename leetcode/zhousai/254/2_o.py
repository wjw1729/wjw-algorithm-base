"""
author:off
分析：重排.重排，将前(n+1)//2个数放到偶数位，将后面的数放到奇数位。
    时间复杂度：O（nlogn）
"""


class Solution:
    def rearrangeArray(self, nums):

        nums.sort()
        n = len(nums)

        re_nums = [0] * n
        for i in range(0, n, 2):
            re_nums[i] = nums[i // 2]

        for i in range(1, n, 2):
            re_nums[i] = nums[(n + 1) // 2 + (i - 1) // 2]
        return re_nums


nums = [1, 2, 3, 4, 5]
res = Solution().rearrangeArray(nums)
print(res)
