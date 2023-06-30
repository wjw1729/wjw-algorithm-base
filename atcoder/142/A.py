from collections import deque

n, k = [int(x) for x in input().split()]

if n < k or int(str(k)[::-1])<k:
    print(0)
else:
    ans = 0
    q = deque()
    q.append(k)

    vis = set()
    vis.add(k)
    while q:
        num = q.popleft()

        ans += 1

        tmp1 = num * 10
        if tmp1 <= n and tmp1 not in vis:
            q.append(tmp1)
            vis.add(tmp1)

        tmp2 = int(str(num)[::-1])
        if tmp2 <= n and tmp2 not in vis:
            q.append(tmp2)
            vis.add(tmp2)

    print(ans)
