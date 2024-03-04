'''
Problem Statement:
Given an integer N, write a program to count the number of digits in N
'''


#soln-count remainders
def count_digits1(n):
    count =0
    x=n
    while(x !=0):
        x//=10
        count+=1
    return count

#soln-convert input to string and count len of string
def count_digits2(n):
    x=str(n)
    return len(x)


# soln - Use logarithm base 10 to count the number of digits. As
# The number of digits in an integer = the upper bound of log10(n).
# n = 12345
# log10(12345) = 4.091
# Integral part of 4.091 is 4 and 4 + 1 =  5 which is also the number of digits in 12345   

import math
def count_digits3(n):
    digits = math.floor(math.log10(n) +1)
    return digits

n = int(input("Enter input: "))
print("Number of digits in ",n," is ", count_digits3(n))
