"""
author:wjw
分析：前缀异或，XOR(Li,Ri)=Pre(Li-1)^Pre(Ri)
"""


class Solution:
    def xorQueries(self, arr, queries):
        xor_sum = 0
        pre = []
        for i in range(len(arr)):
            xor_sum ^= arr[i]
            pre.append(xor_sum)

        xor_list = []
        for i in range(len(queries)):
            if queries[i][0] == 0:
                res = pre[queries[i][1]]
            else:
                res = pre[queries[i][0] - 1] ^ pre[queries[i][1]]
            xor_list.append(res)

        return xor_list


arr = [4, 8, 2, 10]
queries = [[2, 3], [1, 3], [0, 0], [0, 3]]

result = Solution().xorQueries(arr, queries)
print(result)
