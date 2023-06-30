# Python2

[Python Performance++](http://codeforces.com/blog/entry/63102)

By [c1729](http://codeforces.com/profile/c1729), [history](http://codeforces.com/topic/63482/en5), 3 years ago, ![In English](http://codeforces.org/s/45670/images/flags/24/gb.png)

I've listed my findings on experimenting with Python below, I hope they are useful to someone else who uses Python too.

**TL;DR:** Links for the [master template](https://github.com/cheran-senthil/PyRival/blob/master/template/template.py) and [algorithms](https://github.com/cheran-senthil/PyRival).

#### **Python Version**

Based on [prior benchmarking](https://codeforces.com/blog/entry/21851) on Codeforces, it is quite conclusive that PyPy 2 is the fastest version of Python available on Codeforces.

PyPy 2 also has features not present in PyPy 3 such as random, and numpypy. Moreover, in Python 2, bytes and strings are equivalent, this is not the case in Python 3 and results in significant input and output slowdowns unless you use Bytes in Python 3.

#### **Input & Output**

Though there are faster ways to read input for specific types (integers and non-strings). The safest way to redefine input/print while maintaining the same functionality is to use the following code,

```python
import os
import sys
from atexit import register
from io import BytesIO

sys.stdin = BytesIO(os.read(0, os.fstat(0).st_size))
sys.stdout = BytesIO()
register(lambda: os.write(1, sys.stdout.getvalue()))

input = lambda: sys.stdin.readline().rstrip('\r\n')
```

if your input does not involve strings, you can directly use,

```python
import os
import sys
from atexit import register
from io import BytesIO

sys.stdout = BytesIO()
register(lambda: os.write(1, sys.stdout.getvalue()))

input = BytesIO(os.read(0, os.fstat(0).st_size)).readline
```

This should be enough for the majority of cases, except in some rare cases where you have lots of integers as input and would require custom str -> int.

You can also do much faster output in PyPy 2 by following [pajenegod](http://codeforces.com/profile/pajenegod)'s instructions [here](https://codeforces.com/blog/entry/65922?#comment-499139).

#### **Python 3 Compatability**

print and division work differently between Python 2 and 3, but this can be remedied with imports from `__future__`

Other differences are that range, filter, map, and zip all return iterators in Python 3 as opposed to lists in Python 2 and thus use less memory and are slightly faster when you don't need the data more than once.

A minor issue in Python 2 is that the builtin gcd is much slower than writing your own iterative gcd, ideally having code for this is useful too.

The code below should handle all of these issues, and let you write Python 3 code within Python 2.

```python
""" Python 3 compatibility tools. """
from __future__ import division, print_function

import itertools
import sys

if sys.version_info[0] < 3:
    input = raw_input
    range = xrange

    filter = itertools.ifilter
    map = itertools.imap
    zip = itertools.izip


def gcd(x, y):
    """ greatest common divisor of x and y """
    while y:
        x, y = y, x % y
    return x
```

#### **Recursion Limit**

In Python, we can use threading to increase the stack size to allow for large recursion limits, in PyPy this is not possible.

However, [PyPy's docs](https://pypy.readthedocs.io/en/latest/stackless.html#recursion-depth-limit) give detail on how to resolve this issue. I've added some code below that should work for both. However, overall, this is much slower than using your own stack in Python.

```python
import sys

if 'PyPy' in sys.version:
    from _continuation import continulet
else:
    import threading


def main():
    pass


if __name__ == '__main__':
    if 'PyPy' in sys.version:

        def bootstrap(cont):
            call, arg = cont.switch()
            while True:
                call, arg = cont.switch(to=continulet(lambda _, f, args: f(*args), call, arg))

        cont = continulet(bootstrap)
        cont.switch()

        main()

    else:
        sys.setrecursionlimit(1 << 30)
        threading.stack_size(1 << 27)

        main_thread = threading.Thread(target=main)
        main_thread.start()
        main_thread.join()
```

# Python3

CF提交建议：

1. 使用pypy3.7提交
2. 使用快读和快写，进行优化（详见模板）



防止因为hash冲突导致hashtable中插入复杂度变为O(n**2)的方法。

1. 对哈希表中键值（整数）统一进行处理，加上一个随机数，返回结果时记得返回即可。
2. 将整数转换为字符串作为键值。
