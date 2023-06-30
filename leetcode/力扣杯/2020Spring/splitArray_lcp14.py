"""
author:wjw
分析：神仙题啊！
素数筛+dp
"""

max_num = 1000000
min_factor = [1] * (max_num + 1)
p = 2

while (p <= max_num):
    i = p
    while i * p <= max_num:
        if min_factor[i * p] == 1:
            min_factor[i * p] = p
        i += 1
    p += 1
    while p <= max_num:
        if min_factor[p] == 1:
            break
        p += 1


class Solution:
    def splitArray(self, nums):
        f = {}
        n = len(nums)

        x = nums[0]
        INF = 100000000
        while True:
            if min_factor[x] == 1:
                f[x] = 1
                break
            f[min_factor[x]] = 1
            x //= min_factor[x]

        min_prev = 1

        for i in range(1, n):
            x = nums[i]
            min_cur = INF
            while True:
                if min_factor[x] == 1:
                    f[x] = min(f.get(x, INF), min_prev + 1)
                    min_cur = min(min_cur, f[x])
                    break
                f[min_factor[x]] = min(f.get(min_factor[x], INF), min_prev + 1)
                min_cur = min(min_cur, f[min_factor[x]])
                x //= min_factor[x]

            min_prev = min_cur

        return min_prev


nums = [2, 3, 3, 2, 3, 3]
nums = [2, 3, 5, 7]
res = Solution().splitArray(nums)
print(res)
