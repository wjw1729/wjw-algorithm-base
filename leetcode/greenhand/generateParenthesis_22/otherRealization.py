"""
author:wjw
分析：转为一个数学问题：左括号表示+1，右括号表示-1，随意放置2n个数（+1，-1）各n个，确保任意accumulate和>=0.求所有可能的排列.
    复杂：全排列浪费时间。
"""
import itertools


def judge(l):
    l1 = list(itertools.accumulate(l))
    for i in l1:
        if i < 0:
            return False
    return True


class Solution:
    def generateParenthesis(self, n: int):
        l1 = [1] * n + [-1] * n
        l2 = list(set(itertools.permutations(l1)))
        l2 = [i for i in l2 if judge(i) == True]

        ans = []
        for i in range(len(l2)):
            ele = ''
            for j in range(len(l2[i])):
                if l2[i][j] == 1:
                    ele += "("
                else:
                    ele += ")"

            ans.append(ele)

        return ans


n = 6
res = Solution().generateParenthesis(n)
print(res)
print(len(res))