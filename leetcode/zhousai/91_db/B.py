class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:

        mod=10**9+7
        f=[0 for _ in range(high+2)]
        f[0]=1
        for i in range(high+1):
            if i+zero<=high+1:
                f[i+zero]+=f[i]
                f[i+zero]%=mod
            if i+one<=high+1:
                f[i+one]+=f[i]
                f[i+one]%=mod

        return sum(f[low:high+1])%mod

