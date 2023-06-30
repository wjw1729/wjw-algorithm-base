class Solution:
    def checkValidString(self, s: str) -> bool:

        bstack = []
        sstack = []

        for ch in s:
            if ch == '(' or ch == '*':
                bstack.append(ch)

            if ch == ')':
                if '(' in bstack:
                    bstack.remove('(')
                elif bstack:
                    bstack.pop(0)
                else:
                    return False

        if '(' not in bstack:
            return True

        index = bstack.index('(')

        return bstack[index:].count('(') <= bstack[index:].count('*')

s="((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()"
#s='(*'
res=Solution().checkValidString(s)
print(res)
