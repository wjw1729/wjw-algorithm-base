"""
author:wjw
分析：LIS问题
"""

import bisect
class Solution:
    def maxEnvelopes(self,envelopes):

        envelopes.sort(key=lambda x:(x[0],-x[1]))


        stack=[]
        for _,w in envelopes:
            index=bisect.bisect_left(stack,w)
            if index==len(stack):
                stack.append(w)
            else:
                stack[index]=w

        return len(stack)


envelopes=[[5,4],[6,4],[6,7],[2,3]]
envelopes=[[6,7],[5,3],[2,4],[1,1]]
res=Solution().maxEnvelopes(envelopes)
print(res)
