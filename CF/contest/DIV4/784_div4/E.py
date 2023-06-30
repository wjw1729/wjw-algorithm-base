
from collections import Counter

def howmanypairs(sls):
    first=[0]*(ord('k')-ord('a')+1)
    second=[0]*(ord('k')-ord('a')+1)

    counter=Counter(sls)

    for s in sls:
        first[ord(s[0])-ord('a')]+=1
        second[ord(s[1])-ord('a')]+=1

    ans=0
    for c in first:
        ans+=c*(c-1)//2
    for c in second:
        ans+=c*(c-1)//2

    for k,v  in counter.items():
        ans-=v*(v-1)

    return ans

t=int(input())
for _ in range(t):
    sls=[]
    n=int(input())
    for i in range(n):
        sls.append(input())
    print(howmanypairs(sls))