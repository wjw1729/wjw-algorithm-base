

class Solution:

    def maxPalindromes(self, s: str, k: int) -> int:
        def manacher(s,kk):

            n = len(s)
            news = '#'.join(list(s))
            news = '#' + news + '#'

            center = 0
            maxlen = 0
            d1 = [0] * (2 * n + 1)
            l = 0
            r = -1
            for i in range(2 * n + 1):
                k = 1 if i > r else min(d1[l + r - i], r - i + 1)

                while i - k >= 0 and i + k < 2 * n + 1 and news[i - k] == news[i + k]:
                    k += 1

                if k > maxlen:
                    center = i
                    maxlen = k

                d1[i] = k
                k -= 1
                if i + k > r:
                    l = i - k
                    r = i + k


            k=kk
            ans=0
            pre=-1
            pls=[]
            for i in range(2*n+1):
                if i%2==0:#'#'
                    tk=k if k%2==0 else k+1
                    if 2*d1[i]-1>=2*k+1 and i-tk+1>pre:
                        ans+=1
                        pre=i+tk-1
                        pls.append(i)
                        #print(pre)

                else:# s
                    tk=(kk//2)*2+1
                    if 2*d1[i]-1>=2*k+1 and i-tk+1>pre:
                        ans+=1
                        pre=i+tk-1
                        pls.append(i)
                        #print(pre)

            return ans

        return manacher(s,k)


s = "abaccdbbd"
s = "adbcda"
k = 2

s="fttfjofpnpfydwdwdnns"
k=2

res=Solution().maxPalindromes(s,k)
print(res)

