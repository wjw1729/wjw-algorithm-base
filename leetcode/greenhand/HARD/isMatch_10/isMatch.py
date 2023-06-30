"""
author:wjw
分析：双指针试一下！
"""


class Solution:
    def isMatch(self, s, p):

        len_s = len(s)
        len_p = len(p)

        for i in range(len_p-1,1,-1):
            if p[i-1]=='*' and p[i]==p[i-2]:
                p=p[:i]+p[i+1:]
        len_p=len(p)
        for i in range(len_p-1,0,-1):
            if p[i]=='*' and p[i-1]=='*':
                p=p[:i]+p[i+1:]
        len_p=len(p)

        i = 0
        j = 0

        while i < len_s and j < len_p:
            if s[i] == p[j] or p[j]=='.':
                i += 1
                j += 1
                continue
            if s[i] != p[j]:
                if p[j] == '*':
                    if s[i] == p[j - 1] or p[j-1]=='.':
                        i += 1
                        continue
                    else:
                        j += 1
                        continue
                else:
                    if j < len_p - 1 and p[j + 1] == '*':
                        j += 2
                        continue
                    else:
                        return False

        if i<len_s:
            return False
        if j<len_p and p[j]=='*':
            j+=1
        if j==len_p:
            return True

        if (len_p-j)%2!=0:
            return False
        for k in range(j+1,len_p,2):
            if p[k]!='*':
                return False
        return True


s = "aa"
p = "a"
p='a*'
s='ab'
p='.*'
s='aab'
p='c*a*b'
s = "mississippi"
p = "mis*is*p*."
s="ab"
p=".*c"
s='aaa'
p='.*a'
res=Solution().isMatch(s,p)
print(res)