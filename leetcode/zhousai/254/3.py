"""

"""

class Solution:
    def minNonZeroProduct(self,p):
        n=2**p-1

        ans=pow(n-1,n//2,10**9+7)
        ans=ans*n%(10**9+7)
        return ans

p=1
p=60
res=Solution().minNonZeroProduct(p)
print(res)