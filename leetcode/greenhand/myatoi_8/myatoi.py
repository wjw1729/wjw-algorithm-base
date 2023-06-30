"""
author:wjw
分析：没啥特点的，就是按照题目的逻辑，进行分情况设计，暂时感觉流程还是有点乱的。
好像正则表达式很容易，一行？？？？？？？？？？？？？？？？？？？？？？？？？？？
"""


class Solution:
    def myAtoi(self, s):
        num = ''
        sign_sure = False
        sign = 0
        for i in range(len(s)):
            if sign_sure == False and s[i].isspace():
                continue
            if sign_sure == False and s[i] == '+':
                sign = 1
                sign_sure = True
                continue
            if sign_sure == False and s[i] == '-':
                sign = -1
                sign_sure = True
                continue
            if s[i].isnumeric():
                if sign_sure == False:
                    sign = 1
                    sign_sure = True
                num += s[i]
            else:
                break

        if num == '':   
            return 0
        res = sign * int(num)
        if res > 2 ** 31 - 1:
            res = 2 ** 31 - 1
        if res < -2 ** 31:
            res = -2 ** 31
        return res


s = ' -91283472332'
res = Solution().myAtoi(s)
print(res)
