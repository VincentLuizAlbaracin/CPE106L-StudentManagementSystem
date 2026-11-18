"""
manager.py
StudentManager stores all student records in a dictionary
(key = student ID, value = Student object) and provides the
add, update, delete, search, and display features.
"""

from student import Student


class StudentManager:
    """Manages a collection of Student objects."""

    def __init__(self):
        self.__records = {}          # dictionary: {student_id: Student}

    def add_student(self, student_id, name, email, course):
        if student_id in self.__records:
            raise ValueError(f"Student ID {student_id} already exists.")
        student = Student(student_id, name, email, course)
        self.__records[student_id] = student
        return student

    def get_student(self, student_id):
        return self.__records.get(student_id)

    def update_student(self, student_id, name=None, email=None, course=None):
        student = self.get_student(student_id)
        if student is None:
            raise KeyError(f"No student with ID {student_id}.")
        if name:
            student.set_name(name)
        if email:
            student.set_email(email)
        if course:
            student.set_course(course)
        return student

    def delete_student(self, student_id):
        if student_id not in self.__records:
            raise KeyError(f"No student with ID {student_id}.")
        return self.__records.pop(student_id)

    def search(self, keyword):
        """Finds students whose ID or name contains the keyword."""
        keyword = keyword.lower()
        return [s for s in self.__records.values()
                if keyword in s.get_student_id().lower()
                or keyword in s.get_name().lower()]

    def all_students(self):
        return list(self.__records.values())

    def class_average(self):
        averages = [s.get_average() for s in self.__records.values()
                    if s.get_grades()]
        if not averages:
            return 0.0
        return sum(averages) / len(averages)

    def count(self):
        return len(self.__records)
