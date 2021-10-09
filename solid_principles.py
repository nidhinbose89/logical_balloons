from enum import Enum
from abc import ABC, abstractmethod

# Single-responsibility principle [SRP]
# A class should have only reason to change.
# this increases reusability.
def print_k():
    print("SRP -- From K")
def print_m():
    print("SRP -- From M")

def main():
    print_k()
    print_m()
main() # main has single resp of calling child classes

# The Open–closed principle [OCP]
# Software entities should be open for extension but closed for modification.
# this makes implementations less error prone; and allow easy refactoring wiht reusable 
# small components
class T(ABC):
    @abstractmethod
    def test(self):
        print("From Base Class")

class M(T):
    def test(self): print("OCP -- From M")

class K(T):
    def test(self): print("OCP -- From K")

# class T is open for extension but closed for modification
for each in T.__subclasses__():
    each().test()


# Liskov substitution principle [LSP]
"""
Objects in a program should be replaceable with instances of their subtypes
 without altering the correctness of that program.

If in a subclass, you redefine a function that is also present in the base class, 
the two functions ought to have the same behaviour. This, though, does not mean that 
they must be mandatorily equal, but that the user, should expect that the same `type`
of result, given the same input.
"""
class Car:
    def __init__(self, type):
        self.type = type
        self._properties = {}
    def set_properties(self, color, gear):
        self._properties = {'color':color, 'gear':gear}
    def get_properties(self):
        return self._properties
    @property
    def properties(self):
        return self._properties

class PetrolCar(Car):
    def __init__(self, type):
        self.type = type
        self._properties = {}

car_1 = Car('BMW'); car_1.set_properties('green', 4)
car_2 = PetrolCar('BMW'); car_2.set_properties('blue', 4)
car_3 = Car('AUDI'); car_3.set_properties('green', 3)
cars = [car_1, car_2, car_3]
def find_cars(color='green'):
    count = 0
    for car in cars:
        if car.properties.get('color', '') == color:
            count += 1
    return count
print(find_cars('green'), 'Liskov substitution principle')


# Interface Segregation Principle [ISP]
# keep base class as simple as possible; if base is fat, 
# it would need rework once a base inherits and it doesnt need functionality
# then need would arise to add/inherited automatically dummy methods.
class Walker(ABC):
  @abstractmethod
  def walk(self) -> bool:
    return print("ISP-Can Walk") 

class Swimmer(ABC):
  @abstractmethod
  def swim(self) -> bool:
    return print("ISP-Can Swim") 

class Human(Walker, Swimmer):
  def walk(self):
    return print("ISP-Humans can walk") 
  def swim(self):
    return print("ISP-Humans can swim") 

class Whale(Swimmer):
  def swim(self):
    return print("ISP-Whales can swim") 

if __name__ == "__main__":
  h1 = Human()
  h1.walk()
  h1.swim()
  f1 = Whale()
  f1.swim()
#   f1.walk()  # WOULDN't WORK!


# Dependency Inversion Principle [DIP]
'''
Abstractions should not depend on details. 
Details should depend on abstraction.
[ie, there should be an abstract class which outlines functionalities]
High-level modules should not depend on low-level modules.
Both should depend on abstractions
Implicitly followed if you follow:
    Open-Closed Principle
    Liskov Substitution Principle
'''

class Team(Enum):
    BLUE = 1
    RED = 2
    GREEN = 3

class Student:
    def __init__(self, name) -> None:
        self.name = name


class TeamMembershipLookup:
    @abstractmethod
    def find_all_students_of_team(self):
        pass

class TeamMembership(TeamMembershipLookup):
    def __init__(self) -> None:
        self.team_memberships = []

    def add_team_memberships(self, student, team):
        self.team_memberships.append((student, team))

    def find_all_students_of_team(self, team):
        for mems in self.team_memberships:
            if mems[1] == team:
                yield mems[0].name
class Analysis:
    def __init__(self, team_membership_lookup, team_name):
        for student in team_membership_lookup.find_all_students_of_team(team_name):
            print(f'DIP-{student} is in Team: {team_name.name}')
s1 = Student('Tom')
s2 = Student('Dick')
s3 = Student('Harry')
memberships = TeamMembership()
memberships.add_team_memberships(s1, Team.RED)
memberships.add_team_memberships(s2, Team.RED)
memberships.add_team_memberships(s3, Team.BLUE)

Analysis(team_membership_lookup=memberships, team_name=Team.RED)
'''
TeamMembershipLookup -- this abstract class implements DIP
Without it, Analysis higher level class would depend on 
TeamMembership high level class

'''