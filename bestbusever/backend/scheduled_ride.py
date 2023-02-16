import random

from bestbusever.frontend.menu import Menu


class ScheduledRide:
    def __init__(self, origin_time, destination_time, driver_name):
        self._origin_time = origin_time
        self._destination_time = destination_time
        self._driver_name = driver_name
        self._id = random.randint(1, 1000)
        self._delays = 0


    # def add_scheduled_ride(self, origin_time, destination_time, driver_name):
    #     self._driver_name = input("What is the drivers name")
    #     scheduled = ScheduledRide(origin_time, destination_time, driver_name)
    #     return scheduled


    def get_origin_time(self):
        self._origin_time = input("Origin Time? ")
        return self._origin_time

    def get_driver(self):
        self._driver_name = input("Driver's Name? ")
        return self._driver_name

    def get_dest_time(self):
        self._destination_time = input("Destination Time? ")
        return self._destination_time


    # @staticmethod
    # def schedule_ride():
    #     driver = Menu.driver_name()
    #     origin_time = Menu.orig_time()
    #     dest = Menu.dest_time()
    #     sc = ScheduledRide(driver, origin_time, dest)
    #     return sc

    def __str__(self):
        return f"Driver's Name: {self._driver_name}\n" \
               f"Id: {self._id}\n" \
               f"Origin Time: {self._origin_time}\n" \
               f"Destination Time: {self._destination_time}\n"








