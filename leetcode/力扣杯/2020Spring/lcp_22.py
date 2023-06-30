def factorial(n):
    if n==0:
        return 1
    if n == 1:
        return 1
    return n * factorial(n - 1)


def Cnk(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))


class Solution:
    def paintingPlan(self, n: int, k: int) -> int:
        if k < n:
            return 0

        if k % n == 0:
            return 2 * Cnk(n, k // n) if k//n!=n else 1
        else:
            red = (k // n + 1) * n - k
            ans = 0
            for i in range(1, n + 1):
                if red < i:
                    break
                if red % i == 0:
                    ans += Cnk(n, i) * Cnk(n, red // i)

            return ans


n = 2
k = 4
res = Solution().paintingPlan(n, k)
print(res)
