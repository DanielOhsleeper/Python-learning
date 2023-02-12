import random


class ScheduledRide:
    def __init__(self, origin_time, destination_time, driver_name):
        self._origin_time = origin_time
        self._destination_time = destination_time
        self._driver_name = driver_name
        self._id = random.randint(1, 1000)
        self._delays = 0

