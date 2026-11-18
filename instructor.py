"""
instructor.py
Instructor inherits from Person and adds an employee ID and department.
"""

from person import Person


class Instructor(Person):
    """An instructor who belongs to a department."""

    def __init__(self, employee_id, name, email, department):
        super().__init__(name, email)
        self.__employee_id = employee_id
        self.__department = department

    def get_employee_id(self):
        return self.__employee_id

    def get_department(self):
        return self.__department

    # ----- Overridden methods (polymorphism) -----
    def role(self):
        return "Instructor"

    def display_info(self):
        super().display_info()
        print(f"  Employee ID : {self.__employee_id}")
        print(f"  Department  : {self.__department}")
