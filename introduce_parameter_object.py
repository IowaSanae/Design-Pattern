from typing import List
from datetime import date
from collections import namedtuple

DateRange = namedtuple("DateRange", "start end")

class Account:
    def __init__(self):
        self._entries = []

    def get_flow_between(self, range: DateRange) -> float:
        result = 0.0
        for each in self._entries:
            if (range.includes(each.get_date())):
                result += each.get_value()
        return result


class Entry:
    def __init__(self, date: date, value: float):
        self.date = date
        self.value = value

    def get_date(self) -> date:
        return self.date

    def get_value(self) -> float:
        return self.value


class DateRange:
    def __init__(self, start: date, end: date):
        self._start = start
        self._end = end

    def get_start(self) -> date:
        return self._start

    def get_end(self) -> date:
        return self._end

    def includes(self, arg: date) -> bool:
        return self._start == arg or self._end == arg or (arg > self._start and arg < self._end)


def main():
    start = date(2020, 1, 1)
    end = date(2020, 1, 31)
    _range = DateRange(start, end)
    account = Account()
    entry = Entry(date(2020, 1, 1), 1.0)
    account._entries.append(entry)
    print(f"Flow between {start} and {end} is {account.get_flow_between(_range)}")


if __name__ == "__main__":
    main()