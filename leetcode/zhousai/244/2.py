
from collections import Counter
class Solution:
    def reductionOperations(self, nums) -> int:
        d=Counter(nums)
        k=sorted(d.keys(),reverse=True)

        n=len(k)
        num=n-1
        ans=0
        for i in k:
            ans+=d[i]*num
            num-=1

        return ans


nums=[1,1,2,2,3]
res=Solution().reductionOperations(nums)
print(res)