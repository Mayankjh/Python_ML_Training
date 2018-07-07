# Program To calculate the average of numbers given in list
import numpy as np
a = int(input("Enter the no. of elements in list:-"))
list1 = []
for a in range(a):
    n= float(input("Enter Number :"))
    list1.append(n)

print(np.mean(list1))