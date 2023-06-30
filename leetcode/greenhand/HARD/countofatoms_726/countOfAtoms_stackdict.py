"""
author:wjw
分析：stack里存放字典
"""


class Solution:
    def countOfAtoms(self, formula):

        n = len(formula)
        stack = [{}]

        i = 0
        while i < n:
            if formula[i] == '(':
                stack.append({})
                i += 1
                continue

            if i < n - 1 and formula[i].isupper() and formula[i + 1].islower():
                stack[-1].setdefault(formula[i:i + 2], 0)
                if i == n - 2 or (not formula[i + 2].isnumeric()):
                    stack[-1][formula[i:i + 2]] += 1
                    i = i + 2
                    continue
                else:
                    j = i + 2
                    while j < n and formula[j].isnumeric():
                        j += 1
                    num = int(formula[i + 2:j])
                    stack[-1][formula[i:i + 2]] += num
                    i = j
                    continue
            if formula[i].isupper():
                stack[-1].setdefault(formula[i], 0)
                if i == n - 1 or (not formula[i + 1].isnumeric()):
                    stack[-1][formula[i]] += 1
                    i = i + 1
                    continue
                else:
                    j = i + 1
                    while j < n and formula[j].isnumeric():
                        j += 1
                    num = int(formula[i + 1:j])
                    stack[-1][formula[i]] += num
                    i = j
                    continue

            if formula[i] == ')':
                if (i+1<n and not formula[i + 1].isnumeric()) or i==n-1:
                    num = 1
                    i += 1
                else:
                    j = i + 1
                    while j < n and formula[j].isnumeric():
                        j += 1
                    num = int(formula[i + 1:j])
                    i = j

                bra_dic = stack.pop()
                for k, v in bra_dic.items():
                    if k in stack[-1]:
                        stack[-1][k] += v * num
                    else:
                        stack[-1][k] = v * num
        res = ''
        for k, v in sorted(stack[0].items(), key=lambda x: x[0]):
            if v == 1:
                res += k
            else:
                res += k + str(v)

        return res


formula = "H2O"
formula = "H2MgO2"
formula = "K4N2O14S4"
formula = "Mg(OH)2"
formula = "K4(ON(SO3)2)2"

formula = "((N42)24(OB40Li30CHe3O48LiNN26)33(C12Li48N30H13HBe31)21(BHN30Li26BCBe47N40)15(H5)16)14"
formula="(H)"
res = Solution().countOfAtoms(formula)
print(res)
