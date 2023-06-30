from functools import lru_cache
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:

        @lru_cache(None)
        def dfs(s):
            print(s)

            if s[0] == '!':
                return not dfs(s[2:-1])

            elif s[0] == '&':
                stack = []
                l = 2
                for i in range(1, len(s)):
                    if s[i] == ')':

                        stack.pop()

                    elif s[i] == '(':
                        stack.append(s[i])
                    elif s[i] == ',':
                        if len(stack) == 1:
                            tmp = dfs(s[l:i])
                            l = i + 1
                            if tmp == False:
                                return False
                if not dfs(s[l:-1]):
                    return False

                return True

            elif s[0] == '|':
                stack = []
                l = 2
                for i in range(1, len(s)):
                    if s[i] == ')':
                        stack.pop()

                    elif s[i] == '(':
                        stack.append(s[i])
                    elif s[i] == ',':
                        if len(stack) == 1:
                            tmp = dfs(s[l:i])
                            l = i + 1
                            if tmp == True:
                                return True
                if dfs(s[l:-1]):
                    return True
                return False
            else:
                if s == 't':
                    return True
                else:
                    return False

        return dfs(expression)


s = "&(|(f))"
s="|(f,f,f,t)"
res = Solution().parseBoolExpr(s)
print(res)
