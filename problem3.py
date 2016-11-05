# -*- coding: utf-8 -*-
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""
import math

def is_prime(x):    
    if x % 2 == 0 and x>2:
        return(False)
    for i in range(3,int(math.sqrt(x))+1, 2):
        if x % i == 0:
            return(False)
    return(True)

test_number = 600851475143
highest = 0
for i in range(1,test_number):
    if is_prime(i) == True and test_number%i ==0:
        highest = max(highest, i)
        print(highest)

print(is_prime(13187))