def minod(s,k):

    n=len(s)
    if k>=25:
        return 'a'*n

    s=[ord(c)-ord('a') for c in s]
    if k>=max(s):
        return 'a'*n

    pre=0
    for i,c in enumerate(s):
        if c>k:
            k-=pre
            stag=c
            break
        else:
            pre=max(pre,c)

    s=[x if x>pre else 0 for x in s]
    for i,c in enumerate(s):
        if stag-k<c<=stag:
            s[i]=stag-k

    return ''.join([chr(ord('a')+x) for x in s])


t=int(input())

for _ in range(t):
    n,k=[int(x) for x in input().split()]
    s=input()
    res=minod(s,k)
    print(res)
