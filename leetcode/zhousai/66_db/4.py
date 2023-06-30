from collections import deque, defaultdict
class Solution:
    def findAllPeople(self, n: int, meetings, firstPerson: int) :
        person = [0] * n
        person[0] = 1
        person[firstPerson] = 1
        meetings.sort(key=lambda x: (x[2]))

        ans = {0, firstPerson}

        m = len(meetings)
        idx = 0
        while idx < m:
            x, y, t = meetings[idx]
            tmpset = {x, y}
            edges = defaultdict(list)
            edges[x].append(y)
            edges[y].append(x)
            idx += 1
            while idx < m and meetings[idx][2] == t:
                tmpset.add(meetings[idx][0])
                tmpset.add(meetings[idx][1])
                edges[meetings[idx][0]].append(meetings[idx][1])
                edges[meetings[idx][1]].append(meetings[idx][0])
                idx += 1

            queue = deque(list(ans & tmpset))
            while queue:
                node = queue.popleft()
                for v in edges[node]:
                    person[v] = 1
                    if v not in ans:
                        queue.append(v)
                    ans.add(v)
        return list(ans)


n=12
meetings=[[10,8,6],[9,5,11],[0,5,18],[4,5,13],[11,6,17],[0,11,10],[10,11,7],[5,8,3],[7,6,16],[3,6,10],[3,11,1],[8,3,2],[5,0,7],[3,8,20],[11,0,20],[8,3,4],[1,9,4],[10,7,11],[8,10,18]]
firstPerson=9
res=Solution().findAllPeople(n,meetings,firstPerson)
print(res)