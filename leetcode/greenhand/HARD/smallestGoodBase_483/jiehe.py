"""
author:wjw
分析：问题为k**m+k**(m-1)+...+k**0=n， 即(k**(m+1)-1)/(k-1)==n
    k**m<n<(k+1)**m,k**m<n<k**(m+1)
    将两者结合一下，减少遍历的复杂度，对于k属于(2,10)，从k出发，遍历数少
    对于K>10，从m出发，遍历少。因为n范围最大为10**18，最大从18-10，所以遍历也较少
"""

import math


class Solution:
    def smallestGoodBase(self, n):
        n = int(n)

        for k in range(2, 10):
            m = math.floor(math.log(n, k))
            if k ** m > n:
                m -= 1

            if (k ** (m + 1) - 1) // (k - 1) == n:
                return str(k)

        m_range = math.floor(math.log10(n))

        for m in range(m_range, 0, -1):

            if m==1:
                return n-1
            k = math.ceil(n ** (1 / m)) - 1
            while (k + 1) ** (m) < n:
                k += 1


            if (k ** (m + 1) - 1) // (k - 1) == n:
                return str(k)


n = "821424692950225218"
res = Solution().smallestGoodBase(n)
print(res)
