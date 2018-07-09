class Human:
    def __init__(self,name,gender,occupation,speaks,dowork):
        self.name = name
        self.gender = gender
        self.occupation = occupation
        self.speaks = speaks
        self.dowork = dowork
    def PrintData(self):
        print("Name :", self.name)
        print("Gender :", self.gender)
        print("Gccupation :", self.occupation)
        print("Speaks :", self.speaks)
        print("Do work :", self.dowork)
t = Human("Tom","male","actor","I am Ethen hunt in Mission Impossible","shoot movie")
t.PrintData()
m = Human("maria sharapova", "female","tennis palyer", "I play tennis", "Play")
m.PrintData()
    
        