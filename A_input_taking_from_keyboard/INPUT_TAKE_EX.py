t = int(input().strip())
# Remove spaces at the beginning and at the end of the string:
# The strip() method removes any leading (spaces at the beginning) and trailing
# (spaces at the end) characters (space is the default leading character to remove)
# string.strip(characters)
str = "....'''',,,rrr...banana.......''''''"
res = str.strip(".,'r")
print(res)
# Remove any white spaces at the end of the string:
str1 = "....'''',,,rrr...banana.......''''''"
res1 = str1.rstrip("'.")
print(res1)
str2 = "....'''',,,rrr...banana.......''''''"
res2 = str2.lstrip("'.,r")
print(res2)