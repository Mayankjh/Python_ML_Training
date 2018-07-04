#use brak continue and pass

for i in [10,21,23,34,45]:
    if i % 2==1: #if no is odd
        continue
    print(i)
print("done")

for i in [10,21,23,34,45]:
    if i % 2==1: #to get first no odd
        break
    print(i)
print("done")

    
for i in [10,21,23,34,45]:
    if i % 2==1: #to get first no odd
       pass
       print('this is pass block')
    print(i)
print("done")

