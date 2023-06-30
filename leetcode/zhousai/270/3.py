
class Solution:
    def getDirections(self, root, startValue: int, destValue: int) -> str:



        t_p=[]
        def find(root,path,target,tp):
            if root.val==target:
                return path,t_p

            find(root.left,path+[root.val],t_p+['L'])
            find(root.right,path+[root.val],t_p+['R'])


        spath,_=find(startValue,t_p)
        tpath,tp=find(destValue,t_p)

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
