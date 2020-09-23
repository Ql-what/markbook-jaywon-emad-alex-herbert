"""
Markbook Application
Group members: 
"""
from typing import Dict


def create_assignment(name: str, due: str, points: int) -> Dict:
    """Creates an assignment represented as a dictionary
    
    Args:
        name: the name of the assignment.
        due: the due date for the assignment.
        points: what the assignment is out of (denominator).
    Returns:
        Assignment as a dictionary.
    """
    Assignment = {
        'name': name,
        'due': due,
        'points': points
    }

    return Assignment


def create_classroom(course_code: str, course_name: str, period: int, teacher: str) -> Dict:
    """Creates a classroom dictionary"""
    Classroom = {
        'course_code': course_code,
        'course_name': course_name,
        'period': period,
        'teacher': teacher,
    }

    return Classroom 


def calculate_average_mark(student: Dict) -> float:
    sum = 0
    marks = student['marks']
    for num in marks:
        sum += num

    average = sum/len(marks)
    
    return average


def add_student_to_classroom(student: Dict, classroom: Dict):
    """Adds student to a classroom

    Args:
        student: Student dict
        classroom: The classroom to add the student to
    """
    pass


def remove_student_from_classroom(student: Dict, classroom: Dict):
    """Removes student from classroom

    Args:
        student: The student to be removed
        classroom: the class from which the student will be removed.
    """
    pass


def edit_student(student: Dict, **kwargs: Dict):
    """Edits the student's info with the provided key/value pairs

    Args:
        student: The student whose data needs to be udated.
        **kwargs: KeyWordARGumentS. The key/value pairs of the
            data that needs to be changed. Can come in the form
            of a dictionary.
    """
    pass
