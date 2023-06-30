
def interoutput(l,r):
    print('?',l,r,flush=True)
    return


def interinput():
    return int(input())



n,t=[int(x) for x  in input().split()]
k=interinput()
l=1
r=n

while 1:
    mid=(l+r)//2
    interoutput(l,mid)
    a=interinput()
    b=(mid-l+1)-a
    if l==r and k==b==1:
        ans=l
        break

    if b>=k:
        r=mid
    else:
        k-=b
        l=mid+1

print('!',ans,flush=True)