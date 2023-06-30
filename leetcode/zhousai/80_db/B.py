import bisect
class Solution:
    def successfulPairs(self, spells, potions, success: int) :

        n=len(spells)
        m=len(potions)
        potions.sort()

        ans=[0]*n
        for i in range(n):
            idx=bisect.bisect_left(potions,success/spells[i])

            ans[i]=m-idx


        return ans




