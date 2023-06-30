
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:

        f=[0]*(forget+1)


        mod=10**9+7
        f[0]=1


        for i in range(n):

            f[forget]+=f[forget-1]
            for j in range(forget-1,1,-1):
                f[j]=f[j-1]


            f[0]=sum(f[x] for x in range(forget) if delay<=x<forget)


        return sum(f)%mod








