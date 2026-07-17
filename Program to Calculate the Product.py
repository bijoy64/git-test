def multiply (numbers):
    total = 1
    for x in numbers:
        total *= x
    return total
result = multiply((4,3,6,10,7))
print("the multiplication of the numbers is:", result)