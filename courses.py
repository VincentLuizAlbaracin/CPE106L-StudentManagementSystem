"""
courses.py
Fixed course information stored as tuples.
Tuples are used because course data (code, title, years) should not change
while the program is running.
"""

# Each course: (course code, course title, years to complete)
COURSES = (
    ("BSCpE", "Bachelor of Science in Computer Engineering", 5),
    ("BSCS", "Bachelor of Science in Computer Science", 4),
    ("BSIT", "Bachelor of Science in Information Technology", 4),
    ("BSEE", "Bachelor of Science in Electrical Engineering", 5),
)

PROGRAM_INFO = ("CPE106L", "Software Design Laboratory", "Mapua University")


def find_course(code):
    """Returns the course tuple that matches the code, or None."""
    for course in COURSES:
        if course[0].lower() == code.strip().lower():
            return course
    return None


def display_courses():
    """Prints all available courses."""
    print(f"\n{'Code':<8}{'Title':<50}{'Years':>5}")
    print("-" * 63)
    for code, title, years in COURSES:
        print(f"{code:<8}{title:<50}{years:>5}")
