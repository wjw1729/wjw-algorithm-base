class Solution:
    def findMaxCI(self, nums) :

        n=len(nums)
        ans=0
        tmp=1
        for i in range(1,n):
            if nums[i]>nums[i-1]:
                tmp+=1
            else:
                ans=max(ans,tmp)
                tmp=1

        return ans