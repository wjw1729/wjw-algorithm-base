

n=int(input())

ans=[-1]*n

idx=0
for i in range(1,n):

    print('?',idx+1,i+1,flush=True)
    a=int(input())

    print('?',i+1,idx+1,flush=True)
    b=int(input())

    if a<b:
        ans[i]=b
    else:
        ans[idx]=a
        idx=i

ans[idx]=n
print('!',*ans,flush=True)


