import heapq

heap=[]
heapq.heappush(heap,4)
heapq.heappush(heap,3)
heapq.heappush(heap,1)
heapq.heappop(heap)
print(heap[0])