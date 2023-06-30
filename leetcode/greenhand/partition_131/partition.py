"""
author:wjw
分析:回溯算法
"""

class Solution:
    def partition(self,s):

        ans=[]
        def backtrack(s,split_ls):
            if s=='':
                ans.append(split_ls[:])
                return

            n=len(s)
            for i in range(1,n+1):
                if s[:i]==s[:i][::-1]:
                    tmp=s
                    split_ls.append(s[:i])
                    s=s[i:]

                    backtrack(s,split_ls)

                    s=tmp
                    split_ls.pop()


        backtrack(s,[])
        return  ans


s="aab"
res=Solution().partition(s)
print(res)



