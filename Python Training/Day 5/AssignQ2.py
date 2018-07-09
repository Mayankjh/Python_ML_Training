# Prog to find GCD

import fractions
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
print("The GCD of the two numbers is",fractions.gcd(a,b))

#using recurssion
# def gcd(a,b):
#     if(b==0):
#         return a
#     else:
#         return gcd(b,a%b)
# a=int(input("Enter first number:"))
# b=int(input("Enter second number:"))
# GCD=gcd(a,b)
# print("GCD is: ")
# print(GCD)