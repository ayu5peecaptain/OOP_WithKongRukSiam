#Access Modifier
class Employee:        
    #Default constructor
    def __init__(self, name="", salary=0, department=""):
        self.__name = name
        self.__salary = salary
        self.__department = department

    # Public method to display employee data
    def _showData(self):
        print(f"Name: {self.getName()}")
        print(f"Salary: {self.getSalary()}")
        print(f"Department: {self.getDepartment()}\n")

    def setName(self, newname):
        self.__name = newname

    def setSalary(self, newsalary):
        self.__salary = newsalary

    def setDepartment(self, newdepartment):
        self.__department = newdepartment
    
    #getter method
    def getName(self):
        return self.__name
    def getSalary(self):
        return self.__salary
    def getDepartment(self):
        return self.__department

obj1 = Employee("Chawankorn Ramanee", 50000, "HR")
obj1.setName("Joe Doe")
obj1.setSalary(100000)
obj1.setDepartment("IT")
obj1._showData()    