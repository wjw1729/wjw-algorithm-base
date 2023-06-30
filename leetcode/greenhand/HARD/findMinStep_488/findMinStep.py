"""
author:wjw
祖玛游戏
"""

from collections import deque
import re
class Solution:
    def findMinStep(self,board,hand):

        def clean(s):
            n = 1
            while n:
                s, n = re.subn(r"(.)\1{2,}", "", s)
            return s


        hand=''.join(sorted(hand))
        queue=deque()
        queue.append((board,hand,0,))

        visited={(board,hand)}


        while queue:
            board,hand,step=queue.popleft()

            for i in range(len(board)+1):
                for j in range(len(hand)):
                    if j>0 and hand[j]==hand[j-1]:
                        continue

                    if i>0 and hand[j]==board[i-1]:
                        continue

                    choose=False

                    if i<len(board) and hand[j]==board[i]:
                        choose=True
                    if 0<i<len(board) and hand[j]!=board[i-1] and board[i-1]==board[i]:
                        choose=True

                    if choose:
                        new_board=clean(board[:i]+hand[j]+board[i:])
                        new_hand=hand[:j]+hand[j+1:]

                        if not new_board:
                            return step+1

                        if (new_board,new_hand) not in visited:
                            queue.append((new_board,new_hand,step+1))
                            visited.add((new_board,new_hand))

        return -1


board = "WRRBBW"
hand = "RB"
board = "WWRRBBWW"
hand = "WRBRW"
res=Solution().findMinStep(board,hand)
print(res)