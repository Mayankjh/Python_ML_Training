#Write a Program to Print all Integers that Aren’t Divisible by Either 2 or 3 and Lie between 1 and 50
for n in range(1,50):
    if(n%2 !=0 and n%3!=0):
        print(n)
          