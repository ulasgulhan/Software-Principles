class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_pay(self):
        # Both salary calculation and database operations are combined here
        # This does not adhere to the Separation of Concerns principle
        pass

# Usage
employee = Employee("Ahmet", 5000)
print(f"{employee.name}'s salary: {employee.calculate_pay()}")
