#! /usr/bin/python
def fizz_count(x):
    count = 0
    for y in x:
        if y == "fizz":
            count = count + 1
    return count
    
print fizz_count(["fizz", "cat", "fizz"])
