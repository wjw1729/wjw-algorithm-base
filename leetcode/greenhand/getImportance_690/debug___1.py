"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
import logging


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        yuangong = employees[id - 1]
        sum = 0
        need_add = [id]
        k = 0
        while k < len(need_add):
            sum += yuangong.importance
            for i in yuangong.subordinates:
                print(i)
                need_add.append(i)
            k = k + 1
            if k >= len(need_add):
                break
            try:
                yuangong = employees[need_add(k) - 1]
            except Exception as e:
                print(need_add[k])
                logging.exception(e)

        return sum