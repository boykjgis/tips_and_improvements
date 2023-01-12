# Unpacking

# Code to refactor
a, b = (1, 2)

print(a)
print(b)

# Refactored code
a, _ = (1, 2)

print(a)
#print(b)

# a, b = (1, 2, 3, 4)
# Will result in a value error -> Too many values to unpack (ValueError)

# a, b, c = (1, 2)
# Will result in not enough values to unpack (ValueError)

a, b, *c = (1, 2, 3, 4, 5)
print(a, b, c)

a, b, *_ = (1, 2, 3, 4, 5)
print(a, b)
print(_)