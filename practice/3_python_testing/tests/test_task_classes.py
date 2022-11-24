"""
Write tests for classes in 2_python_part_2/task_classes.py (Homework, Teacher, Student).
Check if all methods working correctly.
Also check corner-cases, for example if homework number of days is negative.
"""

import pytest
import sys
sys.path.append("..")
from tasks.task_classes import Teacher, Student, Homework


# tests for teacher class
@pytest.fixture
def teacher():
    return Teacher("John", "Doe")


@pytest.fixture
def student():
    return Student("Anna", "Smith")


@pytest.fixture
def homework1():
    return Homework("Read an article", 3)


@pytest.fixture
def homework2():
    return Homework("Solve math problems", 0)


def test_init_teacher(teacher):
    assert teacher.first_name == "John"
    assert teacher.last_name == "Doe"


def test_create_homework(teacher):
    homework = teacher.create_homework("Write an essay", 5)
    assert homework.days_to_complete == 5
    assert homework.text == "Write an essay"


def test_create_homework_invalid(teacher):
    with pytest.raises(ValueError):
        teacher.create_homework("Learn pytest", -20)


def test_init_student(student):
    assert student.first_name == "Anna"
    assert student.last_name == "Smith"


def test_do_homework(student, homework1):
    student.do_homework(homework1)
    assert homework1.is_active()


def test_init_homework(homework1):
    assert homework1.text == "Read an article"
    assert homework1.days_to_complete == 3
    assert homework1.is_active()


def test_deadline(homework2):
    assert not homework2.is_active()

