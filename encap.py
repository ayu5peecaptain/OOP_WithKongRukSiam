#Access Modifier
class Employee:        
    #Default constructor
    def __init__(self, name="", salary=0, department=""):
        self.name = name
        self.__salary = salary
        self.__department = department
        self.__showData()

    # Public method to display employee data
    def __showData(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.__salary}")
        print(f"Department: {self.__department}\n")
        
obj1 = Employee("Chawankorn Ramanee", 50000, "HR")
obj1.__salary = 100000 # This will not change the salary because it's a private variable
