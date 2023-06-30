from collections import Counter
class Solution:
    def dividePlayers(self, skill ) -> int:
        tt=sum(skill)
        n=len(skill)
        if (tt*2)%n!=0 or n%2==1:
            return -1

        tg=tt*2//n
        ans=0
        cnt=Counter(skill)
        for k,v in sorted(cnt.items()):
            if tg%2==0 and k==tg//2:
                if cnt[k]%2==0:
                    ans+=cnt[k]//2*(k*k)
                else:
                    return -1

            else:
                if cnt[k]!=cnt[tg-k]:
                    return -1
                else:

                    ans+=cnt[k]*(k*(tg-k))
                    cnt[k] = cnt[tg - k] = 0



        return ans

skill = [3,2,5,1,3,4]
res=Solution().dividePlayers(skill)
print(res)