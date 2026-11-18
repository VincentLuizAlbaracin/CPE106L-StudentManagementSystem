"""
student.py
Student inherits from Person and adds a student ID, a course (tuple),
and a list of grades.
"""

from person import Person


class Student(Person):
    """A student enrolled in a course, with a list of grades."""

    def __init__(self, student_id, name, email, course):
        super().__init__(name, email)        # inherit name and email
        self.__student_id = student_id
        self.__course = course               # tuple: (code, title, years)
        self.__grades = []                   # list of grades

    # ----- Getters -----
    def get_student_id(self):
        return self.__student_id

    def get_course(self):
        return self.__course

    def get_grades(self):
        return list(self.__grades)           # return a copy, not the original

    # ----- Setters / updaters -----
    def set_course(self, course):
        self.__course = course

    def add_grade(self, grade):
        if not 0 <= grade <= 100:
            raise ValueError("Grade must be between 0 and 100.")
        self.__grades.append(grade)

    def get_average(self):
        if not self.__grades:
            return 0.0
        return sum(self.__grades) / len(self.__grades)

    # ----- Overridden methods (polymorphism) -----
    def role(self):
        return "Student"

    def display_info(self):
        super().display_info()
        grades = ", ".join(str(g) for g in self.__grades) or "No grades yet"
        print(f"  ID      : {self.__student_id}")
        print(f"  Course  : {self.__course[0]} - {self.__course[1]}")
        print(f"  Grades  : {grades}")
        print(f"  Average : {self.get_average():.2f}")

    def to_record(self):
        """Returns the student's data as a dictionary."""
        return {
            "StudentID": self.__student_id,
            "Name": self.get_name(),
            "Email": self.get_email(),
            "Course": self.__course[0],
            "Grades": self.get_grades(),
            "Average": round(self.get_average(), 2),
        }
