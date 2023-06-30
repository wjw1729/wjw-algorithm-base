import math
class Solution:
    def minOperations(self, nums) -> int:

        lcm=1

        for c in nums:
            lcm=lcm*c//math.gcd(c,lcm)


        ans=0
        for c in nums:
            b=lcm//c
            while b%3==0:
                b//=3
                ans+=1

            while b%2==0:
                b//=2
                ans+=1
            if b!=1:
                return -1

        return ans

