class Solution:
    def canChange(self, start: str, target: str) -> bool:

        n=len(start)

        if start.replace('_','')!=target.replace('_',''):
            return False

        cntr=[0]*n
        cntl=[0]*n

        r=0
        l=0
        for i in range(n-1,-1,-1):
            cntr[i]=r
            cntl[i]=l
            if target[i]=='L':
                l+=1

            if target[i]=='R':
                r+=1
        sr=[0]*n
        sl=[0]*n
        l=0
        r=0
        for i in range(n-1,-1,-1):
            sr[i]=r
            sl[i]=l
            if start[i]=='L':
                l+=1

            if start[i]=='R':
                r+=1

        return all((sl[i]>=cntl[i] and sr[i]<=cntr[i]) for i in range(n))

