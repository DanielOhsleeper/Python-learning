from bestbusever.backend.scheduled_ride import ScheduledRide


class BusRoute:
    def __init__(self, line_number: int, origin: str, destination: str, list_of_stops: list[str]):
        self._line_number = line_number
        self._origin = origin
        self._destination = destination
        self._list_of_stops = list_of_stops
        self._scheduled_rides = []


    def __repr__(self):
        return f"Line number: {self._line_number}\n"\
               f"Origin: {self._origin}\n" \
               f"Destination: {self._destination}\n" \
               f"List of stops: {self._list_of_stops}\n" \
               f"Rides: {self._scheduled_rides}"




