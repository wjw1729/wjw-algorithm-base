

n=int(input())
ans=[0]*n
tt=None
pre=None
for i in range(n-1):
    print('?',i+1,n,flush=True)

    now=int(input())
    if tt==None:
        tt=now

    if pre!=None:
        ans[i-1]=pre-now

    pre=now


print('? 1',n-1,flush=True)
ans[-1]=tt-int(input())

ans[-2]=tt-sum(ans)


print('!',*ans,flush=True)