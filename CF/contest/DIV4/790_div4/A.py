



t=int(input())

for _ in range(t):
    s=[int(x) for x  in input()]

    tmp=sum(s[:3])==sum(s[3:])
    if tmp:
        print('YES')
    else:
        print('NO')
