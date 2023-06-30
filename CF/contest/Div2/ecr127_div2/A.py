

def canbuild(s):

    n=len(s)
    l=0
    r=1
    while r<=n:
        while r<n and s[r]==s[r-1]:
            r+=1

        if len(s[l:r])<2:
            return False
        l=r
        r+=1

    return True

t=int(input())
for _ in range(t):
    s=input()
    if canbuild(s):
        print('YES')
    else:
        print('NO')



