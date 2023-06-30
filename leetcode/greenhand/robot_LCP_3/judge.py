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


command = "URRURRR"
x = 4915
y = 1966
result = judge(command, x, y)
print(result)
