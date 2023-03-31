class Employee:
    ENGINEER = 0
    SALESMAN = 1
    MANAGER = 2

    def __init__(self, name: str):
        self.name = name

    @staticmethod
    def create_name(name: str):
        try:
            employee_class = globals()[name]
            return employee_class(name)
        except KeyError:
            raise ValueError(f"Unable to instantiate {name}")


    @staticmethod
    def create_int(type: int):
        if type == Employee.ENGINEER:
            return Engineer()
        elif type == Employee.SALESMAN:
            return Salesman()
        elif type == Employee.MANAGER:
            return Manager()
        else:
            raise ValueError("Incorrect type code value")


class Engineer(Employee):
    def __init__(self, name: str):
        super().__init__(name)


class Salesman(Employee):
    def __init__(self, name: str):
        super().__init__(name)


class Manager(Employee):
    def __init__(self, name: str):
        super().__init__(name)


def main():
    employee_kent = Employee.create_name("Engineer")
    print(f"Employee is: {employee_kent.name}")


if __name__ == "__main__":
    main()
