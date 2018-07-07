#Program to enter marks of 5 subjects and print their grade
import numpy as np
a = 5
list1 = []
for a in range(a):
    n= float(input("Enter Marks of subject out of 100:"))
    list1.append(n)
b = np.mean(list1)

if(b>=90):
    print("Your Grade: A")
elif(b>=80 and b<=89):
    print("Your Grade: B")
elif(b>=70 and b<=79):
    print("Your Grade: C")
elif(b>=60 and b<=69):
    print("Your Grade: D")
elif(b>=50 and b<=59):
    print("Your Grade: E")
else:
    print("Your Grade : F")
