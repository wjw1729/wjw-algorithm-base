


for _ in range(int(input())):
    n, a = int(input()), [*map(int, input().split())]
    cnt, mx = [[] for _ in range(n + 1)], 0
    ans = [0] * n

    for i in range(n):
        cnt[a[i]].append(i)
        mx = max(mx, len(cnt[a[i]]))
    cyc = [[] for _ in range(mx)]
    for c in cnt:
        for i in range(len(c)):
            cyc[i].append(c[i])

    1==1
    for c in cyc:
        for i in range(len(c)):
            ans[c[i]] = a[c[i - 1]]
    print(*ans)