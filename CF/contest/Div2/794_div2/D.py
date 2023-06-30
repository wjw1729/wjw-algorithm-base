def canmake(s,a,b,c,d):
    anum = s.count('A')
    bnum = s.count('B')

    cnum = s.count('AB')
    dnum = s.count('BA')

    if cnum < c or dnum < d or anum != a + c + d or bnum != b + c + d:
        return False

    n=len(s)

    ans=0

    abls=[]
    bals=[]
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
            abls.append((r-l+1)//2)

        if s[l]=='B' and s[r]=='A':
            bals.append((r-l+1)//2)


        l=r+1
    abls.sort()
    bals.sort()

    for i in abls:
        if i<=c:
            c-=i
        else:

            d-=i-c-1
            c = 0

    for i in bals:
        if i<=d:
            d-=i
        else:

            c-=i-d-1
            d = 0
            
    return (c+d)<=ans


t=int(input())

for _ in range(t):
    a,b,c,d=[int(x) for x  in input().split()]
    s=input()
    res=canmake(s,a,b,c,d)
    if res:
        print('YES')
    else:
        print('NO')