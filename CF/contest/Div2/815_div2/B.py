
t=int(input())

for _ in range(t):
    n=int(input())
    a=[int(x) for  x in input().split()]


    m1=max(range(n),key=lambda x:a[x])
    m2=max(list(range(m1))+list(range(m1+1,n)),key=lambda x:a[x])

    n1=min(range(n),key=lambda x:a[x])
    n2=min(list(range(n1))+list(range(n1+1,n)),key=lambda x:a[x])


    print(a[m1]+a[m2]-a[n1]-a[n2])



