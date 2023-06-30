"""
author:wjw
分析：动态规划会超时。O（m*m**2)
欧拉筛:O(m*n),但是看不懂.

"""

from functools import lru_cache


def main():
    @lru_cache(None)
    def inv(x):
        nonlocal p
        if x <= 1:
            return 1
        return (p - p // x) * inv(p % x)

    p = 998244353
    n, m = [int(word) for word in input().strip().split()]
    dp = [1 for i in range(n + 1)]
    vis = [0 for i in range(n + 1)]  # min_factor
    count = [1 for i in range(n + 1)]  # count min_factor
    primes = []
    ans = 1
    for i in range(2, n + 1):
        if not vis[i]:
            primes.append(i)
            vis[i] = i
        for j in primes:
            if i * j > n:
                break
            vis[i * j] = j
            if i % j == 0:
                count[i * j] = count[i] + 1
                break
        dp[i] = dp[i // vis[i]] * (count[i] + m - 1) * inv(count[i]) % p
        ans += dp[i]
        ans %= p
    print(ans)


if __name__ == "__main__":
    main()
