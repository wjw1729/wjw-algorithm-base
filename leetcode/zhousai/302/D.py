def gcd(a,b):
    return b if a%b==0 else gcd(b,a%b)

class Solution:
    def minOperations(self, nums, numsDivide) -> int:

        mod=numsDivide[0]

        for i in range(1,len(numsDivide)):
            mod=gcd(mod,numsDivide[i])

            if mod==1:
                break

        mmod=float('inf')
        for c in nums:
            if mod%c==0:
                mmod=min(c,mmod)

        if mmod==float('inf'):
            return -1

        ans=0
        for c in nums:
            if c<mmod:
                ans+=1

        return ans

nums = [2,3,2,4,3]
numsDivide = [9,6,9,3,15]
res=Solution().minOperations(nums,numsDivide)
print(res)