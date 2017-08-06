# Problem 3
# Largest prime factor
#
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?
import sys
import math

num = int(sys.argv[1])
given = int(sys.argv[1])
prime = {}
i = 2
while i < int(math.sqrt(num)):
    while num % i == 0:
        num /= i
        prime[i] = ""
    i += 1

if num != 1:
    prime[num] = ""

for key in prime.keys():
    print key, "was considered prime"
    print given, "divided by prime factor", key, "=", given/key
