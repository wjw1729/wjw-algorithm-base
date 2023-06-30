class Solution:
    def ringGame(self, challenge) -> int:
        l = min(challenge)
        r = max(challenge)

        n = len(challenge)

        def canPass(x):

            maxOsum = x
            for i, num in enumerate(challenge):
                if num <= x and num | x >= maxOsum:
                    idx = i
                    maxOsum = num | x

            l = idx - 1
            r = (idx + 1) % n

            grades = maxOsum

            while l != r:
                if grades >= challenge[l]:
                    grades = max(grades, grades | challenge[l])
                    l = (l - 1 + n) % n

                if l == r:
                    return grades>=challenge[l]

                if grades >= challenge[r]:
                    grades = max(grades, grades | challenge[r])
                    r = (r + 1) % n
                if grades < challenge[l] and grades < challenge[r]:
                    break

            return l == r and grades>=challenge[l]

        while l <= r:
            mid = (l + r + 1) // 2
            if canPass(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        return ans


challenge = [5, 4, 6, 2, 7]
challenge = [12, 7, 11, 3, 9]
challenge = [1, 1, 1]
challenge=[1,15,3]
res = Solution().ringGame(challenge)
print(res)
