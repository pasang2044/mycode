#!/usr/bin/env python3
user_input = input("Please enter an IPv4 IP address:")

## the line below creates a single string that is passed to print()
# print("You told me the IPv4 address is:" + user_input)

## print() can be given a series of objects separated by a comma
print("You told me the IPv4 address is:", user_input)



vendor_name = input("What is the name of the vendor? ")

print("Your vendor name is ", vendor_name)


day = input("What day of the week is it?\n>")
name = input("What is your name?\n>")
print(f"Hello, {name}! Happy {day}!")


# PRINT OBJECTS
print("Hello, ",name,"! Happy ",day,"!", sep="")
# CONCATENATION
print("Hello, " + name + "! Happy " + day + "!")
# FORMAT METHOD
print("Hello, {}! Happy {}!".format(name, day))

