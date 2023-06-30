"""
author:wjw
分析：从高到低考虑。
    考虑每个数时，不需要考虑后面比它小的数。因为如果存在比它小的数，无论释放前面还是放他后面对于他的ki都没有影响。
"""

class Solution:
    def reconstructQueue(self,people):
        people.sort(key=lambda x:(-x[0],x[1]))

        ans=[]
        for person in people:
            ans.insert(person[1],person)

        return ans

people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
people=[[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
res=Solution().reconstructQueue(people)
print(res)