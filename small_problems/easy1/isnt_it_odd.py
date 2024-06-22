# input: one integer
# output: boolen
# rules: function that return True if abs value of input is odd, otherwise return False

def odd_abs_value(num):
    return num % 2 != 0

print(odd_abs_value(-9))
print(odd_abs_value(0))
print(odd_abs_value(2))