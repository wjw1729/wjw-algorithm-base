
t=int(input())
for _ in range(t):
    n=int(input())
    s=input()

    t=int(s[0])
    ans=[]

    for x in s[1:]:
        if x=='0':
            ans.append('+')
        else:
            if t>0:
                ans.append('-')
                t-=1
            else:
                ans.append('+')
                t+=1

    print(''.join(ans))
