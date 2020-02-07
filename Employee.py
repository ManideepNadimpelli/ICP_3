class Employee:
    num_Employee = 0
    Tsalary = 0

    def __init__(self, n, f, s, d):
        self.name = n
        self.family = f
        self.salary = s
        self.department = d
        Employee.num_Employee += 1
        Employee.Tsalary += self.salary

    def avg_sal(self):
        a_sal = Employee.Tsalary / self.num_Employee
        print(self.num_Employee)
        print(a_sal)


class FullTimeEmployee(Employee):
    def __init__(self, n, f, s, d):
        super(FullTimeEmployee, self).__init__(n, f, s, d)


emp1 = FullTimeEmployee('mani', 'nadim', 1200, 'eng')
emp1.avg_sal()
emp2 = FullTimeEmployee('Bhavya', 'Sirasa', 2000, 'Cs')
emp2.avg_sal()
