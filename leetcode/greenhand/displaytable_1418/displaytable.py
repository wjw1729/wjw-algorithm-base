"""
author:wjw
分析：
"""


class Solution:
    def displayTable(self, orders) :
        n = len(orders)
        header = set()
        Table = {}
        for i in range(n):
            header.add(orders[i][2])
            Table.setdefault(orders[i][1], {})
            Table[orders[i][1]].setdefault(orders[i][2], 0)
            Table[orders[i][1]][orders[i][2]] += 1

        header = ['Table'] + sorted(list(header))
        res = [header[:] for i in range(len(Table)+1)]

        for i, d in enumerate(sorted(Table.items(), key=lambda x: int(x[0]))):
            k, v = d
            res[i + 1][0] = k
            for j in range(1, len(header)):
                if header[j] in v:
                    res[i + 1][j] = v[header[j]]
                else:
                    res[i + 1][j] = '0'

        return res

orders=orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]

res=Solution().displayTable(orders)
print(res)