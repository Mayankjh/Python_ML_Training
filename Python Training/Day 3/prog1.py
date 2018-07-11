def area():
    print("Enter Your choice :-\n","Press 1 for Triangle\n","Press 2 for Circle\n")
    a= int((input("->")))
    if a==1:
        l=float(input("Enter Length:-"))
        b = float(input("Enter Bredth:-"))
        area1 = 0.5*l*b
        print('Area of rectangle =', area1)
    elif a==2:
        r=float(input("Enter Radius:-"))
        area1 = 3.14*r*r
        print('Area of rectangle =', area2)
    else:
        print('Wrong Choice')
    
area()