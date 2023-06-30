"""
author:wjw
分析：将最小堆和动态规划结合起来！
"""
import heapq
class Solution:
    def nthSuperUglyNumber(self,n,primes):
        dp=[1]
        his={1}
        heap=[]

        for prime in primes:
            heapq.heappush(heap,(prime,0,prime))
            his.add(prime)

        for j in range(1,n):
            num,i,p=heapq.heappop(heap)
            dp.append(num)
            while num in his:
                num=dp[i]*p
                i+=1

            heapq.heappush(heap,(num,i,p))
            his.add(num)
        return dp[-1]

n=12
primes=[2, 7, 13, 19]
res=Solution().nthSuperUglyNumber(n,primes)
print(res)
