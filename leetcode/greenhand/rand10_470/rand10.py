"""
author:wjw
分析：
"""

import random
class Solution:
    def rand10(self):

        hashmap = {}
        k = 0
        for i in range(1, 7):
            for j in range(1, 8):
                hashmap[(i, j)] = k % 10
                k += 1

        hashmap.pop((6, 6))
        hashmap.pop((6, 7))

        a = 6
        b = 7

        while a == 7 or (a == 6 and b == 6 or 7):
            a = random.randint(1,7)
            b = random.randint(1,7)
            if (a, b) in hashmap:
                return hashmap[(a, b)] + 1



bin=set()
for i in range(10000):
    res=Solution().rand10()
    if res not in bin:
        print(res)
    bin.add(res)
