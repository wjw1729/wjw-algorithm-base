class Solution:
    def pathsWithMaxScore(self, board) :

        m = len(board)
        n = len(board[0])
        dp = [[-float('inf')] * n for _ in range(m)]
        plans = [[0] * n for _ in range(m)]
        plans[m - 1][n - 1] = 1
        dp[m - 1][n - 1] = 0

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    continue
                if board[i][j] == 'X':
                    continue
                tmpd, tmpr, tmp = None, None, None
                if i != m - 1:
                    if board[i + 1][j] == 'S':
                        tmpd = dp[i + 1][j]
                        dp[i][j] = max(dp[i][j], dp[i + 1][j])
                    else:
                        tmpd = dp[i + 1][j] + int(board[i + 1][j]) if board[i + 1][j] != 'X' else -float('inf')
                        dp[i][j] = max(dp[i][j],
                                       dp[i + 1][j] + int(board[i + 1][j]) if board[i + 1][j] != 'X' else -float('inf'))

                if j != n - 1:
                    if board[i][j + 1] == 'S':
                        tmpr = dp[i][j + 1]
                        dp[i][j] = max(dp[i][j], dp[i][j + 1])
                    else:
                        tmpr = dp[i][j + 1] + int(board[i][j + 1]) if board[i][j + 1] != 'X' else -float('inf')
                        dp[i][j] = max(dp[i][j],
                                       dp[i][j + 1] + int(board[i][j + 1]) if board[i][j + 1] != 'X' else -float('inf'))

                if i != m - 1 and j != n - 1:
                    if board[i + 1][j + 1] == 'S':
                        tmp = dp[i + 1][j + 1]
                        dp[i][j] = max(dp[i][j], dp[i + 1][j + 1])
                    else:
                        tmp = dp[i + 1][j + 1] + int(board[i + 1][j + 1]) if board[i + 1][j + 1] not in ['X',
                                                                                                         'S'] else -float(
                            'inf')
                        dp[i][j] = max(dp[i][j],
                                       dp[i + 1][j + 1] + int(board[i + 1][j + 1]) if board[i + 1][j + 1] not in ['X',
                                                                                                                  'S'] else -float(
                                           'inf'))

                if tmpd!=None and tmpd == dp[i][j]:
                    plans[i][j] += plans[i + 1][j]
                if tmpr!=None and tmpr == dp[i][j]:
                    plans[i][j] += plans[i][j + 1]
                if tmp!=None and tmp == dp[i][j]:
                    plans[i][j] += plans[i + 1][j + 1]

        return (dp[0][0], plans[0][0])

board = ["E23","2X2","12S"]
res=Solution().pathsWithMaxScore(board)
print(res)