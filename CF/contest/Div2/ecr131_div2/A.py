
t=int(input())

for _ in range(t):
    a=0
    for i in range(2):
        a+=sum([int(x) for x in input().split()])

    if a==0:
        print(0)
    elif a==4:
        print(2)
    else:
        print(1)


