#!/usr/bin/python
print 5 >> 4  # Right Shift
print 5 << 1  # Left Shift
print 8 & 5   # Bitwise AND
print 9 | 4   # Bitwise OR
print 12 ^ 42 # Bitwise XOR
print ~88     # Bitwise NOT

#writing bitwise number
one = 0b1
two = 0b10
three = 0b11
four = 0b100
five = 0b101
six = 0b110
seven = 0b111
eight = 0b1000
nine = 0b1001
ten = 0b1010
eleven = 0b1011
twelve = 0b1100

#shifting bits
shift_right = 0b1100
shift_left = 0b1

# Your code here!
shift_right = shift_right >> 2
shift_left = shift_left << 2

print bin(shift_right)
print bin(shift_left)

# xor statement
print bin(0b1110 ^ 0b101)

#checks if bit 4 is on
def check_bit4(input):
    checker = 0b1000
    desired = checker & input
    if desired > 0:
        return "on"
    return "off"

#flips the bit of a
a = 0b11101110
mask = 0b11111111
desired = a ^ mask
print bin(desired)

#flips nth bit
def flip_bit(number,n):
    mask = 0b1 << (n-1)
    result = number ^ mask
    return bin(result)
