integer = int(input('Please enter an integer greater than 0: '))

action = input('Enter "s" to compute the sum, or "p" to compute the product. ')

if action == 's':
    action_word = 'sum'
    result = 0
    for num in range(1,integer + 1):
        result += num
else:
    action_word = 'product'
    result = 1
    for num in range(1, integer + 1):
        result *= num

print(f'The {action_word} of the integers between 1 and {integer} is {result}.')