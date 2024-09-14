import datetime

from constants import DEPARTMENT_KEY, POSITION_KEY, DATE_OF_BIRTH_KEY, YEAS_OF_SERVICE_KEY


class Employee():

    def __init__(self, full_name: str, details: dict[str, str, datetime.date, int]) -> None:
        self.full_name = full_name
        self.department = details[DEPARTMENT_KEY]
        self.position = details[POSITION_KEY]
        self.date_of_birth: datetime.date = details[DATE_OF_BIRTH_KEY]
        self.years_of_service = details[YEAS_OF_SERVICE_KEY]

    def __str__(self) -> str:
        return f"{self.full_name}: {self.department}-{self.position}. dob: {self.date_of_birth}, yos: {self.years_of_service}"

    def to_json(self) -> dict:
        return {
            "full_name": self.full_name,
            "details": {
                DEPARTMENT_KEY: self.department,
                POSITION_KEY: self.position,
                DATE_OF_BIRTH_KEY: self.date_of_birth,
                YEAS_OF_SERVICE_KEY: self.years_of_service
            }
        }

    @staticmethod
    def from_json(obj):
        return Employee(full_name=obj['full_name'], details=obj['details'])


class EmployeeDb(Employee):

    def __init__(self, id: int, full_name: str, department: str, position: str, date_of_birth: datetime.date, years_of_service: int):
        super().init(full_name=full_name, details={
            DEPARTMENT_KEY: department,
            POSITION_KEY: position,
            DATE_OF_BIRTH_KEY: date_of_birth,
            YEAS_OF_SERVICE_KEY: years_of_service
        })
        self.id = id