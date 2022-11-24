"""
Create 3 classes with interconnection between them (Student, Teacher,
Homework)
Use datetime module for working with date/time
1. Homework takes 2 attributes for __init__: tasks text and number of days to complete
Attributes:
    text - task text
    deadline - datetime.timedelta object with date until task should be completed
    created - datetime.datetime object when the task was created
Methods:
    is_active - check if task already closed
2. Student
Attributes:
    last_name
    first_name
Methods:
    do_homework - request Homework object and returns it,
    if Homework is expired, prints 'You are late' and returns None
3. Teacher
Attributes:
     last_name
     first_name
Methods:
    create_homework - request task text and number of days to complete, returns Homework object
    Note that this method doesn't need object itself
PEP8 comply strictly.
"""
import datetime


class Teacher:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def create_homework(text, days):
        return Homework(text, days)


class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def do_homework(self, homework):
        if homework.is_active():
            return homework
        print("You are late")
        return None


class Homework:
    def __init__(self, text, days_to_complete):
        if days_to_complete >= 0:
            self.text = text
            self.days_to_complete = days_to_complete
            self.created = datetime.datetime.now()
            self.deadline = (self.created + datetime.timedelta(days=self.days_to_complete)) - self.created
        else:
            raise ValueError("Days to complete value can not be negative")

    def __repr__(self):
        return f"Homework '{self.text}' with {self.days_to_complete} days to complete the task"

    def is_active(self):
        # TODO should we check here if homework is still active?
        if self.deadline >= datetime.timedelta(seconds=1):
            return True
        return False


if __name__ == '__main__':
    teacher = Teacher('Dmitry', 'Orlyakov')
    student = Student('Vladislav', 'Popov')
    print(teacher.last_name)
    print(student.first_name)

    expired_homework = teacher.create_homework('Learn functions', 0)
    print(expired_homework.created)  # Example: 2019-05-26 16:44:30.688762
    print(expired_homework.deadline)  # 0:00:00
    print(expired_homework.text)  # 'Learn functions'
    print(expired_homework.is_active())

    # create function from method and use it
    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too('create 2 simple classes', 5)
    print(oop_homework.deadline)  # 5 days, 0:00:00
    print(oop_homework.is_active())

    print(student.do_homework(oop_homework))
    print(student.do_homework(expired_homework)) # You are late
