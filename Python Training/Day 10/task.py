string = 'INDIA123DELHI'
#list = list(filter(lambda x: x!= '1' and x!='2' and x!='3',string))
list = list(filter(lambda x: x not in [str(n) for n in range(10)] ,string))
print((''.join(list)))

    