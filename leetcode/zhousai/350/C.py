class Solution:
    def specialPerm(self, nums) -> int:
        n = len(nums)
        mod = 10 ** 9 + 7
        ans = 0

        f = [[0] * n for _ in range(2 ** n)]

        for mask in range(1, 2 ** n):
            if mask == 2 ** n - 1:
                print(1)
            for j in range(n):
                if mask & (1 << j):
                    pre = mask ^ (1 << j)
                    if pre == 0:
                        f[mask][j] = 1
                        continue
                    for jj in range(n):
                        if nums[j] % nums[jj] == 0 or nums[j] % nums[jj] == 0:
                            f[mask][j] += f[pre][jj]
                            f[mask][j] %= mod

        for i in range(n):
            ans += f[2 ** n - 1][i]
            ans %= mod
        print(f)
        return ans

nums=[2,3,6]
res=Solution().specialPerm(nums)
print(res)

