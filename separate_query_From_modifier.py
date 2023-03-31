class Customer:
    def __init__(self, people: list[str]) -> None:
        self.people = people

    def send_alert(self) -> None:
        print("Alert sent")

    def found_miscreant(self) -> None:
        for i in range(len(self.people)):
            if self.people[i] == "Don":
                self.send_alert()
                return
            if self.people[i] == "John":
                self.send_alert()
                return

        return self.found_person()

    def check_security(self) -> None:
        self.found_miscreant()
        found = self.found_person()
        if found:
            return found
        else:
            return None

    def found_person(self) -> str:
        for i in range(len(self.people)):
            if self.people[i] == "Don":
                return "Don"
            if self.people[i] == "John":
                return "John"

        return ""


def main():
    people = ["John", "Don", "Annie", "Bob"]
    security_check = Customer(people).check_security()
    print(f"Miscreant: {security_check}")


if __name__ == "__main__":
    main()
