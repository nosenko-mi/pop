import datetime
import json

from types import SimpleNamespace

from EmployeeRepositoryV1 import EmployeeRepositoryV1
from Employee import Employee
from constants import DEPARTMENT_KEY, POSITION_KEY, DATE_OF_BIRTH_KEY, YEAS_OF_SERVICE_KEY, DB_FILE

# data = ""
# with open(DB_FILE) as file:
#     data = file.read()

# x = json.loads(data)

# dummy_employees = [Employee(**i) for i in x]
# {"full_name":"Dannie Hamley","department":"Marketing","position":"VP Product Management","date_of_birth":"1998-07-25","years_of_service":8},
# {"full_name":"Sterne Segar","department":"Research and Development","position":"Assistant Media Planner","date_of_birth":"1995-09-23","years_of_service":19},
# {"full_name":"Lem Coule","department":"Services","position":"Account Executive","date_of_birth":"1999-07-08","years_of_service":10},
# {"full_name":"Rosemonde Shuttlewood","department":"Accounting","position":"Software Consultant","date_of_birth":"1997-10-13","years_of_service":20},
# {"full_name":"Moe Hayland","department":"Services","position":"Community Outreach Specialist","date_of_birth":"2001-02-03","years_of_service":18},
# {"full_name":"Gussy Gianullo","department":"Services","position":"Information Systems Manager","date_of_birth":"1998-07-28","years_of_service":2},

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

repository = EmployeeRepositoryV1(dummy_employees)

print(f"All employees:")
for e in repository.get_all_employees():
    print(f"\t {e}")

print(f"Get by name: <John Doe>\n\t{repository.get_employee_by_name("John Doe")}")

print(f"Get by department: <Services>")
for e in repository.get_employees_by_department("Services"):
    print(f"\t {e}")

print(f"Get by date of birth: <2000-2-20>")
for e in repository.get_employees_by_dob(datetime.date(2000, 2, 20)):
    print(f"\t {e}")

repository.add_employee(Employee("New Employee", {DEPARTMENT_KEY: "Marketing", POSITION_KEY: "VP Product Management",
                                         DATE_OF_BIRTH_KEY: datetime.date(1995, 2, 20), YEAS_OF_SERVICE_KEY: 0}))

print(f"Added employee:")
for e in repository.get_all_employees():
    print(f"\t {e}")

e = repository.get_employee_by_name("New Employee")
repository.remove_employee(e)
print(f"Removed employee:")
for e in repository.get_all_employees():
    print(f"\t {e}")


