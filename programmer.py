from employee import Employee
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