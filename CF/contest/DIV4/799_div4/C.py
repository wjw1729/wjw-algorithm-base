
def chcek(i,j):
    return  all(mat[x][y]=='#' for x,y in [(i-1,j-1),(i-1,j+1),(i+1,j-1),(i+1,j+1)])

t=int(input())
for _ in range(t):
    input()
    mat = []
    for _ in range(8):
        mat.append(input())

    for i in range(1,7):
        for j in range(1,7):
            if chcek(i,j):
                print(i+1,j+1)
                break


