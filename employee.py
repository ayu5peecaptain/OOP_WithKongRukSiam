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