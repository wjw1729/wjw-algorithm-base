"""

"""

import bisect
class Solution:
    def getMoneyAmount(self, n: int) -> int:

        def weightedmid(l, r):
            presum = [0]
            total = 0
            for i in range(l, r + 1):
                total += i
                presum.append(total)
            best_splitnum=None
            abserr=float('inf')

            for i in range(r-l+1):
                err=abs(presum[-1]-presum[i]-(l+i)-presum[i])
                if err<abserr:
                    best_splitnum=l+i
                    abserr=err
            return best_splitnum

        def cost(target):
            ans = 0

            l = 1
            r = n
            while l <= r:
                mid = weightedmid(l, r)

                if mid < target:
                    l = mid + 1
                    ans += mid
                    print(mid)

                elif mid > target:
                    r = mid - 1
                    ans += mid
                    print(mid)
                else:
                    break
            return ans

        cost(1)

        return 0


res=Solution().getMoneyAmount(10)
print(res)