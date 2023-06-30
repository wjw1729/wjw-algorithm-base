from collections import deque

def zebras(s):
    preidx = []
    afteridx = deque()
    for i in range(n-1,-1,-1):
        if s[i]=='0':
            afteridx.append(i+1)
    ans = []
    tmp = []
    vis=set()
    for i in range(n):
        if s[i] == '0':
            preidx.append(i + 1)

        else:
            if s[i - 1] == '0':
                if preidx:
                    tmp.append(preidx.pop())
                    tmp.append(i+1)
                else:
                    return -1,None
            else:

                while afteridx and afteridx[-1]<=i+1:
                    afteridx.pop()

                if not afteridx:
                    return -1,None
                aidx=afteridx.popleft()
                vis.add(aidx)
                tmp.append(aidx)
                ans.append(tmp)

                if not preidx:
                    return -1,None
                tmp=[]
                tmp.append(preidx.pop())
                tmp.append(i+1)
    if tmp:
        while afteridx and afteridx[-1] <= tmp[-1]:
            afteridx.pop()

        if not afteridx:
            return -1, None
        aidx = afteridx.popleft()
        vis.add(aidx)
        tmp.append(aidx)
        ans.append(tmp)
    if preidx:
        ans+=[[x] for x  in preidx if x not in vis]



    return 1,ans




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



