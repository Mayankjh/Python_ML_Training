## Lambda function

* while the normal functions are defined using the keyword the  def keyword, in the python
anonymous functions are defines using the lambda keyword.

=> Syntax 
  Example of Lambda Functions in python

  # program to show the use of lambda functions 

  double = lambda x:x*2

  # Output:10

  print(double(5))

## filter() , Map() and reduce() functions in lambda

# Filter example

li = [1,2,3,4,5,6,7,8]

final_list  = list(filter(lambda x: (x%2!=0),li))

print(final_list)

## alter without filter

def alter(values,check):
    return [ val for val in values if check(val)]

my_list = [1,2,3,4,5]
ano_list=alter(my_list,lambda x: x!=5)
print(ano_list)


## same example using filter

list1 =list(filter(lambda x:x!=5,my_list))
print(list1) 

## Python Expression 

* capitalize() => capitalize first letter of string
* upper() => convert lowercase letters in string to uppercase.
* swapcase() => Invert case for all letters in string
* strip()  => return or remove white spaces inthe start & end of the string
* str.replace(old,new[,max]) => old have been replaced with new
* isalnum() returns true if string has atleat 1 character and all characterstics are alphanumeric and false otherwise.
* isdigit() => returns true if string only digits and false otherwise
* isnumeric()
* str.join(obj) => s="-"; seq=("a","b","c"); concats like a string

## USe of lambda() with map()

* The map( function contains in Python takes in a function and list as argument.
  the function is called with a lambda and a list and a new list is returned which contains all the lambda mordified items.