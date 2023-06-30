"""
official
分析：快了20倍。1.二分法查找base，快了很多。2.用的单独变量来保存need和cur，而非数组list之类，节省了时间  
"""
import time
class Solution:
    def shipWithinDays(self, weights, D):
        left,right=max(weights),sum(weights)


        while left<right:
            mid=(left+right)//2
            need, cur = 1, 0
            for weight in weights:
                if cur+weight>mid:
                    need+=1
                    cur=0
                cur+=weight


            if need<=D:
                right=mid
            else:
                left=mid+1

        return left


t1=time.time()
weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
D=5
result = Solution().shipWithinDays(weights, D)
print(result)
print(time.time()-t1)