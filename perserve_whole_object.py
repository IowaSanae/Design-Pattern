from collections import namedtuple

HeatingPlan = namedtuple("HeatingPlan", "low high")
TempRange = namedtuple("TempRange", "low high")


class Room:
    def __init__(self, plan: HeatingPlan, days_temp_range) -> None:
        self.plan = plan
        self.days_temp_range = days_temp_range

    def within_plan(self, plan: HeatingPlan) -> bool:
        within_plan = plan.within_range(self.days_temp_range)
        return within_plan


class HeatingPlan:
    def __init__(self, _range: TempRange, high: int) -> None:
        self._range = _range
        self.high = high

    def within_range(self, room_range: TempRange) -> bool:
        return self._range.includes(room_range)


class TempRange:
    def __init__(self, low: int, high: int) -> None:
        self.low = low
        self.high = high

    def includes(self, range_: TempRange) -> bool:
        return self.low <= range_.low and range_.high <= self.high


class Room:
    def __init__(self, plan: HeatingPlan, days_temp_range: TempRange) -> None:
        self.plan = plan
        self.days_temp_range = days_temp_range

    def within_plan(self, plan: HeatingPlan) -> bool:
        within_plan = plan.within_range(self.days_temp_range)
        return within_plan


def main():
    temp_range = TempRange(1, 2)
    plan = HeatingPlan(temp_range, 2)
    room = Room(plan, temp_range)
    print(room.within_plan(plan))


if __name__ == "__main__":
    main()
