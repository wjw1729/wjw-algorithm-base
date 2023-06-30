import time
import sys


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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

from collections import deque

@bootstrap
def inorderTraversal(root: TreeNode):
    if not root:
        yield deque()


    a=deque([root.val])
    a.extendleft((yield inorderTraversal(root.left)))
    a.extend((yield inorderTraversal(root.right)))

    yield a




root = TreeNode(10 ** 5)
node = root
for i in range(10 ** 5 - 1, -1, -1):
    node.left = TreeNode(i)
    node = node.left

t1 = time.time()

res = inorderTraversal(root)

print(time.time() - t1)
