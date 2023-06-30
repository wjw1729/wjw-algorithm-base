import bisect
import math

t = int(input())

for _ in range(t):
    n, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]

    a.sort()

    ans = float('inf')

    lls=set()

    for i in range(n):
        for j in range(math.ceil(a[i]//a[0]),k+1):
            if a[i]//j<=a[0]:
                lls.add(a[i]//j)


    for l in sorted(lls):
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
        #print(l,r,ans)

    print(ans)
