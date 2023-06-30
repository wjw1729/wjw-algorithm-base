class Solution:
    def substringXorQueries(self, s: str, queries) :

        ans=[]
        for fi,se in queries:
            val=fi^se
            ts=bin(val)[2:]
            idx=s.find(ts)
            if idx==-1:

                ans.append((idx,idx+len(ts)))
            else:
                ans.append((-1,-1))

        return ans

