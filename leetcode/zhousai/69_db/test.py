class Solution:
    def minSwaps(self, nums) -> int:
        nums1 = 0
        n = len(nums)
        for num in nums:
            if num == 1:
                nums1 += 1

        maxnum = 0


        total = 1

        if nums[n - 1] != 1:
            total = 0

        else:
            for r in range(n - 2, -1, -1):
                if nums[r] == 1:
                    total += 1
                else:
                    break
        if nums[0] == 1:
            total += 1
        for i in range(1, n):
            if nums[i] == 1:
                total += 1

            else:
                maxnum = max(maxnum, total)
                total = 0

        return nums1 - maxnum


nums=[1,1,1,0,0,1,0,1,1,0]
res=Solution().minSwaps(nums)
print(res)