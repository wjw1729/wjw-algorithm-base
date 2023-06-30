class Solution:
    def constructArray(self, n: int, k: int):
        ans = list(range(1, (k + 1) // 2 + 1)) + reversed(list(range((k + 1) // 2 + 1, k + 1)))

        ans += list(range(k + 1, n + 1))

        return ans
