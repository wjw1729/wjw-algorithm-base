"""
author:wjw
分析：Counter以及字典的用法

"""

from collections import Counter


class Solution:
    def containsDuplicate(self, nums):
        d = Counter(nums)
        for k, v in d.items():
            if v >= 2:
                return True
        return False


nums = [1, 2, 3, 4]
res = Solution().containsDuplicate(nums)
print(res)
