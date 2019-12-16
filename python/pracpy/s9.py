#More on Classes

class Example:
    number = 0
    name = "noname"

def Main():
    me = Example()
    me.number = 1233
    me.name = "Augustus"

    friend = Example()
    friend.number = 3
    friend.name = "Abraham"

    empty = Example()

    print("Name: " +  me.name + ", Favorite number: " + str(me.number))
    print("Name: " +  friend.name + ", Favorite number: " + str(friend.number))
    print("Name: " +  empty.name + ", Favorite number: " + str(empty.number))

if __name__ == '__main__':
    Main()