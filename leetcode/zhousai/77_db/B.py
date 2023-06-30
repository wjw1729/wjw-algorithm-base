class Solution:
    def minimumAverageDifference(self, nums) -> int:

        n = len(nums)
        presum = [0] * (n + 1)

        for i in range(1, n + 1):
            presum[i] = presum[i - 1] + nums[i - 1]

        total = presum[-1]
        mindiff = float('inf')
        ans = 0
        for i in range(1, n + 1):
            a=(total - presum[i]) / (n - i) if i < n else 0
            tmp = abs(int(presum[i] / i) - int(a))
            if tmp < mindiff:
                mindiff = tmp
                ans = i - 1

        return ans

nums=[0,1,0,1,0,1]
res=Solution().minimumAverageDifference(nums)
print(res)


