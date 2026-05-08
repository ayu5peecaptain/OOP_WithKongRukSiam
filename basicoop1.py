class Employee:        
    #Default constructor
    def __init__(self, name="", salary=0, department=""):
        self.name = name
        self.salary = salary
        self.department = department

    def showData(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Department: {self.department}\n")

    #Destructor
    def __del__(self):
        print(f"Employee {self.name} is deleted.")
emp1 = Employee("Chawankorn Ramanee", 50000, "HR")
emp1.salary = 55000
emp1.showData()

emp2 = Employee("Kittakorn Kaewloy", 60000, "IT")
emp2.showData()

emp3 = Employee("Jirayut Srisopa", 55000, "Finance")
emp3.showData()