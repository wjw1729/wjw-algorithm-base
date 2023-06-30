

def print3d(ls1,ls2,ls3):

    ans=[min(ls1[i],ls2[i],ls3[i]) for i in range(4)]

    if sum(ans)<10**6:
        return False

    ans[0]=ans[0]
    ans[1]=min(ans[1],10**6-ans[0])
    ans[2]=min(ans[2],10**6-ans[0]-ans[1])
    ans[3]=min(ans[3],10**6-sum(ans[0:3]))

    return ans


n=int(input())

for i  in range(n):
    ls1=[int(x) for x in input().strip().split()]
    ls2=[int(x) for x in input().strip().split()]
    ls3=[int(x) for x in input().strip().split()]
    res=print3d(ls1,ls2,ls3)
    if res==False:
        print('Case #%d: IMPOSSIBLE'%(i+1))
    else:
        print('Case #%d: %d %d %d %d'%(i+1,res[0],res[1],res[2],res[3]))


