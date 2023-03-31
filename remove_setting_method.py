class Account:
    def __init__(self, id) -> None:
        self._id = None
        self.initialize_id(id)

    def initialize_id(self, arg) -> None:
        self._id = "ZZ" + arg


class InterestAccount(Account):
    def __init__(self, id, rate):
        super().__init__(id)
        self._interest_rate = rate


class Person:
    def __init__(self):
        self._courses = []

    def get_courses(self):
        return self._courses

    def set_courses(self, arg):
        self._courses = arg


def main():
    account = Account("123")
    print(f"Account id: {account._id}")
    interest_account = InterestAccount("123", 10)
    print(f"Interest account id: {interest_account._id}")
    person = Person()
    person.set_courses(["Math", "English"])
    print(f"Person courses: {person.get_courses()}")


if __name__ == "__main__":
    main()