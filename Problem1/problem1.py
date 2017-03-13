# Problem 1, simple program that finds the sum of all
# the multiples of 3 or 5 below 1000.

numbers = range(1, 1000, 1)
result = 0

for number in numbers:
    if number%3 == 0 or number%5 == 0:
        result += number

print result
