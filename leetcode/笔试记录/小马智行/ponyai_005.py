n = int(input().strip())

adjcost = []

for i in range(n):
    tmp = [int(x) for x in input().strip().split()]
    adjcost.append(tmp)

target = [int(x) for x in input().strip().split()]


def minTime(adjcost, target):
    a, b, k = target

    def check(x):
        nonlocal a, b, k
        for i in range(n):
            for j in range(i + 1, n):
                tmp = min(adjcost[i][j], adjcost[i][a] + x + adjcost[b][j], adjcost[i][b] + x + adjcost[a][j])
                if tmp+x >= k:##############为什么要加个x啊？？？？？？？？？？？？？
                    return False
        return True

    left = 0
    right = k
    ans = -1
    while left <= right:
        mid = (left + right + 1) // 2
        if check(mid):
            left = mid + 1
            ans = max(ans, mid)
        else:
            right = mid - 1
    return ans


res = minTime(adjcost, target)
print(res)
