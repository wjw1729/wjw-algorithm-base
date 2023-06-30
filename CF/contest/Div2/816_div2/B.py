t = int(input())
for _ in range(t):
    n, k, b, s = [int(x) for x in input().split()]

    if not (k * b <= s and k * b+n*(k-1) >= s):
        print(-1)
    else:
        ans = [0] * n
        ans[-1] = b*k
        lt = s-b*k

        i = 0
        while lt > 0:

            if lt >= k - 1:
                ans[i] += k - 1
                lt -= k - 1
                i += 1
            else:
                ans[i] += lt
                lt = 0
                i += 1

        print(*ans)
