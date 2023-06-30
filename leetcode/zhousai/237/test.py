"""
卷积：
"""

w = 100
h = 100

pic = [[[0] * w for _ in range(h)] for _ in range(3)]

k = 1
filter = [[0] * (2 * k + 1) for _ in range(2 * k + 1)]


def convolution(pic, filter):
    newpic = [[[0] * (w + 2 * k) for _ in range(h + 2 * k)] for _ in range(3)]

    for c in range(3):
        for i in range(k, h + k + 1):
            for j in range(k, w + k + 1):
                newpic[c][i][j] = pic[c][i - k][j - k]

    res = [[[0] * w for _ in range(h)] for _ in range(3)]
    for c in range(3):
        for i in range(k, h + k + 1):
            for j in range(k, w + k + 1):
                tmp = 0
                for p in range(2 * k + 1):
                    for q in range(2 * k + 1):
                        tmp += filter[p][q] * newpic[c][i - k + p][j - k + q]
                res[c][i][j] = tmp
    return res
