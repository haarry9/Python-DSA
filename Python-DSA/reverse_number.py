'''
Problem Statement: 
Given a number N reverse the number and print it.
'''

def rev_num(n):
    x=n
    rem=0
    while(x != 0):
        rem = rem*10 + x%10
        x//=10
    return rem


n = int(input("Enter input: "))
print("The reverse of the {} is {}".format(n, rev_num(n)))