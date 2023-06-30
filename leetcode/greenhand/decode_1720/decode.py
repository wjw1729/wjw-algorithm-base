"""
author：wjw
分析：异或操作的逆运算也是异或，只需要将first开始，逐位与encoded list中的数进行异或运算即可


"""


class Solution:
    def decode(self, encoded, first: int):
        arr = [first]
        now = first
        for i in range(len(encoded)):
            next = encoded[i] ^ now
            arr.append(next)
            now = next

        return arr


encoded = [1, 2, 3]
encoded = [6, 2, 7, 3]

first = 1
first = 4
res = Solution().decode(encoded, first)
print(res)
