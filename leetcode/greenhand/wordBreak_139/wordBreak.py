"""
author:wjw
分析：
"""

class Solution:
    def wordBreak(self,s,wordDict):
        wordDict=set(wordDict)
        n=len(s)
        dp=[False]*(n+1)
        dp[0]=True

        for i in range(1,n+1):
            for j in range(i):
                dp[i]=dp[i] or (dp[j] and s[j:i] in wordDict)


        return dp[-1]

s='leetcode'
wordDict=['leet','code']
res=Solution().wordBreak(s,wordDict)
print(res)
