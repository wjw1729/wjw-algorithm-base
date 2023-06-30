t = int(input())

for _ in range(t):
    m = int(input())
    mat = []
    mat.append(input())
    mat.append(input())


    def get(mat):
        if mat[0][0] == mat[1][0] == 'B':
            status = 3
        elif mat[0][0] == 'B':
            status = 1
        elif mat[1][0] == 'B':
            status = 2

        for i in range(1, m):
            if mat[0][i] == 'B' and mat[1][i] == 'B':
                if status == 1:
                    status = 2
                elif status == 2:
                    status = 1

            elif mat[0][i] == 'B':
                if status == 3:
                    status = 1
                elif status != 1:
                    return False
            elif mat[1][i] == 'B':
                if status == 3:
                    status = 2
                elif status != 2:
                    return False

        return True


    if get(mat):
        print('YES')
    else:
        print('NO')
