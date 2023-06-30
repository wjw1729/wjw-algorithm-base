from collections import Counter, defaultdict
import heapq

n, m, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]


def solve():
    """
    hq1 = []
    hq2 = []
    for k, v in cnt.items():
        if v > 0:
            heapq.heappush(hq1, (k, v))
        if v < 0:
            heapq.heappush(hq2, (k, v))

    while hq1 and hq2:
        k1, v1 = heapq.heappop(hq1)

        while hq2 and hq2[0][0] < k1:
            k2, v2 = heapq.heappop(hq2)
        if hq2:

            k2, v2 = heapq.heappop(hq2)
        else:
            break

        if v1 < -v2:
            heapq.heappush(hq2, (k2, v2 + v1))
        elif v1 > -v2:
            heapq.heappush(hq1, (k1, v1 + v2))

    if hq1:
        return True
    else:
        return False
    """
    a.sort(reverse=True)
    b.sort(reverse=True)

    for i in range(min(len(a), len(b))):
        if a[i] > b[i]:
            return True

    return len(a) > len(b)


if solve():
    print('YES')
else:
    print('NO')
