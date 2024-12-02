class Employee:
    def __init__(self, emp_id, name, position, basic_salary, hours_worked, hourly_rate):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.basic_salary = basic_salary
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def display_details(self):
        print(f"ID: {self.emp_id}\nName: {self.name}\nPosition: {self.position}\n" +
              f"Basic Salary: {self.basic_salary}\nHours Worked: {self.hours_worked}\nHourly Rate: {self.hourly_rate}")

    def update_details(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def calculate_salary(self):
        return self.basic_salary + (self.hourly_rate * self.hours_worked)

    def generate_payslip(self):
        salary = self.calculate_salary()
        payslip = (f"Payslip for {self.name}\n"
                   f"Position: {self.position}\n"
                   f"Basic Salary: {self.basic_salary}\n"
                   f"Hours Worked: {self.hours_worked}\n"
                   f"Hourly Rate: {self.hourly_rate}\n"
                   f"Total Salary: {salary}")
        print(payslip)
        return payslip
