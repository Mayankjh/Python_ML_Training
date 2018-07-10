import time as t
a= ["sonic","CN","pogo","hungama","nick","disney","zetX","discovery"]
b= iter(a)
c = reversed(a)
for channels in a:
   print(next(c))
   t.sleep(1)  
   
class RemoteControl():
    def __init__(self):
        self.channels = ["sonic","CN","pogo","hungama","nick","disney","zetX","discovery"]
        self.index= -1
    