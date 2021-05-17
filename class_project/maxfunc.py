#!/usr/bin/env python3

# Write a Python function to find the Max of three numbers.
num1 = int(input("Enter a random number: \n >"))
num2 = int(input("Enter a random number: \n >"))
num3 = int(input("Enter a random number: \n >"))

def max_number(a,b,c):
    max=a
    if b>a:
        max=b
        if c>b:
            max=c
    else:
        if c>a:
            max=c
    return max;

print(f"The max of {num1}, {num2}, {num3} is ", max_number(num1,num2,num3))
