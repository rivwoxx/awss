#vector 2D
class Vector2D:
    x = 0.0
    y = 0.0
    
    #method
    def __init__(self, x, y):
        self.x = x
        self.y = y 

def Main():
    vec = Vector2D(5,6)
    print("X: " + str(vec.x) + " Y: " + str(vec.y))

if __name__ == "__main__":
    Main()    