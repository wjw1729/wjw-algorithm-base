"""
author:wjw
分析：回溯。

"""

class Solution:
    def splitString(self, s: str) -> bool:

        def backtrack(start, end, prenum):
            if start == end and prenum !=int(s):
                return True

            for i in range(start + 1, end + 1):
                num = int(s[start:i])
                if num == prenum - 1 or prenum == -1:
                    if backtrack(i, end, num):
                        return True

            return False

        return backtrack(0, len(s), -1)

s='1234'
res=Solution().splitString(s)
print(res)