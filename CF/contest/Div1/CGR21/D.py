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


class RangeQueryIdx:
    def __init__(self,array,func,func_eq):
        limit=len(array)
        self.array=array
        self.func=func
        self.func_eq=func_eq
        self.row=limit.bit_length()
        self.tab=[[0 for _ in range(limit)] for _ in range(self.row)]

        self.tab[0]=list(range(limit))

        for i in range(1,self.row):
            for j in range(limit-2**i+1):
                self.tab[i][j]=self._apply_func(self.tab[i-1][j],self.tab[i-1][j+2**(i-1)])


    def _apply_func(self,l,r):
        val_l=self.array[l]
        val_r=self.array[r]
        if val_l==val_r:
            return self.func_eq(l,r)

        return l  if self.func(val_l,val_r)== val_l else r


    def index(self,l,r):
        i=0 if r-l==0 else (r-l+1).bit_length()-1
        return self._apply_func(self.tab[i][l],self.tab[i][r-2**i+1])

    def query(self,l,r):
        return self.index(l,r)



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




t=int(input())
for _ in range(t):
    n=int(input())
    a=[int(x) for x  in input().split()]
    if n==1:
        print(0)
    else:

        rqi_min=RangeQueryIdx(a,min,min)
        rqi_max=RangeQueryIdx(a,max,min)
        print(dfs(0,n-1))








