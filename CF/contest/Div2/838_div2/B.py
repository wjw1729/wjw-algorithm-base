import math

t=int(input())
for _ in range(t):
    n=int(input())
    a=[int(x) for x in input().split()]


    ans=[]

    als=list(enumerate(a))
    als.sort(key=lambda x:x[1])

    pre=als[0][1]
    for idx,i in als[1:]:
        pre=int(math.ceil(i/pre)*pre)
        ans.append((idx+1,pre-i))

    print(len(ans))
    for x in ans:
        print(*x)


