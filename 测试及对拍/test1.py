
def bag_01(costs,values,v):

    f=[0]*(v+1)
    n=len(costs)

    for i in range(n):
        for j in range(v,costs[i]-1,-1):
            f[j]=max(f[j],f[j-costs[i]]+values[i])

    return (max(f),f[-1])


def bag(costs,values,v):
    n=len(costs)
    f=[[0]*(v+1) for _ in range(n)]

    for i in range(n):
        for j in range(costs[i],v+1):

            f[i][j]=max(f[i-1][j],f[i-1][j-costs[i]]+values[i])

    return max(f[-1]),f[-1][-1]



def bag_02(costs,values,v):
    f=[0]*(v+1)
    n=len(costs)

    for i in range(n):
        for j in range(costs[i],v+1):
            f[j]=max(f[j],f[j-costs[i]]+values[j])

    return max(f),f[-1]


costs=[2,4]
values=[4,7]
v=5
print(bag(costs,values,v))


