class Person:
    def __init__(self, _office_area_code: str, _office_number: str) -> None:
        self._office_area_code = _office_area_code
        self._office_number = _office_number

    def get_telephone_number(self) -> str:
        return self.get_office_telephone_number()

    def get_office_telephone_number(self) -> str:
        return (" (" + self._office_area_code + ") " + self._office_number)


def main():
    _office_area_code = "500"
    _office_number = "123456789"
    print(
        f"Get phone number: {Person(_office_area_code, _office_number).get_telephone_number()}")


if __name__ == "__main__":
    main()