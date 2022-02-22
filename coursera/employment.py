class Employee:
    def __init__(self, first, last, salary=0):
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self, new_salary=0):
        if new_salary == 0:
            new_salary += 5000
        self.salary += new_salary

