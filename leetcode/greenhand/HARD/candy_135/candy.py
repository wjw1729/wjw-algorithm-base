"""
author：wjw
分析：将原问题拆解为左规则和右规则。
"""

class Solution:
    def candy(self,ratings):
        n=len(ratings)

        left=[1]*n

        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                left[i]=left[i-1]+1

        right=1
        ans=max(right,left[n-1])

        for i in range(n-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                right+=1
            else:
                right=1

            ans+=max(left[i],right)

        return  ans

ratings=[1,0,2]
ratings=[1,2,2]
res=Solution().candy(ratings)
print(res)

