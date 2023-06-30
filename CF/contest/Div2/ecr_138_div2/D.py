import math

mod = 998244353

n, m = [int(x) for x in input().split()]


def getnum(m, factors):
    ans = 0
    n = len(factors)
    for mask in range(1 << n):
        num = 1
        cnt = 0
        for i in range(n):
            if 1 << i & mask:
                num *= factors[i]
                cnt += 1
        ans += (-1) ** cnt * (m // num)

    return ans


def solve():
    b = m // 2
    a = m - b

    ans1 = m * a % mod
    ans2 = m * b % mod

    if n == 2:
        print(ans1)
        return

    ans = ans1
    for i in range(3, n + 1):
        factors = []
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                factors.append(j)
                while i % j:
                    i //= j
            if i == 1:
                break
        if i > 1:
            factors.append(i)

        a = getnum(m, factors)
        b = m - a

        ans1 = ((ans1 + ans2) * a + ans1 * b) % mod
        ans2 = ans2 * b % mod
        ans += ans1

    print(ans)


solve()
