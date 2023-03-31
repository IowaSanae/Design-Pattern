from collections import namedtuple


class IllegalArgumentException(Exception):
    def __init__(self, message="Incorrect type code value"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message


class Employee:
    global ENGINEER
    ENGINEER = 0
    global SALESMAN
    SALESMAN = 1
    global MANAGER
    MANAGER = 2

    employee_datatype = namedtuple("Employee", "type")

    def __init__(self, type: int) -> employee_datatype:
        self.type = type

    def create(self, type: int):
        if type == ENGINEER:
            return self.create_engineer()
        if type == SALESMAN:
            return self.create_salesman()
        if type == MANAGER:
            return self.create_manager()
        raise IllegalArgumentException

    def create_engineer(self) -> employee_datatype:
        return self.Engineer()

    def Engineer(self) -> employee_datatype:
        print("I'm an engineer")

    def create_salesman(self) -> employee_datatype:
        return self.Salesman()

    def Salesman(self) -> employee_datatype:
        print("I'm a salesman")

    def create_manager(self) -> employee_datatype:
        return self.Manager()

    def Manager(self) -> employee_datatype:
        print("I'm a manager")


def main():
    employee_kent = Employee(0).create(0)
    print(f"Employee is: {employee_kent}")


if __name__ == "__main__":
    main()
