
from collections import defaultdict

def triple(nums):
    counter=defaultdict(int)
    for c in nums:
        counter[c]+=1

    ans=[]

    for k,v in counter.items():
        if v>=3:
            ans.append(k)


    return ans


t=int(input())

for _ in range(t):
    n=int(input())
    nums=[int(x) for  x in input().split()]
    res=triple(nums)
    print(res[0] if res else -1)



