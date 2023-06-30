

def trans(nums):

    res=[]
    for c in nums:
        tmp=c
        while tmp%m==0:
            tmp//=m

        if not res or tmp!=res[-1][0]:
            res.append([tmp,c//tmp])
        else:
            res[-1][1]+=c//tmp

    return res




t=int(input())
for _ in range(t):
    n,m=[int(x) for x  in input().split()]
    a=[int(x) for x  in input().split()]
    k=int(input())
    b=[int(x) for x in input().split()]


    ans=(trans(a)==trans(b))

    if ans:
        print('YES')
    else:
        print('NO')

