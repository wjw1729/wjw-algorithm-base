"""
author:wjw
分析：判断小数，判断整数
"""

def judgeint(s):
    if s.isnumeric():
        return True
    return False


def judgefloat(s):

    if s.count('.')==1:
        index=s.index('.')
        s=s[:index]+s[index+1:]
        if judgeint(s):
            return True
    else:
        return False



class Solution:
    def isNumber(self,s):
        if s[0]=='+' or s[0]=='-':
            s=s[1:]
        if judgeint(s) or judgefloat(s):
            return True

        if s.count('e')==1:
            index=s.index('e')
            front=s[:index]
            behind=s[index+1:]
            if judgeint(front) or judgefloat(front):
                if behind!='' and (behind[0]=='+' or behind[0]=='-'):
                    behind=behind[1:]
                if judgeint(behind):
                    return True

        if s.count('E')==1:
            index=s.index('E')
            front=s[:index]
            behind=s[index+1:]
            if judgeint(front) or judgefloat(front):
                if behind!='' and (behind[0]=='+' or behind[0]=='-'):
                    behind=behind[1:]
                if judgeint(behind):
                    return True
        return False

s="9E"
res=Solution().isNumber(s)
print(res)