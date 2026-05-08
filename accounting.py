from employee import Employee
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
        