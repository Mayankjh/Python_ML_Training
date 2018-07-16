# program to show the use of lambda functions 

# double = lambda x:x*2
# 
#   # Output:10
# 
# print(double(5))
# 
# li = [1,2,3,4,5,6,7,8]
# 
# final_list  = list(filter(lambda x: (x%2!=0),li))
# final_list1  =filter(lambda x: (x%2!=0),li)
# print(final_list)
# print(final_list1)

# def alter(values,check):
#     return [ val for val in values if check(val)]
# 
my_list = [1,2,3,4,5]
# ano_list=alter(my_list,lambda x: x!=5)
# print(ano_list)

list1 =list(filter(lambda x:x!=5,my_list))
print(list1) 