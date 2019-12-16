#class robot
#r1 object1 tom
#r2 object2 jerry

class Robot:
     #constructor
    def __init__(self, name, color, weight): 
        self.name = name
        self.color = color
        self.weight = weight    

    def introduce_self(self):   #method of the class robot
        print('My name is ' + self.name)

# r1 =  Robot()
# r1.name = "Tom"
# r1.color = "red"
# r1.weight = 30

# r2 = Robot()
# r2.name= "Jerry"
# r2.color= "blue"
# r2.weight= 50

r1 = Robot("Tom", "red", 30)
r2 = Robot("Jerry", "blue", 40)
#this just applied with the commented code r1 = robot() bla bla bla
#when you execute the following, in the method self will be the r1.name r1 instead of self, 
#whatever I said it made sense to me today I do not know whether it will be like that tomorrow
r1.introduce_self()
r2.introduce_self()