class Site:
    def __init__(self):
        self._readings = []  # initialize an empty list of readings

    def last_reading(self):
        if not self._readings:
            return None  # return None if there are no readings
        return self._readings[-1]

    def add_reading(self, reading):
        self._readings.append(reading)

def main():
    the_site = Site()
    the_site.add_reading(10)
    the_site.add_reading(20)
    the_site.add_reading(30)
    last_reading = the_site.last_reading()
    print(f"Last reading: {last_reading}")

if __name__ == "__main__":
    main()
