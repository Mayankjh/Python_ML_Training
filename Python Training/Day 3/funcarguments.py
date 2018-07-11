def area(l,b):
    area1 = 0.5*l*b;
    area2 = l*b
    print('area is:-', area1)
    return area1,area2
# a= area(5,6)
a = area(b=3,l=10)
print('area of tri',a[0])
print('area of rec', a[1])

print(a) 