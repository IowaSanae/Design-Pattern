class Employee:
    def __init__(self, factor: float) -> None:
        self.factor = factor

    def salary_raise(self) -> float:
        salary = 1
        salary *= (1 + self.factor)
        return salary

def main() -> None:
    factor = 0.1
    employee = Employee(factor).salary_raise()
    print(f"Salary is raised to: {employee}")


if __name__ == "__main__":
    main()