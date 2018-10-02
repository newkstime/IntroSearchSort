from comparable import Comparable
from date import Date

class Person(Comparable):
    """
    This class is immutable and inherits from Comparable
    It uses composition by having a Date object for birthday
    Please code this using private instance variables.
    Each instance variable should have a getter, but no setters
    Code the compare method, and call the base class compare
    Code a __str__ method
    """

    def __init__(self, name, year, month, day):
        super().__init__()
        self.__name = name
        self.__birthday = Date(year, month, day)

    def get_name(self):
        return self.__name

    def get_birthday(self):
        return self.__birthday

    def compare(self, other_person):
        this_name = self.get_name()
        other_name = other_person.get_name()
        other_person_date = other_person.get_birthday()
        Comparable.compare(other_person)
        compare_result = self.__birthday.compare(other_person_date)

        if compare_result == 1:
            return 1
        elif compare_result == -1:
            return -1
        else:
            if this_name > other_name:
                return 1
            elif this_name < other_name:
                return -1
            else :
                return 0


    def __str__(self):
        return self.__name + " " + str(self.__birthday)
