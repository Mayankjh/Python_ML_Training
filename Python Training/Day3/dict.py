# d = dict(name='mayank',id=9,roll=42,branch='cse')
# print(d)

d= dict(one=1,two=2,three=3)
# print(d)
# for k in d:
#     print(k,d[k])
# for k in sorted(d.keys()):
#     print(k,d[k])
# for k,v in sorted(d.items()):
#     print(k,v)
# for v in sorted(d.values()):
#     print(v)
# for k in d:
#     print(d)
    
#append keys
# d['seven']=7
# print(d)
# s=d.get('three6767', "key not found!")
# print(s)     
# d.pop('one')  
# s= d.pop('indindi', 'key not found!')
# print(s)
# print(d)

del d['one']
print(d)

x= dict(om=2, mu=3,**d)
print(x)

print('this is d:-{}',.format(x))
