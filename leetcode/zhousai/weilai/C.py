from collections import defaultdict
class Solution:
    def buildTransferStation(self, area) -> int:

        rls=[]
        cls=[]


        m=len(area)
        n=len(area[0])
        for i in range(m):
            for j in range(n):
                if area[i][j]==1:
                    rls.append(i)
                    cls.append(j)

        rls.sort()
        cls.sort()

        ans=float('inf')

        for i in range(m):
            tmp=0
            for c in rls:
                tmp+=abs(c-i)
            if tmp<ans:
                xls=[i]
                ans=tmp
            elif tmp==ans:
                xls.append(i)

        ans=float('inf')
        for j in range(n):
            tmp=0
            for c in cls:
                tmp+=abs(c-j)
            if tmp<ans:
                yls=[j]
                ans=tmp
            elif tmp==yls:
                yls.append(j)

        ans=float('inf')
        for x in xls:
            for y in yls:
                tmp=0
                for i in range(m):
                    for j in range(n):
                        if area[i][j]==1:
                            tmp+=abs(i-x)+abs(j-y)

                ans=min(ans,tmp)

        return ans





        return ans

area = [[0,1,0,0,0],[0,0,0,0,1],[0,0,1,0,0]]
res=Solution().buildTransferStation(area)
print(res)