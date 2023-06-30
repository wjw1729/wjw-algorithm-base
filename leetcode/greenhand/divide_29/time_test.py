
import time
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if (dividend >= 0 and divisor > 0) or (dividend <= 0 and divisor < 0):
            sign = 1
            divisor = abs(divisor)
            dividend = abs(dividend)

        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            sign = -1
            divisor = abs(divisor)
            dividend = abs(dividend)

        ans = 0
        while divisor <= dividend:
            dividend = dividend - divisor
            ans += 1

        return ans * sign


t1=time.time()
dividend = 3000000000000
divisor = 1
res = Solution().divide(dividend, divisor)
print(res)
print(time.time()-t1)