def summation():
    sum = 0
    for i in range(101):
        if i % 2 == 0:
            continue
        sum = sum + i
    return sum
add = summation()
print("the summatin is:",add)
