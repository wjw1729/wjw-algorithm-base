"""
author:wjw
分析：暴力枚举，超出时间限制
"""


class Solution:
    def xorQueries(self, arr, queries):
        xor_list = []
        for i in range(len(queries)):
            res = 0
            for j in range(queries[i][0], queries[i][1] + 1):
                res = res ^ arr[j]

            xor_list.append(res)
        return xor_list


arr = [4, 8, 2, 10]
queries = [[2, 3], [1, 3], [0, 0], [0, 3]]

result = Solution().xorQueries(arr, queries)
print(result)
