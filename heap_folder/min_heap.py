# Example Python program that removes smallest element(s) from a

# min heap using heappop() function

import heapq

# Construct a heap

heapElements = ["a", "d", "b", "g", "e", "c", "f"]

print("Original list: %s" % heapElements)

heapq.heapify(heapElements)

print("Result of calling heapq.heapify():%s" % heapElements)

print(heapElements)

# Remove the smallest element from the heap

smallest = heapq.heappop(heapElements)

print("Smallest element:%s" % smallest)

print("Updated heap:%s" % heapElements)

# Remove the current smallest element

smallest = heapq.heappop(heapElements)

print("Currently the smallest element is:%s" % smallest)

print("Updated heap:%s" % heapElements)

# The functions of the heapq module enable construction and manipulation of min heaps.

# The heap is constructed as a binary tree. In a min heap the smallest element is at the root.
# The child nodes store values greater than the parent nodes.

# The heappop() function removes and returns the smallest element from the heap.

# As heappop() is called it removes and returns the root node of a min heap and
# invalidates the heap to maintain the heap invariant.
#
