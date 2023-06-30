def maxprod(nums):



    def nozeroseq(nums):
        n=len(nums)
        pre=[1]*(n+1)
        for i in range(1,n+1):
            pre[i]=pre[i-1]*nums[i-1]

        total=pre[n]
        if total>0:
            return 0,0,total

        suf=[1]*(n+1)
        for i in range(1,n+1):
            suf[i]=suf[i-1]*nums[n-i]

        maxl=(0,0)
        maxr=(0,0)
        for i in range(n+1):
            if maxl==(0,0) and pre[i]<0:
                maxl=(i,pre[i])
            if maxr==(0,0) and suf[i]<0:
                maxr=(i,suf[i])
            if maxl!=(0,0) and maxr!=(0,0):
                break
        if maxl[1]<maxr[1]:
            return (0,maxr[0],total//maxr[1])
        else:
            return maxl[0],0,total//maxl[1]

    n=len(nums)
    indices=[-1]
    for i,c in enumerate(nums):
        if c==0:
            indices.append(i)
    indices.append(n)

    ans=[n,0,1]

    for i in range(1,len(indices)):
        nnums=nums[indices[i-1]+1:indices[i]]
        tans=nozeroseq(nnums)

        if tans[2]>ans[2]:
            ans[0]=indices[i-1]+1+tans[0]
            ans[1]=n-indices[i]+tans[1]
            ans[2]=tans[2]

    return ans[0],ans[1]


t=int(input())
for _ in range(t):
    _=input()
    nums=[int(x) for x in input().split()]
    print(' '.join( str(x) for x in maxprod(nums)))








