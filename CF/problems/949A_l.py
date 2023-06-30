

from collections import deque

def zebras(s):

    zbs=[]
    alzbs=[]

    for i in range(n):
        if s[i]=='0':
            if not alzbs:
                zbs.append([i+1])
            else:
                tmp=alzbs.pop()
                tmp.append(i+1)
                zbs.append(tmp)

        else:
            if not zbs:
                return -1,None

            tmp=zbs.pop()
            tmp.append(i+1)
            alzbs.append(tmp)

    if alzbs:
        return -1,None

    return 1,zbs



s=input()
n=len(s)
num0=s.count('0')
num1=s.count('1')

if num0-num1<1:
    print(-1)
else:
    res=zebras(s)
    if res[0]==-1:
        print(-1)
    else:
        print(len(res[1]))
        for x  in res[1]:
            print(len(x),*x)



