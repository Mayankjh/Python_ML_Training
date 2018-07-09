#defining Class
class Myclass:
    variable = "blah"
    def function(self):
       print("This is a message inside the class.")

myobject= Myclass()

print(myobject.variable)
myobject.function()