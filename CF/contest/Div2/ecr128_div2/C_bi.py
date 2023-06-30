
def can(pos,c):
    left_1=len(pos)-c
    m=len(pos)
    for i in range(m):
        if i+left_1-1>=m:
            break
        lp=pos[i]
        rp=pos[i+left_1-1]
        if rp-lp+1-left_1<=c:
            return True

    return False



def solve(s):
    n=len(s)
    pos=[i for i,c in enumerate(s) if c=='1']

    m=len(pos)
    if m<=1 or pos[-1]-pos[0]+1==m:
        return 0

    l=0
    r=m
    ans=n
    while l<=r:
        mid=(l+r+1)//2
        if can(pos,mid):
            ans=mid
            r=mid-1
        else:
            l=mid+1

    return ans






t=int(input())
for _ in range(t):
    s=input()
    res=solve(s)
    print(res)