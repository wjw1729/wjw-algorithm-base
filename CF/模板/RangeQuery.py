

"""
区间最值查询数据结构
时间复杂度:O(nlogn)
func:决定查询最小值或者最大值
func_eq:区间最小值（最大值）的最小（最大值）下标，当数组存在相等值的时候才会有区别。
"""


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
        return self.array[self.index(l,r)]

