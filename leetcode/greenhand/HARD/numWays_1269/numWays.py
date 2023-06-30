"""
auhtor:wjw
分析：1表示向右，-1表示向左，0表示不动，生成所有的方案（不同0），然后计算其不重复的排列数，最后去掉迭代和不符合要求的数目
"""

import itertools
import time

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:

        def judge(l1):
            x = list(itertools.accumulate(l1))
            if min(x) >= 0 and max(x) <= arrLen - 1:
                return True
            return False

        zero_num = steps % 2
        mth = []
        while zero_num <= steps:
            x = [0] * zero_num + [1] * ((steps - zero_num) // 2) + [-1] * ((steps - zero_num) // 2)
            mth.append(x)
            zero_num += 2

        total = 0
        for i in range(len(mth)):
            x = set(itertools.permutations(mth[i]))
            x = list(x)
            x = [i for i in x if judge(i) == True]
            total += len(x)

        return total


t1 = time.time()
steps = 15
arrLen = 15
res = Solution().numWays(steps, arrLen)
print(res)
print(time.time() - t1)
