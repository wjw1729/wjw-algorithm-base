class Solution:
    def countDistinct(self, nums, k: int, p: int) -> int:

        n = len(nums)
        vis = set()

        a=[int(x%p==0) for x in nums]

        presum = [0] * (n + 1)
        for i in range(1,n+1):
            presum[i]=presum[i-1]+a[i-1]


        cnt=0
        for l in range(n):
            for r  in range(l,n):#取到
                if tuple(nums[l:r+1]) not in vis:
                    if presum[r+1]-presum[l]<=k:
                        cnt+=1
                    vis.add(tuple(nums[l:r+1]))

        return cnt

nums = [2,3,3,2,2]
k = 2
p = 2
nums = [1,2,3,4]
k = 4
p = 1
res=Solution().countDistinct(nums,k,p)
print(res)

