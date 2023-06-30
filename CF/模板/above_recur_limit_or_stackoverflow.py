from types import GeneratorType


def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to

    return wrappedfunc

"""
将return 改为yield
以及调用dfs()时改为，(yield dfs())
"""


@bootstrap
def dfs(l,r):

    if (rqi_min.query(l,r)==l and rqi_max.query(l,r)==r) or (rqi_min.query(l,r)==r and rqi_max.query(l,r)==l):
        yield 1

    elif rqi_min.query(l,r)==l:

        j=rqi_max.query(l,r)

        res=1+(yield dfs(j,r))


    elif rqi_max.query(l,r)==l:
        j=rqi_min.query(l,r)
        res=1+(yield dfs(j,r))

    elif rqi_min.query(l,r)==r:
        j=rqi_max.query(l,r)
        res=1+(yield dfs(l,j))

    elif rqi_max.query(l,r)==r:
        j=rqi_min.query(l,r)

        res=1+(yield dfs(l,j))
    else:
        i=rqi_min.query(l,r)
        j=rqi_max.query(l,r)

        if i>j:
            i,j=j,i
        res=1+(yield dfs(l,i))+(yield  dfs(j,r))

    yield res
