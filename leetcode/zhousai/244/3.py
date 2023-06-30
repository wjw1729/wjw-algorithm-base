#计算海明距离。最小


def countHam(s,target):
    sum= s^ target
    return bin(sum).count('1')

class Solution:
    def minFlips(self, s: str) -> int:

        n=len(s)
        t1=''
        t2=''
        for i in range(n):
           if i%2==0:
                t1+='0'
                t2+='1'
           else:
                t1+='1'
                t2+='0'

        s=int(s,base=2)
        res=min(countHam(s,int(t1,base=2)),countHam(s,int(t2,base=2)))

        return res


s="01001001101"
res=Solution().minFlips(s)
print(res)
