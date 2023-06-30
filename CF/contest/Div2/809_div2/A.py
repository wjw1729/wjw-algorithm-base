

t=int(input())

for _ in range(t):
    n,m=[int(x) for x in input().split()]
    a=[int(x) for x in input().split()]

    s=['B']*m
    for c in a:
        if c>m+1-c:
            c=m+1-c
        if s[c-1]=='B':
            s[c-1]='A'
        elif s[m-c]=='B':
            s[m-c]='A'


    print(''.join(s))

