
def interinput():
    return int(input())

def interoutput(l,r):
    print('?',l,r,flush=True)
    return


n=int(input())
l=1
r=n

while 1:
    mid=(l+r)//2
    interoutput(l,r)
    idx2=interinput()
    if r-l+1==2:
        ans=l if idx2==r else r
        break
    elif r-l+1==3:
        if idx2==l:
            interoutput(l+1,l+2)
            p=interinput()
            ans=l+2 if p==l+1 else l+1

        elif idx2==l+1:
            interoutput(l + 1, l + 2)
            p = interinput()
            if p==idx2:
                ans=l+2
            else:
                ans=l
        else:
            interoutput(l+1,l+2)
            p=interinput()
            if p==idx2:
                ans=l+1
            else:
                ans=l
        break




    if idx2<=mid:
        interoutput(l,mid)
        p=interinput()
        if p==idx2:
            r=mid
        else:
            l=mid+1
    else:
        interoutput(mid+1,r)
        p=interinput()
        if p==idx2:
            l=mid+1
        else:
            r=mid

print('!',ans,flush=True)








