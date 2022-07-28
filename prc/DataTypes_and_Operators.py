# We can take out character from a String by simply considering it an array of characters
s = "Hello"
print(s[2])
print("He_Is_Shy"[7])

# In python the _ between the numbers is considered same as the commas in our traditional maths like 52,956,85
n = 52_956_85
print(n)

# In python we have 'True' and 'False' as boolean data types
# Where if we covert integer to boolean then 0 is 'False' and rest all numbers are 'True'
print(bool(2))
print(bool(0))

# In python we can't add any other data type in String.
# We first need to convert it to String then it can be added.
print("Hello " + str(6) + " haha")


# When we divide two integers in Python, the output comes in float.
print(8 / 2)

# ** is the exponent operator in python.
print(2 ** 4)

""" Precidence of Operators in Python is: -

PEDMAS

()
**
* /
+ -

"""

print(3 * (3 - 3) / 3 + 3)

# Floor Division is done using // i.e. (8 // 3) and it gives the value same as int(8 / 3)
print(8 // 3)
print(int(8 / 3))

# To round of number properly, we use 'round' function, and we can also round to some particular decimal place.
print(round(8 / 3))
print(round((4 / 3), 2))

# F Strings are used to make work easy
# We can put values without changing their type by simply putting a 'f' just before string and put our variables in {}.
# Example is given below
age = 20
weight = 45
name = "Sanidhya"
print(f"My name is {name}.\nI am {age}.\nMy weight is {weight}kg")
