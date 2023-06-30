
def maxstring(dicels):

    dicels.sort()
    ans=0
    for i in dicels:
        if i>ans:
            ans+=1

    return ans



n=int(input())
for i in range(n):
    m=input()
    dicels=[int(x) for x in input().strip().split()]
    res=maxstring(dicels)
    print('Case #%d: %d'%(i+1,res))



