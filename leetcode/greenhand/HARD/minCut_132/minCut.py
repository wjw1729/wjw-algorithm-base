"""
author:wjw
分析：回溯算法。会超时。
"""


class Solution:
    def minCut(self, s):
        self.ans = float('inf')

        def backtrack(s, split_num):
            if s == '':
                self.ans = min(self.ans, split_num)
                return

            n = len(s)
            for i in range(1, n + 1):
                if s[:i] == s[:i][::-1]:
                    split_num += 1
                    tmp = s
                    s = s[i:]

                    backtrack(s, split_num)
                    s = tmp
                    split_num -= 1

        backtrack(s, 0)
        return self.ans - 1


s = "aab"
res = Solution().minCut(s)
print(res)
