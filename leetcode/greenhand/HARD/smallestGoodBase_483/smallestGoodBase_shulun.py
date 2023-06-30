"""
author:wjw
分析：问题为k**m+k**(m-1)+...+k**0=n， 即(k**(m+1)-1)/(k-1)==n
    k**m<n<(k+1)**m,k**m<n<k**(m+1)
    从k出发，依据不等式求m，然后判断k和m是否符合上述等式关系

"""
import math


class Solution:
    def smallestGoodBase(self, n):
        n = int(n)

        for k in range(2, n):
            m = math.floor(math.log(n, k))

            if (k ** (m + 1) - 1) / (k - 1) == n:
                return str(k)


n = "1000000000000000000"
res = Solution().smallestGoodBase(n)
print(res)
