"""
main.py
Student Management System - CPE106L Experiment 1 PostLab
Menu-driven program that uses the Person, Student, Instructor,
and StudentManager classes.
"""

from courses import COURSES, PROGRAM_INFO, find_course, display_courses
from instructor import Instructor
from manager import StudentManager

MENU = """
========== STUDENT MANAGEMENT SYSTEM ==========
 1. Add Student
 2. Update Student
 3. Delete Student
 4. Search Student
 5. Display Student Records
 6. Add Grade
 7. Compute Average Grade
 8. Display Course Information
 9. Display All People (Polymorphism)
 0. Exit
==============================================="""


def ask_course():
    display_courses()
    while True:
        course = find_course(input("Enter course code: "))
        if course:
            return course
        print("Invalid course code. Choose from the list above.")


def add_student(manager):
    student_id = input("Student ID: ").strip()
    name = input("Name: ").strip()
    email = input("Email: ").strip()
    course = ask_course()
    manager.add_student(student_id, name, email, course)
    print(f"Student {name} added.")


def update_student(manager):
    student_id = input("Student ID to update: ").strip()
    if manager.get_student(student_id) is None:
        print("Student not found.")
        return
    print("Press Enter to keep the current value.")
    name = input("New name: ").strip()
    email = input("New email: ").strip()
    course = ask_course() if input("Change course? (y/n): ").lower() == "y" else None
    manager.update_student(student_id, name, email, course)
    print("Record updated.")


def delete_student(manager):
    student_id = input("Student ID to delete: ").strip()
    removed = manager.delete_student(student_id)
    print(f"Deleted {removed.get_name()}.")


def search_student(manager):
    results = manager.search(input("Enter ID or name to search: "))
    if not results:
        print("No matching students.")
    for student in results:
        student.display_info()


def display_records(manager):
    if manager.count() == 0:
        print("No records yet.")
        return
    print(f"\n{'ID':<10}{'Name':<22}{'Course':<8}{'Average':>8}")
    print("-" * 48)
    for student in manager.all_students():
        record = student.to_record()          # dictionary
        print(f"{record['StudentID']:<10}{record['Name']:<22}"
              f"{record['Course']:<8}{record['Average']:>8.2f}")


def add_grade(manager):
    student = manager.get_student(input("Student ID: ").strip())
    if student is None:
        print("Student not found.")
        return
    student.add_grade(float(input("Grade (0-100): ")))
    print(f"Grades for {student.get_name()}: {student.get_grades()}")


def compute_average(manager):
    student_id = input("Student ID (leave blank for class average): ").strip()
    if not student_id:
        print(f"Class average: {manager.class_average():.2f}")
        return
    student = manager.get_student(student_id)
    if student is None:
        print("Student not found.")
    else:
        print(f"{student.get_name()}'s average: {student.get_average():.2f}")


def display_course_info():
    code, title, school = PROGRAM_INFO
    print(f"\nSubject: {code} - {title} ({school})")
    print(f"Number of courses offered: {len(COURSES)}")
    display_courses()


def display_all_people(manager, instructors):
    people = instructors + manager.all_students()
    for person in people:
        person.display_info()     # same call, different output per class
        print()


def main():
    manager = StudentManager()
    instructors = [Instructor("EMP-1024", "Engr. Ana Reyes",
                              "areyes@mapua.edu.ph", "Computer Engineering")]

    actions = {
        "1": lambda: add_student(manager),
        "2": lambda: update_student(manager),
        "3": lambda: delete_student(manager),
        "4": lambda: search_student(manager),
        "5": lambda: display_records(manager),
        "6": lambda: add_grade(manager),
        "7": lambda: compute_average(manager),
        "8": display_course_info,
        "9": lambda: display_all_people(manager, instructors),
    }

    while True:
        print(MENU)
        choice = input("Choose an option: ").strip()
        if choice == "0":
            print("Goodbye!")
            break
        action = actions.get(choice)
        if action is None:
            print("Invalid option.")
            continue
        try:
            action()
        except (ValueError, KeyError) as error:
            print("Error:", error)


if __name__ == "__main__":
    main()
