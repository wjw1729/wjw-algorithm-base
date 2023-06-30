from collections import deque, defaultdict


class LockingTree:

    def __init__(self, parent):
        n = len(parent)
        self.child = defaultdict(list)
        self.parent = defaultdict(int)
        self.locks = [0] * n  # 0 表示未上锁

        for u, v in enumerate(parent):
            self.parent[u] = v
            self.child[v].append(u)

    def lock(self, num: int, user: int) -> bool:
        if self.locks[num] == 0:
            self.locks[num] = user
            return True
        else:
            return False

    def unlock(self, num: int, user: int) -> bool:
        if self.locks[num] == user:
            self.locks[num] = 0
            return True
        else:
            return False

    def judge(self, node):
        if node == -1:
            return True
        if self.locks[node] != 0:
            return False
        return self.judge(self.parent[node])

    def upgrade(self, num: int, user: int) -> bool:

        if self.judge(num):

            queue = deque()
            queue.append(num)
            ans = []

            while queue:
                node = queue.popleft()

                for nxt in self.child[node]:
                    queue.append(nxt)
                    if self.locks[nxt] != 0:
                        ans.append(nxt)
            if not ans:
                return False
            else:
                for i in ans:
                    self.locks[i] = 0
                self.locks[num] = user
                return True

        else:

            return False


obj = LockingTree([-1, 5, 3, 0, 7, 4, 7, 0, 0, 1])
print(obj.unlock(8, 23))
print(obj.unlock(2, 30))
print(obj.upgrade(1, 25))
print(obj.upgrade(0, 43))
print(obj.upgrade(1, 9))
print(obj.lock(9, 1))
print(obj.unlock(3, 24))
print(obj.upgrade(2, 45))
print(obj.upgrade(5, 13))
print(obj.upgrade(4, 7))
print(obj.upgrade(3, 33))
print(obj.upgrade(9, 18))
print(obj.unlock(9, 1))
print(obj.unlock(3, 43))
print(obj.upgrade(6, 16))
print(obj.upgrade(3, 5))
print(obj.lock(8, 10))
print(obj.upgrade(7, 9))
print(obj.upgrade(4, 49))
print(obj.upgrade(9, 25))

["LockingTree", "unlock", "unlock", "upgrade", "upgrade", "upgrade", "lock", "unlock", "upgrade", "upgrade", "upgrade",
 "upgrade", "upgrade", "unlock", "unlock", "upgrade", "upgrade", "lock", "upgrade", "upgrade", "upgrade"]
[[], [8, 23], [2, 30], [1, 25], [0, 43], [1, 9], [9, 1], [3, 24], [2, 45], [5, 13], [4, 7], [3, 33], [9, 18], [9, 1],
 [3, 43], [6, 16], [3, 5], [8, 10], [7, 9], [4, 49], [9, 25]]
