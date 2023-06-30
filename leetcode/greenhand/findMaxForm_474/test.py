a=[1,2,3,4]
b=[1,1,1,1]
for i in range(10):

    for j in range(50):
        a[0]=j
        print(b, i, j)

    b=a.copy()
    print('after',b,i,j)