class Solution:
    def maximumXOR(self, nums) -> int:

        ans=0
        for  c in nums:
            ans|=c

        return ans

