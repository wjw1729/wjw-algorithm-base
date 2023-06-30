t=int(input())

for _ in range(t):
    s=int(input())

    a=list(range(10))
    i=9
    ans=[]
    while s>a[i]:
        s-=a[i]
        ans.append(a[i])
        i-=1

    if s>0:
        ans.append(s)

    print(int(''.join(str(x) for x in ans[::-1])))
