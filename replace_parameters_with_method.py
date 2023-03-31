class Price:
    def __init__(self, _quantity: int, _item_price: int) -> None:
        self._quantity = _quantity
        self._item_price = _item_price

    def get_price(self) -> float:
        return self.discounted_price()

    def discounted_price(self) -> float:
        if (self.get_discount_level() == 2):
            return self.get_base_price() * 0.1
        else:
            return self.get_base_price() * 0.05

    def get_discount_level(self) -> int:
        if (self._quantity > 100):
            return 2
        else:
            return 1

    def get_base_price(self) -> float:
        return self._quantity * self._item_price


def main():
    price = Price(100, 10).get_price()
    print(f"The price is: {price}")


if __name__ == "__main__":
    main()
