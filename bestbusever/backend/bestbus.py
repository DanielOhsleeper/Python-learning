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

    def update_route_info(self, line_number, origin=False, destination=False, list_of_stops=False):
        if line_number not in self._routes:
            raise Exception("This line number does not exists")
        route_to_update = self._routes.get(line_number)
        if origin:
            route_to_update.set_origin(origin)
        elif destination:
            route_to_update.set_destination(destination)
        elif list_of_stops:
            route_to_update.set_stops(list_of_stops)

    def add_sched_to_route(self, line_number, origin_time, destination_time, driver_name):
        route_to_update = self._routes.get(line_number)
        if not route_to_update:
            raise Exception("No such line")
        return route_to_update.add_scheduled_ride(origin_time, destination_time, driver_name)

    def get_route_by_line(self, line_number):
        ret_val = self._routes.get(line_number)
        if ret_val:
            return ret_val
        raise Exception("No such line")

    def search(self, origin=False, destination=False, stop=False):
        for i in self._routes:
            for bus_route in [self._routes[i]]:
                if bus_route.search_by_origin_for_best_bus() == origin or bus_route.search_by_destination_for_best_bus()\
                        == destination:
                    return self._routes[i]
                if stop in bus_route.search_by_stops():
                    return self._routes[i]
                else:
                    raise Exception("No information about this, try again ")

    # def search_stop_station(self):
    #     for i in self._routes:
    #         for bus_route in [self._routes[i]]:
    #             if Menu.get_stop_station() in bus_route.search_by_stops():
    #                 return self._routes[i]

    def __repr__(self):
        return f"{self._routes}"
