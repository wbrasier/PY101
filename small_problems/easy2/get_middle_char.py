def center_of(string):
    length = len(string)
    
    if length == 1 or length == 2:
        return string
    
    middle_index = length // 2
    
    if length % 2 == 0:
        return string[middle_index - 1: middle_index + 1]
    return string[middle_index]

print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True