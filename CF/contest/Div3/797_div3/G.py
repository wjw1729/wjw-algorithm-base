

t=int(input())

for _ in range(t):
    input()
    n,m=[int(x) for x  in input().split()]
    a=[int(x) for  x in input().split()]

    ops=[]
    for i in range(m):
        k,d=[int(x) for x in input().split()]
        ops.append((k,d))
        a[k-1]=max(0,a[k-1]-d)


    cnt=1
    pre=a[0]
    b=[0]*n
    b[0]=a[0]
    for i in range(1,n):
        if a[i]>=pre:
            b[i]=pre
            continue
        else:
            pre=a[i]
            b[i]=pre
            cnt+=1

    ans = [cnt]

    for k,d in ops[n-1:0:-1]:
        pre=a[k-1]
        a[k-1]+=d
        if k-2>=0:
            b[k-1]=min(a[k-1],b[k-2])
        else:
            b[k-1]=a[k-1]

        if (1<k<n and b[k-2]>pre>b[k] and b[k-2]<=b[k-1]) or (k==n  and b[k-2]>pre and b[k-1]>=b[k-2]) :
            cnt-=1
        elif (1<k<n and b[k-2]>pre and pre<=b[k] and b[k-2]>b[k-1]>b[k]) or  (k==1 and pre <=b[k] and b[k-1]>b[k]):
            cnt+=1


        ans.append(cnt)

    print(*ans[::-1])








