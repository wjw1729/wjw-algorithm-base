def gcd(a,b):
    return b if a%b else gcd(b,a%b)
import copy
class Solution:
    def distinctSequences(self, n: int) -> int:



        if n==1:
            return 6


        f=[[0]*6 for _ in range(6)]

        for j in range(6):
            for k in range(6):
                if gcd(j + 1, k + 1) != 1 or j == k:
                    f[j][k] = 0
                else:
                    f[j][k] = 1




        for i in range(n-2):
            g=[[0]*6 for _ in range(6)]
            for j in range(6):
                for k in range(6):
                    if gcd(j+1,k+1)!=1 or j==k:
                        g[j][k]=0
                    else:
                        g[j][k]=sum(f[k][m] for m in range(6) if m!=j )


            f=copy.deepcopy(g)



        return sum(sum(x) for x in f)




