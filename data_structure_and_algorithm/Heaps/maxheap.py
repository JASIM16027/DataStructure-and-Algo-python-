import heapq

arr = [6, 5, 3, 2, 8, 10, 7]
k = 3
res = []
heap = []

for i in range(len(arr)):
    heapq.heappush(heap, arr[i])
    if len(heap) > k:
        heapq.heappop(heap)

while len(heap)>0:
    res.append(heapq.heappop(heap))

print(res[::-1])