"""
author:wjw
分析：递归会超时。
"""

class Solution:
    def numTrees(self,n):
        if n==0:
            return 1
        if n==1:
            return 1
        else:
            res=0
            for i in range(1,n+1):
                res+=self.numTrees(i-1)*self.numTrees(n-i)

            return res


n=4
res=Solution().numTrees(n)
print(res)


