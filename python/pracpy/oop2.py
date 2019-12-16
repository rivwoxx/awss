#class robot
#r1 object1 tom
#r2 object2 jerry
#class person
    #methods for this class
    #sit_down()
    #stand_up()
#p1 ob1 alice
#p2 obj2 becky

class Robot:
     #constructor
    def __init__(self, name, color, weight): 
        self.name = name
        self.color = color
        self.weight = weight    

    def introduce_self(self):   #method of the class robot
        print('My name is ' + self.name)

r1 = Robot("Tom", "red", 30)
r2 = Robot("Jerry", "blue", 40)

class Person:
    def __init__(self,n,p,i):
        self.name = n
        self.personality = p
        self.is_sitting = i
    
    def sit_down(self):
        self.is_sitting = True
    
    def stand_up(self):
        self.is_sitting = False

    def introduce_self(self):   #method of the class robot
        print('My name is ' + self.name)


p1 = Person("Alice", "agressive", False)
p2 = Person("Becky", "talkactive", True)

p1.robot_owned = r2
p2.robot_owned = r1

p1.introduce_self()
p2.introduce_self()

p1.robot_owned.introduce_self()
p2.robot_owned.introduce_self()
