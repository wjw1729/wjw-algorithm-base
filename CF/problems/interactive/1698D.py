def interoutput(l,r):
    print('?',l,r,flush=True)
    return

def interinput():
    return [int(x) for x in input().split()]



t=int(input())

for _ in range(t):
    n=int(input())
    l=1
    r=n
    while 1 :


        mid=(l+r)//2
        interoutput(l,mid)
        a=interinput()


        cnt=0
        for c in a:
            if l<=c<=mid:
                cnt+=1

        if cnt%2==1:
            r=mid
        else:
            l=mid+1

        if l==r:
            break

    ans=interoutput(l,r)
    ans=interinput()[0]
    print('!',ans,flush=True)
