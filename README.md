# Student Management System

CPE106L Experiment 1 – PostLab
**Author:** Vincent Luiz S. Albaracin

A menu-driven Python program for managing student records. It combines Git version control, Python data structures, and object-oriented programming.

## How to Run
```
python main.py
```

## Features
1. Add Student
2. Update Student
3. Delete Student
4. Search Student
5. Display Student Records
6. Add Grade
7. Compute Average Grade (per student or whole class)
8. Display Course Information
9. Display All People (polymorphism demo)

## Project Structure
| File | Purpose |
|---|---|
| `courses.py` | Fixed course information stored as **tuples** |
| `person.py` | `Person` base class with private attributes, getters and setters (**encapsulation**) |
| `student.py` | `Student(Person)`: ID, course, and a **list** of grades (**inheritance**) |
| `instructor.py` | `Instructor(Person)`: employee ID and department (**inheritance**) |
| `manager.py` | `StudentManager`: stores records in a **dictionary** keyed by student ID |
| `main.py` | Menu and user interaction |

## Concepts Applied
- **Strings:** names, emails, and course information; formatted output
- **Lists:** each student's grades
- **Tuples:** fixed course data (code, title, years)
- **Dictionaries:** student records `{student_id: Student}`, and `to_record()` output
- **Encapsulation:** private `__` attributes accessed through getters and setters with validation
- **Inheritance:** `Student` and `Instructor` extend `Person`
- **Polymorphism:** `role()` and `display_info()` behave differently for each class
