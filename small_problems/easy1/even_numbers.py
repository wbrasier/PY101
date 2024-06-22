# input: none
# output: all even numbers from 1 to 99 with each num on a line
# iterate over a range

for num in range(1, 100):
    if num % 2 == 0:
        print(num)