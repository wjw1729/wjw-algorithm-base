import math
class Solution:
    def splitMessage(self, message: str, limit: int) :

        def l(b):
            return len(str(b))

        def get(s,b):
            ans=[]
            l=0
            for i in range(1,b+1):
                suf='<'+str(i)+'/'+str(b)+'>'
                ans.append(s[l:l+limit-len(suf)]+suf)
                l+=limit-len(suf)
            return ans


        st=(len(message)-1)//limit+1

        f=[0]*(10**5)
        for i in range(1,10**5):
            f[i]=f[i-1]+l(i)-1


        for i in range(st,10**5):
            tmp=len(message)+(l(i)-1)*i+f[i]+5*i

            if int(math.ceil(tmp/limit))==i:
                print(tmp)
                print(i)

                return get(message,i)

        return []









message = "this is really a very awesome message"
limit = 9
res=Solution().splitMessage(message,limit)