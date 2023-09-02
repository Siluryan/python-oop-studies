class Person:
    number_of_people = 0

    def __init__(self, name) -> None:
        self.name = name
        Person.number_of_people += 1


p1 = Person("tim")
p2 = Person("jill")

print (Person.number_of_people)

class Ghost:

    number_of_people = 0

    @classmethod
    def _number_of_people(ghost):
        return ghost.number_of_people
    
    @classmethod
    def add_person(ghost):
        ghost.number_of_people += 1        
    
print(Ghost.number_of_people)

Ghost.add_person()

print(Ghost.number_of_people)



