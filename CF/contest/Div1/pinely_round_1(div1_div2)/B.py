from collections import Counter
t=int(input())

for _ in range(t):
    n=int(input())
    a=[int(x) for x in input().split()]

    cnt=Counter(a)

    if max(cnt.values())==1:
        print(n)
    elif len(cnt)>2:
        print(n)
    else:
        print(n//2+1)

