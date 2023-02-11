from bestbus import BestBus

class Manager:

    @staticmethod
    def add_info_for_line():
        line_number = int(input("Insert line num: "))
        if line_number not in BestBus.rides_dict:
            BestBus.rides_dict["line number"] = line_number
        origin = input("insert origin:")
        BestBus.rides_dict["origin"] = origin
        destination = input("insert destination: ")
        BestBus.rides_dict["destination"] = destination
        list_of_stops = input("insert list or stops:")
        list_of_stops_split = list_of_stops.split(",")
        BestBus.rides_dict["list of stops"] = list_of_stops_split
        BestBus.ride_list = [BestBus.rides_dict]

    @staticmethod
    def delete_route():
        if True:
            return BestBus.ride_list.pop()

