from employee import Employee
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