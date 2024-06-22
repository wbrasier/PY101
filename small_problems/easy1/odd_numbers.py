# print odd numbers from 1 up to and including 99 with one number per line
# BONUS: input: 2 ints (starting value and ending value)
# BONUS: output: all odd numbers between (and including end) the two inputs


for num in range(1,100,2):
    print(num)

# BONUS

start = int(input("Starting value: "))
end = int(input("Ending value: "))

for num in range(start, end + 1):
    if num % 2 == 1:
        print(num)