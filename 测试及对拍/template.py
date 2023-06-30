"""
用于随机生成的测试案例的调试

"""

import cyaron
import os



def sumofnums(nums):
    return sum(nums)



def getout(input_file,output_file):


    fout=open(output_file,'w')
    with open(input_file,'r') as f:
        s=f.readlines()
        for each_s in s:
            nums=[int(x) for x in each_s.split()]
            fout.write(str(sumofnums(nums))+'\n')
    f.close()
    fout.close()




getout('test.in','test1.out')
getout('test.in','test2.out')











