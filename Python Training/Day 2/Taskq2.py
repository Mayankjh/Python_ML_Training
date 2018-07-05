#Program to find the area of triangle

a= float(input("Eter the Length of First Side :-"))
b= float(input("Eter the Length of Second Side :-"))
c= float(input("Eter the Length of Third Side :-"))

if(a+b>c and b+c>a and a+c>b):
    s= (a+b+c)/2
    area = (s*(s-a)*(s-b*(s-c))-1)/2
    print("Area Of triangle is :-",area)
else:
    print("The entered sides do not form a Triangle")