
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        raise NotImplementedError('Subclass must implent abstract method')

class Cat(Pet):
    def __init__(self, name, age):
        super().__init__(name, age) #You can run super class methods like this

    def talk(self):
        return "Meowww"

class Dog(Pet):
    def __init__(self, name, age):
        super().__init__(name, age)

    def talk(self):
        return "Woooooffff"

def Main():
    pets = [Cat('jess', 3), Dog('buster', 4), Cat('rachel', 5), Pet('thePet', 5)]

    for pet in pets:
        print('Name:' + pet.name+", Age:" + str(pet.age)+", says:" +pet.talk())
if __name__ == '__main__':
    Main()
