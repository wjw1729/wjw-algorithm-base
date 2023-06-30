from collections import  deque,defaultdict
class Solution:
    def getMaxLayerSum(self, root) -> int:

        lsum=defaultdict(int)
        queue = deque()
        queue.append((root,0))

        nodelevel=defaultdict(int)
        nodesubsum=defaultdict(int)

        valid=set()

        while queue:
            node,l=queue.popleft()
            lsum[l]+=node.val
            nodelevel[node]=l
            tmp=0

            cnt=0

            if node.left:
                queue.append((node.left,l+1))
                tmp+=node.left.val
                cnt+=1

            if node.right:
                queue.append((node.right,l+1))
                tmp+=node.right.val
                cnt+=1

            if cnt<=1:
                valid.add(node)

            nodesubsum[node]=tmp

        ans=max(lsum.values())


        for node in valid:

            l = nodelevel[node]
            queue = deque()
            queue.append(node)

            i = 0
            while queue:
                nxtq = deque()
                ans = max(ans, lsum[l + i] - sum([x.val for x in queue]) + sum([nodesubsum[x] for x in queue]))
                while queue:
                    node = queue.popleft()
                    if node.left:
                        nxtq.append(node.left)
                    if node.right:
                        nxtq.append(node.right)
                queue = nxtq
                i += 1

        return ans





















