#  1-to-Many Relationship: Department and Employees
# Scenario: A department can have multiple employees, but each employee belongs to one department.
# Create Department and Employee classes.
# Implement methods in Department to add and remove employees.
# Include attributes such as name and id for Employee and department_name for Department.
# Task: Write a function to list all employees in a department and one to transfer an employee to another department.

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id


class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []

    # Add an employee to the department
    def add_employee(self, employee):
        self.employees.append(employee)
    
    # Remove an employee from the department
    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)
        else:
            print(f"Employee {employee.name} not found in {self.department_name} department.")

    # List all employees in the department
    def list_employees(self):
        print(f"Employees in the {self.department_name} department:")
        for emp in self.employees:
            print(f"Name: {emp.name}, ID: {emp.id}")

    # Transfer an employee to another department
    def transfer_employee(self, employee, new_department):
        # Remove the employee from the current department
        self.remove_employee(employee)
        # Add the employee to the new department
        new_department.add_employee(employee)
        print(f"Employee {employee.name} transferred from {self.department_name} to {new_department.department_name}.")


# Example Usage:
# Create departments
dev_department = Department("Development")
hr_department = Department("Human Resources")

# Create employees
emp1 = Employee("John Doe", 101)
emp2 = Employee("Jane Smith", 102)
emp3 = Employee("Alice Brown", 103)

# Add employees to Development department
dev_department.add_employee(emp1)
dev_department.add_employee(emp2)

# List employees in Development department
dev_department.list_employees()

# Transfer an employee to Human Resources department
dev_department.transfer_employee(emp1, hr_department)

# List employees in both departments after transfer
dev_department.list_employees()
hr_department.list_employees()
