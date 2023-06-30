"""
author:wjw
分析：回溯+剪枝
"""


class Solution:
    def restoreIpAddresses(self, s):
        self.ans = []

        def backtrack(s, pick):
            if s == '' and len(pick) == 4:
                self.ans.append('.'.join(pick))
                return
            if len(pick) >= 4:
                return
            if s == '':
                return
            n = len(s)
            for i in range(n):
                temp = s[:i + 1]
                s = s[i + 1:]
                if int(temp) > 255:
                    break
                if 0 <= int(temp) <= 255 and temp[0] != '0' or temp == '0':
                    pick.append(temp)

                    backtrack(s, pick)
                    pick.pop()
                s = temp + s

        backtrack(s, [])
        return self.ans


s = '25525511135'
"""
s = '1111'
s = "010010"
s = "101023"
s = '0000'
"""
res = Solution().restoreIpAddresses(s)
print(res)
