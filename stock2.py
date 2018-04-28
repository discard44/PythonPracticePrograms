#!/usr/bin/python
shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
    
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Write your code below!
def compute_bill(food):
    total = 0
    for each in food:
        if stock[each] > 0:
            total = total + prices[each]
            stock[each] = stock[each] - 1
        
    return total
