from bestbusever.backend import bestbus
from bestbusever.backend.bestbus import*
from bestbusever.frontend.menu import Menu

if __name__ == '__main__':
    role = Menu.main_menu()
    best_bus = BestBusCompany()
    if role == 1:
        action = Menu.passenger_menu()
        match action:
            case 1:
                print("I am in search route action")
            case 2:
                pass
    elif role == 2:
        action = Menu.manager_menu()
        match action:
            case 1:
                print("Adding a new route")
                line_number = Menu.get_line_number()
                origin = Menu.get_origin() # Implement this function in Menu
                destination = Menu.get_destination() # Implement this function in Menu
                list_of_stops = Menu.get_list_stop() # Implement this function in Menu
                print(best_bus)
                print(list_of_stops)
                try:
                    best_bus.add_bus_route(line_number, origin, destination, list_of_stops) # Implement this function in Menu
                    # break
                except Exception as e:
                    print(e)
            case 2:
                pass

