


def gettree(s):

    odsum=s.count('1')

    if odsum==0 or odsum%2!=0:
        return False,None

    lr=None
    for i in range(n):
        if s[i]=='1' and s[(i+1)%n]=='0':
            lr=i
            break

    pls=[(i+1,c) for i,c in enumerate(s)]
    if lr!=None:
        pls=pls[(lr+1)%n:]+pls[:(lr+1)%n]




    ans=[]
    for i in range(n-1,0,-1):
        if pls[i-1][1]!='1':
          ans.append((pls[i][0],pls[i-1][0]))
        else:
            ans.append((pls[i][0],pls[0][0]))

    return True,ans



t=int(input())

for _ in range(t):
    n=int(input())
    s=input()
    res=gettree(s)
    if not res[0]:
        print('NO')
    else:
        print('YES')
        for v in res[1]:
            print(*v)



