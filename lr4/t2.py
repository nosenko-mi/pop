import datetime
import json

from EmployeeRepositoryV2 import EmployeeRepositoryV2
from Employee import Employee
from constants import DEPARTMENT_KEY, POSITION_KEY, DATE_OF_BIRTH_KEY, YEAS_OF_SERVICE_KEY, DB_FILE


# e = Employee("New Employee", {DEPARTMENT_KEY: "Marketing", POSITION_KEY: "VP Product Management",
#                                          DATE_OF_BIRTH_KEY: datetime.date(1995, 2, 20), YEAS_OF_SERVICE_KEY: 0})
# a = e.to_json()
# a2 = Employee.from_json(a)
# print(a2)


dummy_employees = [
    Employee("John Doe", {DEPARTMENT_KEY: "Marketing", POSITION_KEY: "VP Product Management",
             DATE_OF_BIRTH_KEY: datetime.date(1995, 2, 20), YEAS_OF_SERVICE_KEY: 7}),
    Employee("Sterne Segar", {DEPARTMENT_KEY: "Research", POSITION_KEY: "Assistant",
             DATE_OF_BIRTH_KEY: datetime.date(2000, 2, 20), YEAS_OF_SERVICE_KEY: 1}),
    Employee("Lem Coule", {DEPARTMENT_KEY: "Accounting", POSITION_KEY: "Consultant",
             DATE_OF_BIRTH_KEY: datetime.date(1999, 2, 20), YEAS_OF_SERVICE_KEY: 3}),
    Employee("Moe Hayland", {DEPARTMENT_KEY: "Services", POSITION_KEY: "PM",
             DATE_OF_BIRTH_KEY: datetime.date(1999, 2, 20), YEAS_OF_SERVICE_KEY: 3}),
    Employee("Gussy Gianullo", {DEPARTMENT_KEY: "Services", POSITION_KEY: "IS Manager",
             DATE_OF_BIRTH_KEY: datetime.date(2000, 2, 20), YEAS_OF_SERVICE_KEY: 1}),
]


repository = EmployeeRepositoryV2()

print("Add employees")
for e in dummy_employees:
    repository.add_employee(e)

print("Get employees with limit")
print(repository.get_employees(offset=0, limit=2))

print(f"Get by name: <John Doe>")
print(f"\t{repository.get_employee_by_name("John Doe")}")

print(f"Get by department: <Services>")
print(f"\t{repository.get_employees_by_department("Services")}")

print(f"Get by date of birth: <2000-2-20>")
print(f"\t{repository.get_employees_by_dob(datetime.date(2000, 2, 20))}")

repository.add_employee(Employee("New Employee", {DEPARTMENT_KEY: "Marketing", POSITION_KEY: "VP Product Management",
                                         DATE_OF_BIRTH_KEY: datetime.date(1995, 2, 20), YEAS_OF_SERVICE_KEY: 0}))


print(f"Get by name: <New Employee>")
employees = repository.get_employee_by_name("New Employee")
print(employees)
print(f"Removed employee id:")
for e in employees:
    # print(e[0])
    print(repository.remove_employee(e[0]))

repository.__drop_table__()

