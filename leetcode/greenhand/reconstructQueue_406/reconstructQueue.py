"""
author:wjw
分析：从低到高进行考虑。
"""

class Solution:
    def reconstructQueue(self,people):

        n=len(people)
        people.sort(key=lambda x:(x[0],-x[1]))

        ans=[[] for _ in range(n) ]

        for person in people:
            index=person[1]+1

            for i in range(n):
                if not ans[i]:
                    index-=1
                if index==0:
                    ans[i]=person
                    break

        return ans

people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
people=[[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
res=Solution().reconstructQueue(people)
print(res)
