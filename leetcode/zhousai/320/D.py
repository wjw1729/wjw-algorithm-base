class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        mod = 10 ** 9 + 7
        n = len(s)



        sls = []
        pls = {'2', '3', '5', '7'}
        for i in range(1, n - 1):
            if s[i] not in pls and s[i + 1] in pls:
                if i+1 < minLength or n - i - 1 < minLength:
                    continue
                sls.append(i)

        m = len(sls)

        f = [[0]*k for _ in range(m+1)]
        f[0][0] = 1

        g=[[0]*k for _ in range(m+1)]

        for i in range(m+1):
            g[i][0]=1
        for j in range(1,k):
            for i in range(j,m + 1):
                for jj in range(i - 1, -1, -1):
                    if sls[i-1]-(sls[jj-1] if jj-1>=0 else -1)>=minLength:
                        f[i][j] = g[jj][j - 1]
                        break
            for i in range(m + 1):
                g[i][j] = g[i - 1][j]+f[i][j]


        if k==1:
            if s[0] in pls and s[-1] not in pls:
                return 1
            else:
                return 0
        if not (s[0] in pls and s[-1] not in pls):
            return 0

        return g[-1][-1]%mod


s = "23542185131"
k = 3
minLength = 2
"""
s = "23542185131"
k = 3
minLength = 3
s="242538614532395749146912679859"
k=1
minLength=6
s="783938233588472343879134266968"
k=4
minLength=6

s="71892831976183763178768289335612558549523519189227897669537596687961579"
k=16
minLength=3
s="7753639519183359148598823162755335682921461647796985255166979917649578972791819356618496239687361868933775339936875893219782348459522657159781118588765368954599285197845124455559747963186111993765269"
k=24
minLength=2
"""
res = Solution().beautifulPartitions(s, k, minLength)
print(res)


