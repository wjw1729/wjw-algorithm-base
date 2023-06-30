class Solution:
    def countSubarrays(self, nums, k: int) -> int:

        n=len(nums)
        presum=[0]*(n+1)

        for i in range(1,n+1):
            presum[i]=presum[i-1]+nums[i-1]

        ans1=0
        for i in range(n):

            l=i
            r=n-1

            while l<=r:
                mid=(l+r+1)//2
                ans=(presum[mid+1]-presum[i])*(mid-i+1)
                if ans>=k:
                    r=mid-1

                else:
                    l=mid+1
                    res=mid-i+1

            print(res)
            ans1+=res

        return ans1
nums = [2,1,4,3,5]
k = 10
res=Solution().countSubarrays(nums,k)
print(res)