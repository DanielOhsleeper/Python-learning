class BestBus:
    ride_list = []
    rides_dict = {}

    def __init__(self, line_num, origin, destination, list_of_stops):
        self.line_num = line_num
        self.origin = origin
        self.destination = destination
        self.list_of_stops = list_of_stops

    def __str__(self):
        return f"Line number: {self.line_num}\n" \
               f"Origin: {self.origin}\n" \
               f"Destination: {self.destination}"
