"""
author:wjw
分析：实现扰乱很容易，困难的是如判断，因为判断实际上需要将所有的可能都考虑进去。
"""
import numpy as np


class Solution:
    def isScramble(self, s1, s2):
        def Scramble(str):
            if len(str) == 1:
                return str

            pos = np.random.randint(1, len(str))
            str1 = str[:pos]
            str2 = str[pos:]
            prob = np.random.random()
            if prob < 0.5:
                outstr = Scramble(str1) + Scramble(str2)
            else:
                outstr = Scramble(str2) + Scramble(str1)
            return outstr

        list = []

        for i in range(10 ** len(s1)):
            out = Scramble(s1)
            if out not in list:
                list.append(out)

        return s2 in list


s1 = "great"
s1 = 'abcde'
s1='abcdbdacbdac'
s2 = "rgeat"
s2 = 'caebd'
s2="bdacabcdbdac"
S = Solution()
res = S.isScramble(s1, s2)
print(res)
