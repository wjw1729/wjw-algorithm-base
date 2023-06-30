"""
author:wjw
分析：xor_sum表示当前list的异或和，每次取数取不等于xor_sum的数，直到无法再取。返回取数次数，奇偶判断。
optimal:优化版，更合理点
"""


class Solution:
    def xorGame(self, nums) -> bool:
        xor_sum = 0
        for i in range(len(nums)):
            xor_sum = xor_sum ^ nums[i]

        ans = 0
        while xor_sum != 0:
            for i in range(len(nums)):
                if nums[i] != xor_sum:
                    xor_sum = xor_sum ^ nums[i]
                    nums.pop(i)
                    ans += 1
                    break
                if i == len(nums) - 1:
                    xor_sum = xor_sum ^ nums[i]
                    nums.pop(i)
                    ans += 1

        if ans % 2 == 1:
            return False
        else:
            return True


nums = [1, 1, 1, 2]
res = Solution().xorGame(nums)
print(res)
