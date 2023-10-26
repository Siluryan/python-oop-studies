class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age  = age

    def show(self):
        print(f'I am {self.name} and I am {self.age} years old')

    def speak(self):
        print('Idk whatysay')


class Pokemon:
    def __init__(self, name, age, element):
        self.name    = name
        self.age     = age
        self.element = element

    def show(self):
        print(f'I am {self.name} and I am {self.age} years old and I am an POKÉMON!')

    def speak(self):
        print('Idk whatysay')


class Cat(Pet):
    def speak(self):
        print('Meow')


class Dog(Pet):
    pass
    # def speak(self):
    #     print('Bark')


# class Fish(Pet):
#     def __init__(self, name, age, color):
#         super().__init__(name, age)
#         self.color = color

#     def speak(self):
#         print('Gloobs')

class Fish(Pokemon):
    def __init__(self, name, age, element, color):
        super().__init__(name, age, element)
        self.color = color

    # def speak(self):
    #     print('Gloobs')
    

class SuperFish(Pokemon):
    def __init__(self, name, age, element, color):
        super().__init__(name, age, element)
        self.color = color

    def speak(self):
        print('Gloobs')


dog = Dog('Doggerson', 5)
dog.speak()

cat = Cat('Mialselino', 3)
cat.speak()

# fish1 = Fish('Fishisto', 0, 'blue')
# fish1.show()

fish1 = Fish('Fishisto', 0, 'AQUA','blue')
fish1.show()

fish2 = SuperFish('Magikarp', 0, 'AQUA', 'orange')
fish2.show()
