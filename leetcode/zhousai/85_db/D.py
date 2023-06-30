# 逆序+成堆分
# 可参考1562


def maxleft(weight, pick_list):
    n = len(weight)
    endpoints = [(-1, -1)] * n
    gather = [0] * n

    maxnum = 0
    ans = []

    for p in pick_list[::-1]:

        ans.append(maxnum)

        idx = p - 1

        l = r = idx

        gather[idx] = weight[idx]
        if idx > 0 and gather[idx - 1] > 0:
            l = endpoints[idx - 1][0]
            gather[idx] += gather[l]
        if idx < n - 1 and gather[idx + 1] > 0:
            r = endpoints[idx + 1][1]
            gather[idx] += gather[r]

        endpoints[l] = endpoints[r] = (l, r)
        gather[l] = gather[r] = gather[idx]

        maxnum = max(maxnum, gather[idx])

    return ans[::-1]
nums = [1,2,5,6,1]
removeQueries = [0,3,2,4,1]
res=maxleft(nums,removeQueries)
print(res)










