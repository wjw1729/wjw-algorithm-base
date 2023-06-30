import io, os
from collections import deque

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


def main(t):
    n = int(input())
    parent = list(map(int, input().split()))

    for i in range(n - 1):
        parent[i] -= 1
    parent = [-1] + parent

    children = [[] for _ in range(n)]
    for i in range(1, n):
        children[parent[i]].append(i)

    maximum = [0] * n
    minimum = [0] * n
    for i in range(n):
        minimum[i], maximum[i] = map(int, input().split())

    queue = deque()
    queue.append(0)
    seq = []
    while queue:
        index = queue.popleft()
        seq.append(index)
        for nextindex in children[index]:
            queue.append(nextindex)

    curr = [0] * n
    ans = [0] * n

    for index in seq[::-1]:
        if len(children[index]) == 0:
            ans[index] = 1
            curr[index] = maximum[index]
            continue

        for nextindex in children[index]:
            curr[index] += curr[nextindex]
            ans[index] += ans[nextindex]

        if curr[index] > maximum[index]:
            curr[index] = maximum[index]

        elif curr[index] < minimum[index]:
            curr[index] = maximum[index]
            ans[index] += 1

    #    print(ans)

    print(ans[0])


T = int(input())
t = 1
while t <= T:
    main(t)
    t += 1
