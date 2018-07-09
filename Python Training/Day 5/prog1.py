# class complexNumber:
#     def __init__(self,r=0,i=0):
#         self.real=r
#         self.image = i
#        
#     def getData(self):
#         print("{0}+{1}j".format(self.real,self.image))
#      
# 
# a =complexNumber(3,5)
# a.getData()

class vehicle:
    name=None
    def __init__(self,n,c,t,v):
        self.name = n
        self.color = c
        self.type = t
        self.value = v
    
    def PrintData(self):
        print("{} is a {} {} worth {}" .format(self.name,self.color,self.type,self.value))
a = vehicle("fer","red","convirtible","$600000")
a.PrintData()
a2=vehicle("jump","blue","van","$10000")
a2.PrintData()

