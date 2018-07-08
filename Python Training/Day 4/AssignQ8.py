a=int(input("Enter a number:"))
sum=0
while(a>0):
    digit=a%10
    sum=sum+digit
    a=a//10
print("The total sum of digits is:",sum)