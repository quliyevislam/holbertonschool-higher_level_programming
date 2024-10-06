#!/usr/bin/python3
"""This module contains Studen calss"""


class Student:
    """
    This class defines a student

    Attributes
        str : first_name
        str : last_name
        age : int

    Methods
    -------
        to_json() -> dict
            Retrieves a dictionary representation of a Student
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student"""
        return self.__dict__


students = [Student("John", "Doe", 23), Student("Bob", "Dylan", 27)]

for student in students:
    j_student = student.to_json()
    print(type(j_student))
    print(j_student['first_name'])
    print(type(j_student['first_name']))
    print(j_student['age'])
    print(type(j_student['age']))
