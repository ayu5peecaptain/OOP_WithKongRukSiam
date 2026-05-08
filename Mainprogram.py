class Employee:        
    #class variable
    minSalary = 12000
    maxSalary = 50000
    companyName = "UNTITLED Company"

    #Default constructor
    def __init__(self, name="", salary=0, department=""):
        self._name = name
        self._salary = salary
        self._department = department

    def _showData(self):
        print(f"Name: {self._name}")
        print(f"Salary: {self._salary}")
        print(f"Department: {self._department}\n")
    
    def _getIncome(self):
        return self._salary * 12 #Assuming salary is monthly, calculating annual income

    def __str__(self):
        return f"Name: {self._name}, Salary: {self._salary}, Department: {self._department})"
class Accounting(Employee):
    __departmentName = "Accounting"
    def __init__(self, name, salary, age):
        super().__init__(name, salary, self.__departmentName)
        self.age = age

    def _showData(self):
        print(f"Name: {self._name}")
        print(f"Salary: {self._salary}")
        print(f"Department: {self._department}\n")
        print(f"Age: {self.age}\n")
    
    def __str__(self):
        return(super().__str__() + f", Age: {self.age}") #overriding the __str__ method to include age information
        
class Programmer(Employee):
    __departmentName = "Software Development"
    def __init__(self, name, salary, experience, skill):
        super().__init__(name, salary, self.__departmentName)
        self.experience = experience
        self.skill = skill
    def _showData(self):
        print(f"Name: {self._name}")
        print(f"Salary: {self._salary}")
        print(f"Department: {self._department}\n")
        print(f"Experience: {self.experience} years")
        print(f"Skill: {self.skill}\n")

    
    def _getIncome(self, ot):
        return super()._getIncome()+(ot*500) #Calculating annual income including overtime pay, assuming 500 per hour of overtime
    def __str__(self):
        return super().__str__() + f", Experience: {self.experience} years, Skill: {self.skill}" #overriding the __str__ method to include experience and skill information
        

class Sale(Employee): 
    __departmentName = "Sales"
    def __init__(self, name, salary, area):
        super().__init__(name, salary, self.__departmentName)
        self.area = area
    def _showData(self):
        print(f"Name: {self._name}")
        print(f"Salary: {self._salary}")
        print(f"Department: {self._department}\n")
        print(f"Area: {self.area}\n")
    def __str__(self):
        return super().__str__() + f", Area: {self.area}" #overriding the __str__ method to include area information

#Creating objects of the derived classes
account = Accounting("John", 25000, 30)
# print(account.__str__())
print(account._getIncome())
programmer = Programmer("Alice", 30000, 5, "Python")
# programmer._showData()

print(programmer._getIncome(1)) #Calculating income with 10 hours of overtime
sale = Sale("Bob", 20000, "Hatyai, Songkhla")
# sale._showData()
print(sale.__str__())
