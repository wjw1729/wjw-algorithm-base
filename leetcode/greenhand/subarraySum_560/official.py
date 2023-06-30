"""
author:wjw
分析：前缀和+哈希表
"""


class Solution:
    def subarraySum(self, nums, k):
        d = {0: 1}
        n = len(nums)
        sum = 0
        ans = 0
        for i in range(n):
            sum += nums[i]
            if sum-k in d.keys():
                ans += d[sum - k]

            if sum in d.keys():
                d[sum] += 1
            else:
                d[sum]=1
        return ans



nums=[1,1,1]
k=2
res=Solution().subarraySum(nums,k)
print(res)
