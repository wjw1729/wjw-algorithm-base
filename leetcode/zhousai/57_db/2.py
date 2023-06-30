"""
author:wjw
分析：
"""
from sortedcontainers import SortedList


class Solution:
    def smallestChair(self, times, targetFriend) -> int:

        n = len(times)
        exittimes = [(i, times[i][1]) for i in range(n)]
        times = list(enumerate(times))
        times.sort(key=lambda x: (x[1][0], x[1][1]))

        end = times[-1][1][0]
        hashmap = {True: SortedList(range(n)), False: SortedList([])}

        placemap = {}

        friendnum = 0

        exittimes.sort(key=lambda x:x[1])
        exitfriend = 0
        for t in range(end + 1):

            while exittimes[exitfriend][1] <= t:
                place = placemap[exittimes[exitfriend][0]]
                hashmap[False].remove(place)
                hashmap[True].add(place)

                exitfriend+=1

            while times[friendnum][1][0] <= t:
                place = hashmap[True].pop(0)
                if times[friendnum][0]==targetFriend:
                    return place

                hashmap[False].add(place)
                placemap[times[friendnum][0]] = place

                friendnum+=1


times = [[1,4],[2,3],[4,6]]
targetFriend = 1
times = [[3,10],[1,5],[2,6]]
targetFriend = 0
"""
times=[[33889,98676],[80071,89737],[44118,52565],[52992,84310],[78492,88209],[21695,67063],[84622,95452],[98048,98856],[98411,99433],[55333,56548],[65375,88566],[55011,62821],[48548,48656],[87396,94825],[55273,81868],[75629,91467]]
targetFriend=6
"""
res=Solution().smallestChair(times,targetFriend)
print(res)