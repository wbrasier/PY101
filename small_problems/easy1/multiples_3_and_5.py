def multisum(num):
    result = 0
    for value in range(1, num + 1):
        if value % 3 == 0 or value % 5 == 0:
            result += value
    return result

# These examples should all print True
print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)