

t=int(input())
for _ in range(t):
    n=int(input())

    res=n%3
    ans=[n//3]*3
    ans[1] += 1
    ans[2] -= 1
    if res==0:
        pass

    elif res==1:
        ans[1]+=1

    else:
        ans[0]+=1
        ans[1]+=1

    print(*ans)

