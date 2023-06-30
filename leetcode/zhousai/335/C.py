# 笛卡尔积
# 每次解析0层{}
# ，表示合并， x表示笛卡尔积
class Solution:
    def braceExpansionII(self, expression: str):

        def solve(s):


            sls = []
            stack = []
            plus = False

            for i in range(len(s)):
                if s[i] == '{':
                    stack.append(i)
                elif s[i] == '}':
                    l = stack.pop()
                    if not stack:
                        sls.append((l, '{'))
                        sls.append((i, '}'))
                elif s[i] == ',':
                    if not stack:
                        sls.append((i, ','))
                        plus = True
            if not sls:
                return [s]
            if not plus:
                pre = 0
                dls = ['']
                for i, x in sls:
                    if pre<i:
                        tmp = solve(s[pre:i])
                        dls = [x + y for x in dls for y in tmp]
                    pre = i + 1
                if pre<len(s):
                    tmp = solve(s[pre:len(s)])
                    dls = [x + y for x in dls for y in tmp]
                print(dls)
                return dls
            else:
                pre = 0
                dls = set()
                for i, x in sls:
                    if x==',':
                        if pre<i:
                            tmp = solve(s[pre:i])
                            dls |= set(tmp)
                        pre = i + 1
                if pre<len(s):
                    tmp = solve(s[pre:len(s)])
                    dls |= set(tmp)
                print(dls,1)
                return list(dls)

        return sorted(solve(expression))


expression = "{a,b}{c,{d,e}}"
expression = "{{a,z},a{b,c},{ab,z}}"
res=Solution().braceExpansionII(expression)
print(res)











