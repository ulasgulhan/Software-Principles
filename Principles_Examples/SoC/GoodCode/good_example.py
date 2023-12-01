class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class PayrollSystem:
    def calculate_pay(self, employee):
        # Salary calculation logic
        return employee.salary

class EmployeeDatabase:
    def get_employee_info(self, employee_id):
        # Database operations to retrieve employee information
        # Only database operations are performed here, nothing else
        pass

# Usage
employee_db = EmployeeDatabase()
employee = employee_db.get_employee_info(1)

payroll_system = PayrollSystem()
print(f"{employee.name}'s salary: {payroll_system.calculate_pay(employee)}")