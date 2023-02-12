from bestbusever.backend.bus_route import BusRoute


class BestBusCompany:
    def __init__(self):
        self._routes: dict[int, BusRoute] = {}

    def add_bus_route(self, line_number, origin, destination, list_of_stops):
        if self._routes.get(line_number):
            raise Exception("This line number already exists")
        new_route = BusRoute(line_number, origin, destination, list_of_stops)
        self._routes[line_number] = new_route

    def __str__(self):
        return "Best Bus Company"

