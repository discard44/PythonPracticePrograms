#!/usr/bin/python
my_list = range(1, 11) # List of numbers 1 - 10

# Add your code b
print my_list[::2]

#reverses a list
my_list = range(1, 11)

# Add your code below!
backwards = my_list[::-1]
print backwards

#travers a list backwards by ten
to_one_hundred = range(101)
# Add your code below!
backwards_by_tens = to_one_hundred[::-10]
print backwards_by_tens

#print odds of a list and middle third
to_21 = range(1,22)

odds = to_21[:21:2]

middle_third = to_21[7:14:]
