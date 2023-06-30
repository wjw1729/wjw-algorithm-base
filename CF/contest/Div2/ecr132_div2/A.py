t = int(input())

for _ in range(t):
    x = int(input())
    a = [int(x) for x in input().split()]

    ans = 0
    x -= 1
    while x >= 0:

        ans += 1
        if a[x] == 0:
            break
        x = a[x]
        x -= 1
    if ans == 3:
        print('YES')
    else:
        print('NO')
