"""
author:wjw
分析：xor_sum表示当前list的异或和，每次取数取不等于xor_sum的数，直到无法再取。返回取数次数，奇偶判断。
"""


class Solution:
    def xorGame(self, nums) -> bool:

        xor_sum = 0
        for i in range(len(nums)):
            xor_sum = xor_sum ^ nums[i]

        result = []

        def takeanum(l1, ans, xor_sum):

            if xor_sum == 0:
                result.append(ans)
                return
            for i in range(len(l1)):
                if l1[i] != xor_sum:
                    xor_sum = xor_sum ^ l1[i]
                    l1.pop(i)
                    ans += 1
                    break

                if i == len(l1) - 1:
                    xor_sum = xor_sum ^ l1[i]
                    l1.pop(i)
                    ans += 1

            takeanum(l1, ans, xor_sum)

        takeanum(nums, 0, xor_sum)
        if result[0] % 2 == 1:
            return False
        else:
            return True


nums = [1, 1, 1, 2]
res = Solution().xorGame(nums)
print(res)
