# Static Methods = A method that belong to a class rather than any object from that class (instance)
#       Usually used for general utility functions

# Instance methods = Best for operations on instances fo the class (objects)
# Static methods = Best for utility functions that do not need access to class Data

class Employee:
    
    def __init__(self, name, job_position):
        self.name = name
        self.job_position = job_position
        
    def get_info(self):
        return f"{self.name} = {self.job_position}"
    
    
    @staticmethod
    def is_valid_position(position):
        valid_poisitions = ["Manager", "Cashier", "Cook", "Cleaner", "Sign-holder"]
        return position in valid_poisitions

employee1 = Employee("Jack", "Manager")
employee2 = Employee("Alex", "Cashier")
employee3 = Employee("John", "Cook")
    
print(Employee.is_valid_position("Cook"))
print(Employee.is_valid_position("Rocket Man"))

print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())