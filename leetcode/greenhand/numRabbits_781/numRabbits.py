"""
author:wjw
分析：
"""

from collections import Counter
import math


class Solution:
    def numRabbits(self, answers):
        d = Counter(answers)
        ans = 0
        for k, v in d.items():
            ans += (k + 1) * math.ceil(v / (k + 1))

        return ans


answers = [1, 1, 2]
answers = [10, 10, 10]
answers=[]
res = Solution().numRabbits(answers)
print(res)
