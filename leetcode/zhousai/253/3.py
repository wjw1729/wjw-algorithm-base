"""
author:wjw
分析：
"""
import math
class Solution:
    def minSwaps(self,s):
        total=0
        minValue=float('inf')
        for bracket in s:
            if bracket=='[':
                total+=1
            else:
                total-=1

            minValue=min(minValue,total)

        return math.ceil(-minValue/2)

s=']]][[['
res=Solution().minSwaps(s)
print(res)