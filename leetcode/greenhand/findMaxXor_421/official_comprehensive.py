"""
author:wjw
分析：将num以及异或和x,都转化为31位2进制数，从30位依次往低位判断，如果nums中有两个n位前缀的num异或和=1，则取1，否则取0.
"""


class Solution:
    def findMaximumXOR(self, nums) -> int:
        HighBit = 30
        x = 0
        for k in range(HighBit, -1, -1):
            k_prefix = set()

            for num in nums:
                k_prefix.add(num >> k)

            x_next = x * 2 + 1

            found = False
            for pre in k_prefix:
                if x_next ^ pre in k_prefix:
                    found = True
                    break

            if found == True:
                x = x_next
            else:
                x = x_next - 1

        return x


nums = [14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70]
res = Solution().findMaximumXOR(nums)
print(res)
