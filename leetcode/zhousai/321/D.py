from collections import Counter


class Solution:
    def countSubarrays(self, nums, k: int) -> int:

        n = len(nums)
        if k > n:
            return 0

        idx = nums.index(k)

        f = [0] * n

        l = 0
        r = 0
        for i in range(idx - 1, -1, -1):
            if nums[i] < k:
                l += 1
            else:
                r += 1
            f[i] = r - l

        l = 0
        r = 0
        for i in range(idx + 1, n):
            if nums[i] < k:
                l += 1
            else:
                r += 1
            f[i] = r - l

        cnt = Counter()
        cnt[0]=1
        for i in range(idx + 1, n):
            cnt[f[i]] += 1

        ans = cnt[1] +cnt[0]
        for i in range(idx):
            ans += cnt[1 - f[i]] + cnt[-f[i]]

        return ans


nums = [3, 2, 1, 4, 5]
k = 4
nums = [2,3,1]
k = 3
nums=[2,5,1,4,3,6]
k=1
res = Solution().countSubarrays(nums, k)
print(res)
