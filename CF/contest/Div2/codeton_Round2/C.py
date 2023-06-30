t = int(input())
for _ in range(t):
    n, m = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    kls = []

    a.sort()

    a.append(a[0] + n)

    for i in range(1, m + 1):
        kls.append(a[i] - a[i - 1] - 1)

    kls.sort(reverse=True)

    ans = 0
    d = 0
    for i, k in enumerate(kls):
        tmp = k - 2 * d
        if tmp <= 0:
            break
        elif tmp <= 2:
            d += 1
            ans += 1
        else:
            ans += tmp - 1
            d += 2

    print(n - ans)
