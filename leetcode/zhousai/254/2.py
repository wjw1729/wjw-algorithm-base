"""

"""
def judge(nums):
    n=len(nums)
    for i in range(1,n-1):
        if nums[i]==(nums[i-1]+nums[i+1])/2:
            return True
    return False


class Solution:
    def rearrangeArray(self,nums):
        nums.sort()
        n=len(nums)

        while judge(nums):

            pre=nums[1]-nums[0]
            for i in range(2,n):
                if nums[i]-nums[i-1]==pre:
                    nums[i-2],nums[i-1],nums[i]=nums[i],nums[i-2],nums[i-1]
                pre=nums[i]-nums[i-1]
        return nums

nums = [1,2,3,4,5]
res=Solution().rearrangeArray(nums)
print(res)




