# Class
The class statement creates a new class defination. The naem of the class
class ClassName:
  Body
  ..

 eg.
 class Myclass:
    variable = "blah"
    def function(self):
       print("This is a message inside the class.")

 myobject= Myclass()

 myobject.variable

NOTE:-
 ->Here Self is a defination for the function to have no arguments
 ->it is necessary for class with no arguments to have self as argument.

# consrtuctor in Python

 class function begins with double underscore(__) acre called special functions
 as they have special meaning. of one particular interest is the __init__() function.
 this is how class is instantiated.

 eg.
 class complexNumber:
     def __init__(self,r=0,i=0):
       self.real=r
       self.image = i
     def getData(self):
     print("{0}+{1}j".format(self.real,self.imag))

 # isinstance() function
  tells whether the object belongs to class or not 
  Syntax: isinstance(object,classinfo)

 # issubclass(class,class) function
 checks whether forst class is subclass of second class

 # Multiple Inheritance

 class Father:

# Super() keyword

