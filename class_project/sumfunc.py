#!/usr/bin/env python3


#Write a Python function to sum all the numbers in a list.
sum = 0

number_list = []
n = int(input("Enter the desired list size " ))

print("\n")
for i in range(0,n):
    print("Enter your number at index", i,)
    item = int(input())
    number_list.append(item)
print(" Here is your list ", number_list)

for elements in range (0, len(number_list)):
    sum = sum + number_list[elements]

print("Sum of all the elements in the given list : ", sum)
