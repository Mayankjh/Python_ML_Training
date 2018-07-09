#
class Father:
    def skills(self):
        print('I enjoy Gradening,Programming')
class Mother:
    def skills(self):
        print("I enjoy cooking,Art")
class child(Father,Mother):
    def skills(self):
        print("I enjoy sports")
        Father.skills(self)
        Mother.skills()
o = child()
o.skills()
