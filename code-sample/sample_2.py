# Base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}"

    def greet(self):
        return f"Hello, {self.name}!"


# Intermediate class 1
class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def get_employee_info(self):
        return f"{self.get_details()}, Employee ID: {self.employee_id}"

    def work(self):
        return f"{self.name} is working on company projects."


# Intermediate class 2
class Manager(Employee):
    def __init__(self, name, age, employee_id, department):
        super().__init__(name, age, employee_id)
        self.department = department

    def manage(self):
        return f"{self.name} is managing the {self.department} department."

    def get_manager_info(self):
        return f"{self.get_employee_info()}, Department: {self.department}"


# Another Intermediate class for interns
class Intern(Employee):
    def __init__(self, name, age, employee_id, duration):
        super().__init__(name, age, employee_id)
        self.duration = duration  # duration in months

    def get_intern_info(self):
        return f"{self.get_employee_info()}, Internship Duration: {self.duration} months"

    def work(self):
        return f"{self.name} is working on internship tasks for {self.duration} months."


# Derived class using multiple inheritance
class MultiRole(Manager, Intern):
    def __init__(self, name, age, employee_id, department, duration):
        Manager.__init__(self, name, age, employee_id, department)
        Intern.__init__(self, name, age, employee_id, duration)

    def get_multi_role_info(self):
        return f"{self.get_manager_info()}, Duration: {self.duration} months"


# Test the multi-inheritance structure
employee = MultiRole("Alice", 30, "E123", "Finance", 6)

# print(employee.get_details())  # From Person
# print(employee.get_employee_info())  # From Employee
# print(employee.get_manager_info())  # From Manager
# print(employee.get_intern_info())  # From Intern
# print(employee.get_multi_role_info())  # Combined
