# Problem 3
# Largest prime factor
#
# The prime factors of 1 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

import sys
result = 0
number = int(sys.argv[1])

#getting the factors list
num = number
factor = num
factorList = []
primeList = []
# primeCheck = 0

while factor != 1:
    if num%factor == 0:
        fractionResult = num/factor
        factorList.append(fractionResult)
    factor = factor - 1

print "All the factors of number" , num, ": ", factorList

for factorInList in factorList:
    x = factorInList
    primeCheck = 0
    for factorInList2 in factorList:
        primeMod = x%factorInList2
        if primeMod == 0:
            primeCheck = primeCheck + 1
    if primeCheck == 2:
        print x, "was considered prime"
        primeList.append(x)

print "Prime factors of", num, ":", primeList
