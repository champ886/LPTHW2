## ANimal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## make class Dog is-a object Animal
class Dog(Animal):
    
    def __init__(self, name):
        ##from self get attribute name andf set it to name
        self.name = name 

    def my_name(self):
        print(self.name)

class Cat(Animal):

    def __init__(self, name):
        ## from self get attribute name and set it to name
        self.name = name
        #self.mary = mary

    def my_name_cat(self):
        print(self.name)
## make a class Person that is-a object
class Person(object):

    def __init__(self, name):
        ## from self, get attribute name and set it to name
        self.name = name


        ## Person has-a pet of some of some kind
        self.pet = None

    def my_name_person(self):
        print(self.name)
        print(self.pet)
## make class Employee that is-a object .Person
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## from self get attribute salary and set to salary
        self.salary = salary

    def my_employee(self):
        print(self.salary)


## make a class fish that is-a object
class Fish(object):
    pass

## make a class Salmon that is-a object fish
class Salmon(Fish):
    pass

## make a class Halibut that is-a object fish
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## Mary is-a Person
mary = Person("Mary")

## from mary get attribute pet and assign it to satan
mary.pet = satan

## set frank to an instance of Employee which takse Frank and 12000 params
frank = Employee("Frank", 120000)

## from frank get attribute pet and assign it to rover
frank.pet = rover

## set flipper to an instance of class Fish
flipper = Fish()

## set crouse to an instance of class Salmon
crouse = Salmon()

## set harry to Halibut
harry = Halibut


rover.my_name()

satan.my_name_cat()

mary.my_name_person()

#print(mary)

print("mary.pet==>", mary.pet)

#satan.mary

frank.my_employee()

frank.name 


#calling each attribute directly from the __init__  inheritance
print(frank.name, frank.salary)

#frank.my_employee(salary)

