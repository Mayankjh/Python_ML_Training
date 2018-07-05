#Program to swap two no. without using third variable
print("#Program to swap two no. without using third variable")
a= int(input("Enter the First Number :-"))
b =int(input("Enter the Second Number :-"))
a=a+b
b=a-b 
a=a-b
print('Value of first no. after swapping is :',a,'\n Value of second no. after swapping :',b) 

#Program to swap two no.  using third variable
print("#Program to swap two no.  using third variable")
c= int(input("Enter the First Number :-"))
d =int(input("Enter the Second Number :-"))
temp = c
c = d
d = temp
print('Value of first no. after swapping is :',c,'\n Value of second no. after swapping :',d) 
