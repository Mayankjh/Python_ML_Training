usa = ["atlanta","new york","chicago","baltimore"]
uk = ["london","bristol","cambridge"]
india = ["mumbai","delhi","banglore"]
a= input("Enter the city:")
if  a in uk :
    print("The city belongs to UK ")
elif a in usa:
    print("The city belongs to USA ")
elif a in india:
    print("The city belongs to India ")
else:
    print("City is not in the list/Wrong Input")
b= input("Enter the city 1:")
c= input("Enter the city: 2")
if  b and c in uk :
    print("The city belongs to UK ")
elif b and c in usa:
    print("The city belongs to USA ")
elif b and c in india:
    print("The city belongs to India ")
else:
    print("The Cities are not from the same country")