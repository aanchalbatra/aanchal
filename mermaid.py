class Person:
    def __init__(self, name: str):
        self.name = name

class Employee(Person):  # Inheritance
    def __init__(self, name: str, employee_id: str):
        super().__init__(name)
        self.employee_id = employee_id
        self.projects = []

    def assign_project(self, project):
        self.projects.append(project)

class Project:
    def __init__(self, title: str):
        self.title = title
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

class Task:
    def __init__(self, description: str):
        self.description = description

class Company:
    def __init__(self, name: str):
        self.name = name
        self.employees = []

    def hire_employee(self, employee: Employee):  # Association
        self.employees.append(employee)
