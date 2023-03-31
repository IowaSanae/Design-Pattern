class Account:
    def __init__(self, balance: int) -> None:
        self.balance = balance

    def withdraw(self, amount: int) -> int:
        if amount > self.balance:
            raise BalanceException()
        self.balance -= amount
        return amount


class Assert:
    def __init__(self, comment: str, test: bool) -> None:
        self.comment = comment
        self.test = test

    @staticmethod
    def is_true(message: str, test: bool) -> None:
        if not test:
            raise ValueError("Assertion failed " + message)


class BalanceException(Exception):
    pass


def main():
    account = Account(1000)
    amount = 200
    try:
        withdrawn = account.withdraw(amount)
        print(f"Withdrew {withdrawn} successfully")
    except BalanceException as e:
        print(e)


if __name__ == "__main__":
    main()
