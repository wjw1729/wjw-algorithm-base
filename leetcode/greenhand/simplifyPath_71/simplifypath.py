"""
author:wjw
分析：比较明显，用栈实现。
"""

class Solution:
    def simplifyPath(self,path):

        stack=[]
        hierarchy=path.split('/')
        hierarchy=[x for x in hierarchy if x!='']
        for dir in hierarchy:
            if dir=='..':
                if stack:
                    stack.pop()
                continue
            if dir=='.':
                continue
            stack.append(dir)

        return '/'+'/'.join(stack)

path = "/home/"
path = "/../"
path = "/home//foo/"
path = "/a/./b/../../c/"
res=Solution().simplifyPath(path)
print(res)