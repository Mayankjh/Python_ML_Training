# import time as t
# a= ["sonic","CN","pogo","hungama","nick","disney","zetX","discovery"]
# b= iter(a)
# c = reversed(a)
# for channels in a:
#    print(next(c))
#    t.sleep(1)  
   
class RemoteControl():
    def __init__(self):
        self.channels = ["sonic","CN","pogo","hungama","nick","disney","zetX","discovery"]
        self.index= -1
    def __iter__(self):
        return self
    def __next__(self):
        self.index += 1
        if self.index == len(self.channels):
            self.index=0
        return self.channels[self.index]
r = RemoteControl()
itr = iter(r)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
