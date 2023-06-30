def similarity(l1, l2):
    s1 = ''.join([str(x) for x in l1])
    s2 = ''.join([str(x) for x in l2])
    n = len(l1)
    res = bin(int(s1, base=2) ^ int(s2, base=2)).count('1')
    return n - res


class Solution:
    def maxCompatibilitySum(self, students, mentors) -> int:
        self.ans = 0

        def backtrack(students, mentors, total):
            if students == []:
                self.ans = max(self.ans, total)
                print(total)
                return

            n = len(students)
            stu_ls = students.pop(0)

            for i in range(n):
                tmp = mentors.pop(i)
                sim = similarity(stu_ls, tmp)

                total += sim

                backtrack(students, mentors, total)

                mentors.insert(i, tmp)
                total -= sim
            students.insert(0,stu_ls)

        backtrack(students, mentors, 0)
        return self.ans



students = [[1, 1, 0], [1, 0, 1]]
mentors = [[1, 0, 0], [0, 0, 1]]
students = [[1,1,0],[1,0,1],[0,0,1]]
mentors = [[1,0,0],[0,0,1],[1,1,0]]
res = Solution().maxCompatibilitySum(students, mentors)
print(res)
