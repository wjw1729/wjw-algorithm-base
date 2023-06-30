
t=int(input())

for _ in range(t):
    input()
    pls=[]
    pls.append([int(x) for x in input().split()])
    pls.append([int(x) for x in input().split()])
    pls.append([int(x) for x in input().split()])

    if len(set(x[1] for x in pls))<=2 and len(set(x[0] for x in pls))<=2:
        print('NO')
    else:
        print('YES')

