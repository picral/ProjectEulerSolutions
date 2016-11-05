# -*- coding: utf-8 -*-
"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

"""
x_0 = 1
x_1 = 2
count = 2

while x_1 < 4000001:    
    z = x_1
    x_1 = z + x_0
    x_0 = z
    if x_1%2 == 0:
        count =x_1 + count
print(count)