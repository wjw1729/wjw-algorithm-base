"""
提取字符串中的数字。
"""

class Solution:
    def extractnums(self,s):
        n=len(s)
        ans=[]
        tmp=''
        for c in s:
            if not c.isnumeric() and tmp!='':
                ans.append(tmp)
                tmp=''
            elif c.isnumeric():
                tmp+=c

        ans=[int(x) for x in ans]
        ans.sort()

        return  ans

s=input().strip()#s="He15l154lo87wor7l87d"
print(Solution().extractnums(s))








