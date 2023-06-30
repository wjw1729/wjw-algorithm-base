t = int(input())
for _ in range(t):
    n, h = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]

    s2 = 2
    s3 = 1
    a.sort()
    i = 0
    cnt1 = a.count(1)
    a = [x for x in a if x != 1]

    for x in a:
        if h > x:
            pass
        elif s2 > 0 and h * 2 > x:
            s2 -= 1
            h *= 2
        elif s3 > 0 and h * 3 > x:
            s3 -= 1
            h *= 3
        elif s2 > 1 and h * 4 > x:
            s2 -= 2
            h *= 4
        elif s2 > 0 and s3 > 0 and h * 6 > x:
            s2 -= 1
            s3 -= 1
            h *= 6
        elif s2 > 1 and s3 > 0 and h * 12 > x:
            s2 -= 2
            s3 -= 1
            h *= 12

        if h > x:
            h += x // 2
            i += 1
        else:
            break
    h *= (2 ** s2) * (3 ** s3)
    if h > 1:
        i += cnt1
    print(i)
