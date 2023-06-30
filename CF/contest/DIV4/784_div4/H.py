

def maxand(nums,k):

    cnt=[0]*31

    for num in nums:
        for j in range(31):
            if num & (1<<j):
                cnt[j]+=1

    ans=0
    for j in range(30,-1,-1):
        if k>=n-cnt[j]:
            k-=n-cnt[j]
            ans+=1<<j

    return ans


t=int(input())
for _ in range(t):
    n,k=[int(x) for  x  in input().split()]
    nums=[int(x) for  x  in input().split()]
    print(maxand(nums,k))