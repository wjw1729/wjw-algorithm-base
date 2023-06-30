from sortedcontainers import SortedList
class Solution:
    def zeroFilledSubarray(self, nums) -> int:

        n = len(nums)
        ans = 0
        i=0

        while i < n:

            while i < n and nums[i] != 0:
                i += 1
            l = i

            while i < n and nums[i] == 0:
                i += 1

            r = i
            ans += (r - l) * (r - l + 1) // 2

        return ans

nums=[1,3,0,0,2,0,0,4]
nums = [0,0,0,2,0,0]
nums = [2,10,2019]
res=Solution().zeroFilledSubarray(nums)
print(res)