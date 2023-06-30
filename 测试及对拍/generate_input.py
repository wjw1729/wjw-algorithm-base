"""
生成输入数据
"""


import cyaron
from cyaron import Vector



def gen_test_in(n):
    f=open('test.in','w')

    for _ in range(n):
        output=[x[0] for x in Vector.random(10,(10,50),1)]

        f.write(' '.join(str(x) for x in output)+'\n')



gen_test_in(10)




