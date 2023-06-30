"""
author:wjw
分析：写一个判断能否到达指定点（x,y）的函数，如果能在到达目标点之前碰到obstacle，则损坏
"""


def judge(command, x, y):
    list = [[0, 0]]
    point = [0, 0]
    for i in range(len(command)):
        if command[i] == 'U':
            point = [point[0], point[1] + 1]
        if command[i] == 'R':
            point = [point[0] + 1, point[1]]
        list.append(point)

    deltax = list[-1][0]
    deltay = list[-1][1]

    k = min(x // deltax, y // deltay)  # 记录循环轮次
    x = x - k * deltax
    y = y - k * deltay

    if [x, y] in list:
        return True
    else:
        return False


class Solution:
    def robot(self, command, obstacle, x, y):
        if judge(command, x, y):
            for i in range(len(obstacle)):
                if obstacle[i][0] <= x and obstacle[i][1] <= y:
                    if judge(command, obstacle[i][0], obstacle[i][1]):
                        return False
            return True
        else:
            return False


command = "URRURRR"
obstacles = [[7, 7], [0, 5], [2, 7], [8, 6], [8, 7], [6, 5], [4, 4], [0, 3], [3, 6]]
x = 4915
y = 1966

result = Solution().robot(command, obstacles, x, y)
print(result)
