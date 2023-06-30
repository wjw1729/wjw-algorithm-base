"""
author:wjw
分析：可以优化
"""

class Solution:
    def minDistance(self,word1,word2):
        m=len(word1)
        n=len(word2)

        pre=[i for i in  range(n+1)]
        next=[0]*(n+1)

        for i in range(1,m+1):
            for j in range(n+1):
                if j==0:
                    next[j]=pre[j]+1
                    continue
                if word1[i-1]==word2[j-1]:
                    next[j]=pre[j-1]
                else:
                    next[j]=min(pre[j],next[j-1],pre[j-1])+1
            pre[:]=next
        return next[-1]

word1='horse'
word2='ros'
word1='intention'
word2='execution'
res=Solution().minDistance(word1,word2)
print(res)