class Solution:
    def findDuplicates(self, nums) :

        n = len(nums)
        for i in range(n):
            while nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1],nums[i] =nums[i],nums[nums[i] - 1]
                a=1

        return [c for i, c in enumerate(nums) if i + 1 != c]


nums = [4,3,2,7,8,2,3,1]
res=Solution().findDuplicates(nums)