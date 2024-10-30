from copy import copy, deepcopy

# print("My first code")

# strings:
a = 'LearnPython1'
print(a)

print(id(a))


b = a
print("b=" + b)
print(id(b))

c = deepcopy(a)
print(id(c))


a = 20
print(a, c, b)

print(id(a), id(b), id(c))

# a = "changed copy"
#
# print(a, b, c)