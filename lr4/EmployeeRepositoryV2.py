import json
from Employee import Employee, EmployeeDb
from constants import DATE_OF_BIRTH_KEY, DB_FILE, DEPARTMENT_KEY, POSITION_KEY, YEAS_OF_SERVICE_KEY
import datetime

import sqlite3


class EmployeeRepositoryV2():

    def __init__(self) -> None:
        self.db = EmployeeDatabase(DB_FILE)

    def get_employees(self, offset: int, limit: int = 50) -> list[EmployeeDb]:
        return self.db.get_employees(offset, limit)

    def get_employee_by_name(self, full_name: str) -> EmployeeDb | None:
        return self.db.get_employee_by_name(full_name)

    def get_employees_by_department(self, department: str) -> list[EmployeeDb]:
        return self.db.get_employees_by_department(department)

    def get_employees_by_position(self, position: str) -> list[EmployeeDb]:
        return self.db.get_employees_by_position(position)

    def get_employees_by_dob(self, dob: datetime.date) -> list[EmployeeDb]:
        return self.db.get_employees_by_dob(dob.isoformat())

    def add_employee(self, employee: Employee) -> int:
        return self.db.insert_employee(employee)

    def remove_employee(self, employee_id: int) -> None:
        return self.db.remove_employee(employee_id)

    def __save_to_file__(self):
        with open(self.filepath, 'w', encoding='utf-8') as file:
            json.dump([e.to_dict() for e in self.employees],
                      file, ensure_ascii=False, indent=4)



class EmployeeDatabase():
    def __init__(self, path: str) -> None:
        self.path = path
        self.__connect__(path)

    def __connect__(self, path):
        self.connection = sqlite3.connect(path)
        try:
            cursor = self.connection.cursor()
            # Save date in TEXT as ISO8601 strings ("YYYY-MM-DD HH:MM:SS.SSS"). 
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS employees (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    full_name TEXT,
                    department TEXT,
                    position TEXT,
                    date_of_birth TEXT,
                    years_of_service INTEGER
                )
            """)
            self.connection.commit()
        finally:
            cursor.close()

    
    def get_employee_by_id(self, id: int) -> EmployeeDb | None:
        try:
            cursor = self.connection.cursor()
            res = cursor.execute(f"SELECT * FROM employees WHERE id = ?;", (id,))
            self.connection.commit()
            rows = res.fetchone()
            return rows
        except Exception as e:
            print(e)
            return None
        finally:
            cursor.close()


    def get_employees(self, offset: int, limit: int)-> list[EmployeeDb]:
        try:
            cursor = self.connection.cursor()
            res = cursor.execute(f"SELECT * FROM  employees LIMIT ? OFFSET ?;", (limit, offset,))
            self.connection.commit()
            rows = res.fetchall()
            return rows
        except Exception as e:
            print(e)
            return []
        finally:
            cursor.close()

    def get_employee_by_name(self, full_name: str) -> EmployeeDb | None:
        try:
            cursor = self.connection.cursor()
            res = cursor.execute(f"SELECT * FROM employees WHERE full_name = ?;", (full_name,))
            self.connection.commit()
            rows = res.fetchall()
            return rows
        except Exception as e:
            print(e)
        finally:
            cursor.close()

    def get_employees_by_department(self, department: str) -> list[EmployeeDb]:
        try:
            cursor = self.connection.cursor()
            res = cursor.execute(f"SELECT * FROM employees WHERE department LIKE ?;", (department,))
            self.connection.commit()
            rows = res.fetchall()
            return rows
        except Exception as e:
            print(e)
        finally:
            cursor.close()

    def get_employees_by_position(self, position: str) -> list[EmployeeDb]:
        try:
            cursor = self.connection.cursor()
            res = cursor.execute(f"SELECT * FROM employees WHERE position LIKE ?;", (position,))
            self.connection.commit()
            rows = res.fetchall()
            return rows            
        except Exception as e:
            print(e)
        finally:
            cursor.close()

    def get_employees_by_dob(self, dob: str) -> list[EmployeeDb]:
        try:
            cursor = self.connection.cursor()
            res = cursor.execute(f"SELECT * FROM employees WHERE date_of_birth LIKE ?;", (dob,))
            self.connection.commit()
            rows = res.fetchall()
            return rows 
        except Exception as e:
            print(e)
        finally:
            cursor.close()

    def remove_employee(self, employee_id: int) -> int:
        try:
            cursor = self.connection.cursor()
            res = cursor.execute(f"DELETE FROM employees WHERE id = ?;", (employee_id,))
            self.connection.commit()
            rows = res.fetchall()
            return employee_id 
        except Exception as e:
            print(e)
        finally:
            cursor.close()

    def insert_employee(self, employee: Employee):
        try:
            cursor = self.connection.cursor()
            res = cursor.execute(f"INSERT INTO employees (full_name, {DEPARTMENT_KEY}, {POSITION_KEY}, {DATE_OF_BIRTH_KEY}, {YEAS_OF_SERVICE_KEY}) VALUES (?, ?, ?, ?, ?);", (employee.full_name, employee.department, employee.position, employee.date_of_birth.isoformat(), employee.years_of_service,))
            self.connection.commit()
        except Exception as e:
            print(e)
        finally:
            cursor.close()


    def drop_table(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("DROP TABLE employees;")
            self.connection.commit()
        except Exception as e:
            print(e)
        finally:
            cursor.close()





    # def __load_from_file__(self,) -> list[Employee]:
    #     try:
    #         with open(self.filepath) as file:
    #             json_employees = json.load(file)
    #             self.employees = [Employee.from_dict(
    #                 data) for data in json_employees]
    #         return self.employees
    #     except FileNotFoundError:
    #         print(f"Could not find file: {self.filepath}")
    #         return []
        

    # def __drop_table__(self):
    #     self.db.drop_table()



