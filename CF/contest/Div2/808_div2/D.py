
from collections import Counter



t=int(input())

for _ in range(t):
    n=int(input())
    a=[int(x) for x in input().split()]

    def solve():
        cnt=Counter(a)

        cnt=sorted(cnt.items())

        for _ in range(n-1):
            ncnt=Counter()
            for k,v in cnt:
                if v>1:
                    ncnt[0]+=v-1

            for i in range(1,len(cnt)):
                ncnt[cnt[i][0]-cnt[i-1][0]]+=1

            cnt=sorted(ncnt.items())

        print(cnt[0][0])

    solve()

