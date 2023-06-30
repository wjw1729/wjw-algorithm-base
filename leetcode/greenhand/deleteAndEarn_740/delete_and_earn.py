"""
author:wjw
分析：间隔取元素，但是不能重复。将原数的list转为一个字典。之后再用dp动态规划记录当最大数为k时的最大点数
"""

from collections import Counter
class Solution:
    def deleteAndEarn(self, nums) -> int:
        nums=sorted(nums)
        d=Counter(nums)
        n=len(d.keys())
        dp=[0]*(n+1)
        pre=0
        i=1
        for k,v in d.items():
            if k==pre+1:
                if i>1:
                    dp[i]=max(dp[i-2]+k*d[k],dp[i-1])
                else:
                    dp[i]=k*d[k]
            else:
                dp[i]=dp[i-1]+k*d[k]
            i=i+1
            pre=k


        return dp[n]



nums=[3,4,2]
nums=[2,2,3,3,3,4]
#nums=[1,1,1,2,4,5,5,5,6]
res=Solution().deleteAndEarn(nums)
print(res)