import heapq

arr = [6, 5, 3, 2, 8, 10, 9]
heap = []
res = []
k = 3
j = 0

# heapq.heapify(arr)
for i in range(len(arr)):
    heapq.heappush(heap, arr[i])
    if len(heap) > k:
        arr[j] = heapq.heappop(heap)
        j += 1
while len(heap):
    arr[j] = heapq.heappop(heap)
    j += 1

print(arr)
