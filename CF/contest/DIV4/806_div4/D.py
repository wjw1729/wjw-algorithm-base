t=int(input())
for _ in range(t):
    n=int(input())
    sls=[]
    for _ in range(n):
        s=input()
        sls.append(s)

    sset=set(sls)

    res=[]
    for i in range(n):
        check=False
        for j in range(0,len(sls[i])+1):
            s=sls[i]
            if s[:j] in sset and s[j:] in sset:
                check=True
                break

        if check:
            res.append('1')
        else:
            res.append('0')

    print(''.join(res))





