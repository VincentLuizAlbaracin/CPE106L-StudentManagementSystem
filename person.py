"""
person.py
Base class for every person in the system.
Attributes are private (double underscore) and accessed through
getters and setters (encapsulation).
"""


class Person:
    """Represents a person with a name and an email address."""

    def __init__(self, name, email):
        self.__name = name
        self.__email = email

    # ----- Getters -----
    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    # ----- Setters with validation -----
    def set_name(self, name):
        if not name.strip():
            raise ValueError("Name cannot be empty.")
        self.__name = name.strip()

    def set_email(self, email):
        if "@" not in email:
            raise ValueError("Invalid email address.")
        self.__email = email.strip()

    # ----- Methods meant to be overridden (polymorphism) -----
    def role(self):
        return "Person"

    def display_info(self):
        print(f"[{self.role()}]")
        print(f"  Name  : {self.__name}")
        print(f"  Email : {self.__email}")
