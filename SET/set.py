# SET
# A set is a collection of unique elements
#  it is used to store multiple values in a single variable

# Unorderd: donot have any fixed position
# mutable: we can ad or remove elements
# no duplicate allows
# can store different data types

# number = {10,20,30,20}
# print(number)
# number.remove(10)
# print(number)

# number1 = {10,20,30,20,40, 50}
# number1.discard(30)
# print(number1)

# number = {10,20,30,20}
# number1 = {10,20,40, 50}
# print(number.union(number1))
# print(number.intersection(number1))
# print(number.issubset(number1))

# # difference is find the first not matching number/
# print(number.difference(number1))
# print(number.symmetric_difference(number1))

a = {10,20,30}
b = {40,50,20}
print(a.intersection(b))
print(a.symmetric_difference(b))
print(a.difference(b))
print(a.update(b))