import random


class ScheduledRide:
    def __init__(self, origin_time, destination_time, driver_name):
        self._origin_time = origin_time
        self._destination_time = destination_time
        self._driver_name = driver_name
        self._id = random.randint(1, 1000)
        self._delays = 0


    def add_scheduled_ride(self, origin_time, destination_time, driver_name):
        scheduled = ScheduledRide(origin_time, destination_time, driver_name)
        return scheduled

    def __str__(self):
        return f"ID: {self._id}\n" \
               f"Driver Name: {self._driver_name}\n" \
               f"Origin Time: {self._origin_time}\n" \
               f"Destination Time: {self._destination_time}"