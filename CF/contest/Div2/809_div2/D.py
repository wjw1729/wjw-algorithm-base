import bisect

t = int(input())

for _ in range(t):
    n, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]

    a.sort()

    ans = float('inf')

    for l in range(a[0] + 1):
        r = l
        for j in range(n):
            ll = 1
            rr = k
            while ll <= rr:
                mid = (ll + rr + 1) // 2
                if a[j] // mid < l:
                    rr = mid - 1
                else:
                    tmpr = a[j] // mid
                    ll = mid + 1

            r = max(tmpr, r)
        ans = min(r - l, ans)
        # print(l,r,ans)

    print(ans)
