
import time
class Solution:
    def coinChange(self, coins, amount: int) -> int:

        n = len(coins)
        coins.sort(reverse=True)
        self.res = float('inf')

        def dfs(index, target, count):
            coin = coins[index]

            if target // coin + count >= self.res:  # 剪枝条件
                return
            if target % coin == 0:
                self.res = count + target // coin
                return

            if index == n - 1:
                return

            for j in range(target // coin, -1, -1):  # DFS
                dfs(index + 1, target - j * coin, count + j)

        dfs(0, amount, 0)
        return self.res if self.res != float('inf') else -1


t1=time.time()
coins = [1, 2, 5]
coins=[411,412,413,414,415,416,417,418,419,420,421,422]
amount = 9864
res = Solution().coinChange(coins, amount)
print(res)
print(time.time()-t1)