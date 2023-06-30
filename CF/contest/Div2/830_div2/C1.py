
t=int(input())

for _ in range(t):
    n,q=[int(x) for x in input().split()]
    a=[int(x) for x in input().split()]
    for _ in range(q):
        l,r=[int(x) for x in input().split()]

    #按位思考
    M=30
    bit_cnt=[[] for _ in range(M)]
    res=[0,0]
    ans=0
    for ii,x in enumerate(a):
        l=ii
        tmp=0
        for i in range(M):
            if x&(1<<i):
                bit_cnt[i].append(ii)

            if len(bit_cnt[i])%2==1:
                if len(bit_cnt[i])>1:
                    l=min(l,bit_cnt[i][1])


            else:
                if bit_cnt[i]:
                    l=min(l,bit_cnt[i][0])
            p=len(bit_cnt[i]) // 2*2
            #print(p)
            tmp+=p*2**i
        #print(tmp,ii)
        #print(bit_cnt)
        if tmp>ans:
            res=[l,ii]
            ans=tmp
        elif tmp==ans:
            if ii-l<res[1]-res[0]:
                res=[l,ii]

    print(*[x+1 for x in res])





