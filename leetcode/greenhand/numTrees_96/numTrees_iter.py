"""
author:wjw
分析：递归会超时。所有的递归都可以转为迭代实现。
"""

class Solution:
    def numTrees(self,n):

        treenum=[0]*20
        treenum[0]=1

        for i in range(1,n+1):
            for j in range(1,i+1):
                treenum[i]+=treenum[j-1]*treenum[i-j]

        return treenum[n]


n=19
res=Solution().numTrees(n)
print(res)