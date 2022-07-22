
# A Set in Python is a collection of unique elements which are unordered and mutable.
s = {1, 2, 3, 4, 5, 6, 7}
print('Before adding 10 : ', s)
# The set add() method adds a given element to a set if the element is not present in the set.
s.add(10)
print('After adding 10 : ', s)
s.remove(7)
print('After removing 7 : ', s)
# discard(): Removes the element from the set
s.discard(9)
print(s)
s.pop()
s.pop()
#  pop(): Returns and removes a random element from the set
print(s)
s1 = s.copy()
print(s1)
s.clear()
print(s1)