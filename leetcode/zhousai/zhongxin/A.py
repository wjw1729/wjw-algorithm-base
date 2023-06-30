from collections import Counter
p,q=[int(x) for  x in input().split()]

nums=[int(x) for x  in input().split()]

cnt=Counter(nums)

b=[int(x) for x in input().split()]

ans=[]
for c in b:
    if c in cnt:
        ans+=[c]*cnt[c]
        del cnt[c]

for k,v in sorted(cnt.items()):
    ans+=[k]*v

print(' '.join(str(x) for x  in ans))