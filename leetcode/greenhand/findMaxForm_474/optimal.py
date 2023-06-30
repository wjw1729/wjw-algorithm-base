"""
author:wjw
分析：存储空间得到了优化，时间反而变慢了
"""
import copy
class Solution:
    def findMaxForm(self,strs,m,n):
        strs_len=len(strs)
        pre_dp=[[0 for i in range(n+1)]for i in range(m+1)]
        next_dp=[[0 for i in range(n+1)]for i in range(m+1)]

        for i in range(1,strs_len+1):

            num_0=strs[i-1].count('0')
            num_1=strs[i-1].count('1')
            for j in range(m+1):
                for k in range(n+1):

                    if num_0<=j and num_1<=k:
                        next_dp[j][k]=max(pre_dp[j][k],pre_dp[j-num_0][k-num_1]+1)
                    else:
                        next_dp[j][k]=pre_dp[j][k]

            pre_dp=copy.deepcopy(next_dp)

        return next_dp[m][n]


strs=["10", "0001", "111001", "1", "0"]
#strs=["111","1000","1000","1000"]
m=5
n=3
res=Solution().findMaxForm(strs,m,n)
print(res)