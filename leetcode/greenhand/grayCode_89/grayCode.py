"""
author:wjw
分析：
"""

class Solution:
    def grayCode(self,n):
        pre='0'*n
        ans=[pre]
        his={pre}

        while len(ans)<2**n:
            for i in range(n-1,-1,-1):
                now=pre[:i]+str(1-int(pre[i]))+pre[i+1:]
                if now not in his:
                    his.add(now)
                    ans.append(now)
                    pre=now
                    break

        return ans


n=2
res=Solution().grayCode(n)
print(res)
