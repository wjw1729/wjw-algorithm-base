"""
author:wjw
分析：定义一个函数，输入为当前的最终输出字符串list，以及下一个输入的数字字符，输出为加入这个字符后的list。
"""


class Solution:
    def letterCombinations(self, digits: str):
        d = {}
        d['2'] = ['a', 'b', 'c']
        d['3'] = ['d', 'e', 'f']
        d['4'] = ['g', 'h', 'i']
        d['5'] = ['j', 'k', 'l']
        d['6'] = ['m', 'n', 'o']
        d['7'] = ['p', 'q', 'r', 's']
        d['8'] = ['t', 'u', 'v']
        d['9'] = ['w', 'x', 'y', 'z']

        def add(ans, num):
            next = []
            for i in range(len(ans)):
                for j in range(len(d[num])):
                    next.append(ans[i] + d[num][j])

            return next

        ans = ['']

        for i in range(len(digits)):
            ans = add(ans, digits[i])

        if ans == ['']:
            return []
        return ans


digits = ''
res = Solution().letterCombinations(digits)
print(res)
