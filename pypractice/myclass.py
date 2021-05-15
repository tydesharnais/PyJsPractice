class Myclass:
    number = 0
    name = "noname"

def Main():
    me = Myclass()
    me.number = 1337
    me.name = "Ty"

    friend = Myclass()
    friend.number = 3
    friend.name = "Jay"

    empty = Myclass()

    print("Name: " + me.name + ", Favorite Number: " + str(me.number))
    print("Name: " + friend.name + ', Favorite Number: ' + str(friend.number))
    print('Name: ' + empty.name + ', Favorite Number: ' + str(empty.number))

if __name__ == '__main__':
    Main()
