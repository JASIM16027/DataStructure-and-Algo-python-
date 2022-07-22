import heapq
arr = [7, 10, 4, 3, 20, 15]
heap = []
k = 3

for i in range(len(arr)):
    heapq.heappush(heap,-arr[i])
    if len(heap) > k:
        heapq.heappop(heap)

print(-heapq.heappop(heap))