"""
author:wjw
分析：在last列表基础上，加入num，输出加入num后的list(n位插入)。
"""
import time


def add(last, num):
    n = len(last[0])
    next = []
    for i in range(len(last)):
        for j in range(n + 1):
            temp = last[i].copy()
            temp.insert(j, num)
            next.append(temp)

    return next


class Solution:
    def permute(self, nums):
        ans = [[nums[0]]]
        for i in range(1, len(nums)):
            ans = add(ans, nums[i])
        return ans


t1 = time.time()
nums = [1, 2, 3, 4, 5, 6]
res = Solution().permute(nums)
print(res)
print(time.time() - t1)
