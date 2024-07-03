def oddities(arr):
    if len(arr) == 0:
        return arr
    odd_list = []
    for index, element in enumerate(arr):
        if index % 2 == 0:
            odd_list.append(element)
    return odd_list

print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities([1, 2, 3, 4]) == [1, 3])        # True
print(oddities(["abc", "def"]) == ['abc'])     # True
print(oddities([123]) == [123])                # True
print(oddities([]) == [])                      # True