t= int(input())

for _ in range(t):
    n=int(input())
    #a = [int(x) for x in input().split()]

    ans=n//3
    l=n%3
    if l==0:
        print(ans)
    elif l==1:
        if ans==0:
            ans=2
        else:
            ans+=1
        print(ans)
    else:
        ans+=1
        print(ans)

