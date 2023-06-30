"""
author:wjw
分析：问题转化为每个数前加+、-，求表达式能达到的最小非负整数。
    即为最终结果。----->将list尽可能平均地分为两堆—>res=A-B（A>=B）——>转化为从list中挑选出不超过（A+B）//2地最大堆，即为B---->背包问题。---->最终结果为A-B
"""

class Solution:
    def lastStoneWeightII(self,stones):
        sumall=sum(stones)
        half_sum=sumall//2

        dp=[0 for i in range(half_sum+1)]


        for stone in stones:
            for j in range(half_sum,-1,-1):
                if stone<=j:
                    dp[j]=max(dp[j],dp[j-stone]+stone)


        return sumall-2*dp[-1]

stones=[2]
res=Solution().lastStoneWeightII(stones)
print(res)
