
class Employee:
    """
    This class represent an employee of the company
    """

    number = 0

    def __init__(self, nom, age, salary, location):
        self.nom = nom
        self.age = age
        self.salary = salary
        self.location = location
        self.number += 1

    def end_contract(self):
        return self.start_date + self.time


