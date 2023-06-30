def canmake(s):
    anum = s.count('A')
    bnum = s.count('B')

    cnum = s.count('AB')
    dnum = s.count('BA')

    if cnum < c or dnum < d or anum != a + c + d or bnum != b + c + d:
        return False

    n=len(s)

    ans=0

    l=0
    while l<n:
        while l<n-1 and  s[l]==s[l+1]:
            l+=1

        r=l
        while r<n-1 and s[r]!=s[r+1]:
            r+=1

        if s[l]== s[r]=='B':
            ans+=(r-l+1)//2
        if s[l]==s[r]=='A':
            ans+=(r-l+1)//2

        if s[l]=='A' and s[r]=='B':
            tmp=(r-l+1)//2
            if tmp<=c:
                c-=tmp
            else:
                d-=tmp-c-1

        if s[l]=='B' and s[r]=='A':
            tmp=(r-l+1)//2
            if tmp<=d:
                d-=tmp
            else:
                d=0
                c-=(tmp-d-1)

        if c==0 and d==0:
            break
        l=r+1



    return c==0 and d==0


t=int(input())

for _ in range(t):
    a,b,c,d=[int(x) for x  in input().split()]
    s=input()
    res=canmake(s)
    if res:
        print('YES')
    else:
        print('NO')