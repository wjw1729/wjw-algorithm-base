

t=int(input())
for _ in range(t):
    n=int(input())
    a=[int(x) for  x in input().split()]

    cnt=[0]*10
    for c in a:
        cnt[c%10]+=1


    def dfs(idx,t):
        if idx==2 :
            return cnt[t]>0


        for i in range(10):
            if cnt[i]<1:
                continue

            cnt[i]-=1
            if dfs(idx+1,t-i if t>=i else t-i+10):
                return True
            cnt[i]+=1
        return False


    ans=dfs(0,3)
    if ans:
        print('YES')
    else:
        print('NO')
