Serial No. 14
# PYTHON OPERATORS

Operators Are as given Below:
-> Arithematic Operators

// Perform floor division
+ To perform addition
- To perform subtraction
* To perform Multiplication
/ To perform division
% To return remainder after division
** Perform exponent(raise to Power)

Relational Operators:

<> similar to not equal !=

# Assignment Operators:
=
/=
+=
-=
*=
%=
**=

Logical Operators:
and
 or
Not

Membership OPERATORS
in: returns true if a variable is in seq of another variable else false
not in : returns true when not in seq else false

Identity OPERATORS
is :If identical or not
is not : If is not same

Note:

To comment single line use '#'
To comment multi line using '''some thing in between''' opened and closed
To comment multi line using """some thing in between""" opened and closed


# Input Output
use syntax input([prompt])

# Output
Type 1
print('something which is to be printed')

Type 2
a=5
print('the value of a is', a)

Type 3
print(*objects,sep='',end='\n') // end='' wirte the next thing in the same line

Type 4
x=5
y=10
print('the value of x is {} and y is {}'.format(x,y))

# importing  modules
use the syntax:
import ModuleName as something
Eg.
import math as m

Usage
a = m.pi

to avoid using following syntax :
use:
from ModuleName import ParticularModule
from math import pi

To import ALL
use :
from ModuleName import *

Conditiona statements

food='spam'
if food == 'spam':
    print('ummm, my favourite')
    print('i feel like saying it 100 times..')
    print(100*(food + '!'))
else:
print('something')


# chainedd conditionals
if exp:
   statements
elif
   statements
.
.
.
..
else:
   statements

# Loops
for Loops

eg.
for buddy in ['Karan', 'Kritarth', 'Geetansh']:
    invitation = "Hi " + buddy + " .Please come For The confrence call!"
    print(invitation)

# Tables
Use '\t'

# break statement:
used to break from the loop i.e exit from loop

# Continue statement
Used to skip the next step of loop and continue next steps

# pass statements
We do not use any stubs in python therefore we write pass in which nothing is operated
