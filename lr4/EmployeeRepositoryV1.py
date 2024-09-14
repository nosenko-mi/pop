from Employee import Employee
import datetime


class EmployeeRepositoryV1():

    def __init__(self, employees: list[Employee]) -> None:
        self.employees: list[Employee] = employees


    def get_all_employees(self) -> list[Employee]:
        return self.employees


    def get_employee_by_name(self, full_name: str) -> Employee|None:
        for e in self.employees:
            if e.full_name == full_name:
                return e
            
        return None


    def get_employees_by_department(self, department: str) -> list[Employee]:
        employees = []
        for e in self.employees:
            if e.department == department:
                employees.append(e)
            
        return employees


    def get_employees_by_position(self, position: str) -> list[Employee]:
        employees = []
        for e in self.employees:
            if e.position == position:
                employees.append(e)
            
        return employees


    def get_employees_by_dob(self, dob: datetime.date) -> list[Employee]:
        employees = []
        for e in self.employees:
            if e.date_of_birth == dob:
                employees.append(e)
            
        return employees


    def add_employee(self, employee: Employee) -> None:
        self.employees.append(employee)

    def remove_employee(self, employee: Employee) -> None:
        self.employees.remove(employee)