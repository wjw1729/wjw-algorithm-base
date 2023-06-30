"""
author:off
分析：滑动窗口+递推关系.
    重点就是递推关系的推导：total(l,r)=(r-l)*nums[r]-sum(nums[l:r])（双闭区间）
                        total(l,r+1)-total(l,r)=(r+1-l)*[nums(r+1)-nums(r)]

"""


class Solution:
    def maxFrequency(self, nums, k):
        nums.sort()
        n = len(nums)
        total = 0
        left = 0
        res = 1

        for r in range(1, n):
            total += (r - left) * (nums[r] - nums[r - 1])

            while total > k:
                left += 1
                total -= nums[r] - nums[left - 1]

            res = max(res, r - left + 1)

        return res


nums = [1, 4, 8, 13]
k = 5
nums = [9930, 9923, 9983, 9997, 9934, 9952, 9945, 9914, 9985, 9982, 9970, 9932, 9985, 9902, 9975, 9990, 9922, 9990,
        9994, 9937, 9996, 9964, 9943, 9963, 9911, 9925, 9935, 9945, 9933, 9916, 9930, 9938, 10000, 9916, 9911, 9959,
        9957, 9907, 9913, 9916, 9993, 9930, 9975, 9924, 9988, 9923, 9910, 9925, 9977, 9981, 9927, 9930, 9927, 9925,
        9923, 9904, 9928, 9928, 9986, 9903, 9985, 9954, 9938, 9911, 9952, 9974, 9926, 9920, 9972, 9983, 9973, 9917,
        9995, 9973, 9977, 9947, 9936, 9975, 9954, 9932, 9964, 9972, 9935, 9946, 9966]
k = 3056
res = Solution().maxFrequency(nums, k)
print(res)
