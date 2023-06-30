"""
author:wjw
分析：按长度排序+0,1计数.不太行
"""

class Solution:
    def findMaxForm(self,strs,m,n):
        n_str=len(strs)
        strs1=sorted(strs,key=lambda x:x.count('0'))
        strs2=sorted(strs,key=lambda x:x.count('1'))

        ans=0
        for i in  range(n_str):

            if strs[i].count('0')<=m and strs[i].count('1')<=n:
                ans+=1
                m-=strs[i].count('0')
                n-=strs[i].count('1')
            if m+n<len(strs[i]):
                break

        return ans


strs=["10", "0001", "111001", "1", "0"]
strs=["111","1000","1000","1000"]
m=9
n=3
res=Solution().findMaxForm(strs,m,n)
print(res)