from collections import deque,defaultdict
class Solution:
    def metroRouteDesignI(self, lines, start: int, end: int) :

        n = len(lines)

        graph = defaultdict(dict)

        lineset = [set(x) for x in lines]

        for i in range(n):
            for j in range(i + 1, n):
                linknode = set(lines[i]) & set(lines[j])

                if linknode != set():
                    graph[i][j] = list(linknode)
                    graph[j][i] = list(linknode)

        targetline = []
        startline = []

        for i in range(n):
            if start in lineset[i]:
                startline.append(i)
            if end in lineset[i]:
                targetline.append(i)

        times = float('inf')
        res=[]
        for startl in startline:
            queue = deque()
            queue.append((startl, [startl]))

            while queue:
                u, path = queue.popleft()

                if u in targetline:
                    res.append(path[:])
                    times = min(times, len(path))

                if len(path) > times:
                    break

                for v in graph[u]:
                    queue.append((v, path[:] + [v]))

        def find(line, x, y):
            x_index = line.index(x)
            y_index = line.index(y)

            if x_index < y_index:
                return line[x_index:y_index]
            else:
                return line[x_index:y_index:-1]

        ans = []
        minlength=min(len(x) for x in res)
        res=[x for x in res if len(x)==minlength]

        for path in res:

            m = len(path)
            aans = [[start]]
            for i in range(m):
                endpoints = graph[path[i]][path[i + 1]] if i < m - 1 else [end]


                aans=[x+[y] for x in aans  for y in endpoints]

            for subpath in aans:
                tmp=[]
                b=start
                for i in range(m):
                    tmp+=find(lines[path[i]],b,subpath[i+1])
                    b=subpath[i+1]

                ans.append(tmp+[end])


        ans.sort()
        return ans[0]

lines = [[1,2,3,4,5],[2,10,14,15,16],[10,8,12,13],[7,8,4,9,11]]
start = 1
end = 7
lines=[[1,2,3],[2,4,5,6],[1,9],[9,5],[7,8]]
start=1
end=6
lines=[[7535,1306,8941,1356,6017,6331,6181,4941],[8941,1356,6181,6017,7535,4941,6331,1306],[1356,1306,6331,6017,6181,7535,4941,8941],[7535,8941,6017,1356,1306,6331,6181,4941],[4941,6331,6181,1356,6017]]
start=6181
end=6331
lines=[[5434,5040,1230,1506,9991,1174,3423,3976],[9991,1230,5434],[7853,3423,9991,5434,3976],[5434,1506,9991,1174]]
start=1506
end=7853
lines=[[4165,8075,3072,6302,3747,3616,1893],[7431,3616,3747,1893,8075,3219],[3072,6302,3747],[3616,3969],[7431,3616]]
start=4165
end=3219
res=Solution().metroRouteDesignI(lines,start,end)
print(res)