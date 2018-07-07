# Print All no. in range divisible by a given no.
a = int(input("Enter The Starting Point of the Range:-"))
b = int(input("Enter The Ending Point of the Range:-"))
n = int(input("Enter No. whose factors are to br looked for in the range"))
for num in range(a,b):
    if(num % n ==0):
        print(num)
        
    
