class Solution:
    def matchReplacement(self, s: str, sub: str, mappings) :

        n=len(s)
        m=len(sub)
        vis=set(tuple(x) for  x in mappings)



        for i in range(n-m+1):

            check=True
            for j in range(m):
                if s[i+j]==sub[j]:
                    continue
                else:
                    if (sub[j],s[i+j]) not in vis:
                        check= False
                        break
            if check:
                return True

        return False


