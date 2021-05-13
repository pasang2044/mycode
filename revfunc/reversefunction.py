#!/usr/bin/env python3


# Write a Python program to reverse a string.


yourString = input("Enter your desired string : ")

reversedString = " "

for i in yourString:
    reversedString = i + reversedString

print("\nYour string was: ", yourString)
print("\nThe reversed string is: ",reversedString)
