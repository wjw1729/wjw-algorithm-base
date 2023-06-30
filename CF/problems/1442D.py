def main():
    n, k = [int(x) for x in input().split()]

    pls = []
    for _ in range(n):
        pls.append([int(x) for x in input().split()][1:])

    ans = 0
    dp = [0] * (k + 1)

    def f(a, total):
        nonlocal dp, ans
        if len(a) == 1:
            s = 0
            for i, x in enumerate(a[0]):
                if i >= k:
                    break
                s += x
                ans = max(ans, dp[k - (i + 1)] + s)
            return

        tmp = dp.copy()
        m = len(a) // 2
        left, right = a[:m], a[m:]

        for i, row in enumerate(left):
            for j in range(k, len(row) - 1, -1):
                dp[j] = max(dp[j], dp[j - len(row)] + total[i])

        f(right, total[m:])

        dp = tmp

        for i, row in enumerate(right):
            for j in range(k, len(row) - 1, -1):
                dp[j] = max(dp[j], dp[j - len(row)] + total[m + i])

        f(left, total[:m])

    total = [sum(x) for x in pls]
    f(pls, total)
    print(ans)


main()
