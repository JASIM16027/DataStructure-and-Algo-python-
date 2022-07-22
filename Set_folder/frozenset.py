# Freeze the list, and make it unchangeable:
ll = ['apple', 'banana', 'cherry']
x = frozenset(ll)
print(x)  # output : frozenset({'banana', 'apple', 'cherry'})
l = ll.append('orange')
print(x)  # output : frozenset({'banana', 'apple', 'cherry'})

# The frozenset() function returns an unchangeable frozenset object
# (which is like a set object, only unchangeable).
# frozenset(iterable) An iterable object, like list, set, tuple etc.
# x[1] = "strawberry"
# print(x)  # TypeError: 'frozenset' object does not support item assignment

# Syntax : frozenset(iterable_object_name)
# Parameter : This function accepts iterable object as input parameter.
# Return Type: This function return an equivalent frozenset object.
u = (1, 2, 3, 4, 5, 6, 7, 8, 9)
tl = frozenset(u)
print(tl)

# creating a dictionary
Student = {"name": "JASIM ", "age": 25, "sex": "Male",
           "university": "MBSTU", "address": "khulna"}

# making keys of dictionary as frozenset
key = frozenset(Student)

# printing keys details
print('The frozen set is:', key)

# Example #3: Warning
# If by mistake we want to change the frozenset object then it throws an error
# “‘frozenset’ object does not support item assignment“.
# creating a list
favourite_subject = ["OS", "DBMS", "Algo"]

# making it frozenset type
f_subject = frozenset(favourite_subject)

# below line will generate error

# f_subject[1] = "Networking"  # TypeError: 'frozenset' object does not support item assignment
