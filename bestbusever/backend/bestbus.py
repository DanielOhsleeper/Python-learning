from bestbusever.backend.bus_route import BusRoute

class BestBusCompany:

    def __init__(self):
        self._routes: dict[int, BusRoute] = {}

    def start_route(self, line_number, origin, destination, list_of_stops):
        new_route = BusRoute(line_number, origin, destination, list_of_stops)
        if line_number not in self._routes:
            self._routes[line_number] = new_route
        return self._routes

    def delete_ride(self, delete):
        if delete in self._routes:
            del self._routes[delete]


    # def update_route_info(self, line_to_update, origin, destination, list_of_stops):
    #     if line_to_update not in self._routes:
    #         raise Exception("This line number does not exists")
    #     self._routes[line_to_update] = BusRoute(line_to_update, origin, destination, list_of_stops)
    #     return self._routes

    def updateline(self, line_number, origin, destination, list_of_stops):
        line_to_update = self._routes.get(line_number)
        self._routes[line_to_update] = BusRoute(line_number, origin, destination, list_of_stops)
        return self

    def add_sched_to_route(self, line_number, origin_time, destination_time, driver_name):
        route_to_update = self._routes.get(line_number)
        if not route_to_update:
            raise Exception("No such line")
        return route_to_update.add_scheduled_ride(origin_time, destination_time, driver_name)

    def search_by_line(self, line_number):
        if line_number in self._routes:
            return self._routes
        else:
            print("Hi")

    def __repr__(self):
        return f"{self._routes}"


