"""
author:wjw
分析:没啥技巧，没有playground，不好调试。有时间自己写，，，，写完调试
"""


class Employee:
    def __init__(self, id, importance, subordinates):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


def find_id(employees,id):
    for i in range(len(employees)):
        if employees[i].id==id:
            return employees[i]


class Solution:
    def getImportance(self, employees, id: int) -> int:
        yuangong = find_id(employees,id)
        sum = 0
        need_add = [id]
        k = 0
        while k < len(need_add):
            sum += yuangong.importance
            for i in yuangong.subordinates:
                need_add.append(i)
            k = k + 1
            if k >= len(need_add):
                break
            yuangong = find_id(employees,need_add[k])
        return sum


employees = []
id =

res = Solution().getImportance(employees, id)
print(res)
