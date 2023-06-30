import random

def biaocheng(boxes):
    n = len(boxes)
    ans = [0] * n

    for i in range(n):
        tmp = 0
        for j in range(n):
            tmp += abs(i - j) * boxes[j]
        ans[i] = tmp

    return ans


def minOperations(boxes):
    n = len(boxes)
    ans = [0] * n

    pre = [0] * (n + 1)
    for i in range(1, n + 1):
        pre[i] = pre[i - 1] + boxes[i - 1]

    tmp = 0
    for i in range(1, n):
        tmp += boxes[i] * i
    ans[0] = tmp

    for i in range(1, n):
        tmp += pre[i] - (pre[n] - pre[i])
        ans[i] = tmp

    return ans



t=int(input())

for _ in range(t):
    n=random.randint(1,2000)
    boxes=[0]*n
    for i in range(n):
        boxes[i]=random.randint(1,100)

    ans1=biaocheng(boxes)
    ans2=minOperations(boxes)
    if ans1==ans2:
        print('YES')
    else:
        print('NO')

