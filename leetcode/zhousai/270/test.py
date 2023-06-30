start = time.time()
s = None
t = None
path = []
spath = []
tpath = []
t_p = []
tp = []


def find(node, path, t_p):
    nonlocal s, t
    if (s != None and t != None) or not node:
        return
    if node.val == startValue:
        spath[:] = path[:]
        s = node
    if node.val == destValue:
        tpath[:] = path[:]
        tp[:] = t_p
        t = node

    find(node.left, path + [node.val], t_p + ['L'])
    find(node.right, path + [node.val], t_p + ['R'])

    return


find(root, path, t_p)
print(time.time() - start)
# print(spath)
# print(tpath)
# print(tp)
spath += [startValue]
tpath += [destValue]
m = len(spath)
n = len(tpath)
# print(tpath,tp)
i = 0
while i < min(m, n):
    if spath[i] != tpath[i]: break
    i += 1
# print(i,n,m)
if i == m:
    ans = tp[i - 1:]
elif i == n:
    ans = ['U'] * (m - i)
else:
    ans = ['U'] * (m - i) + tp[i - 1:]
    # print(['U']*(m-i))
return ''.join(ans)