import math

t = int(input())

for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]

    pls = []
    for i in range(n):
        tmp = float('inf')
        for j in range(n):
            if j == i:
                continue
            tmp = min(tmp, math.gcd(a[i], a[j]))
        pls.append(tmp)

    # print(pls)
    if all(x > 2 for x in pls):
        print('No')
    else:
        print('Yes')
