"""
author:wjw
分析：创建numRows个列表，用于存放Z型回路中每排的字符串，剩下的工作需要的只是将s中的字符添加入对应的列表中，遍历s时确定idx的数值即可，idx作为字符对应的列表索引号，转换关系如下。
"""


class Solution:
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        list = [''] * numRows
        for i in range(len(s)):
            idx = i % (2 * numRows - 2)
            if idx >= numRows:
                idx = 2 * numRows - idx - 2
            list[idx] += s[i]

        res = ''
        for i in range(len(list)):
            res += list[i]
        return res


s = 'PAYPALISHIRING'
numRows = 3
result = Solution().convert(s, numRows)
print(result)
