from collections import defaultdict
def lefts(s):
    cnt=defaultdict(int)
    for c in s:
        cnt[c]+=1

    for i,c in enumerate(s):
        if cnt[c]>=2:
            cnt[c]-=1
        else:
            return s[i:]





t=int(input())
for _ in range(t):
    s=input()
    print(lefts(s))


