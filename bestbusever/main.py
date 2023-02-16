from bestbusever.backend.bestbus import*
from bestbusever.backend.scheduled_ride import ScheduledRide
from bestbusever.frontend.menu import Menu

if __name__ == '__main__':
    role = Menu.main_menu()
    best_bus = BestBusCompany()

    while True:
        if role == 1:
            action = Menu.passenger_menu()
            match action:
                case 1:
                    print("Searching Route")
                case 2:
                    print("Reporting Delay")
                case 3:
                    print("Exiting")
                    break
        elif role == 2:
            action = Menu.manager_menu()
            match action:
                case 1:
                    print("Adding a new route")
                    line_number = Menu.get_line_number()
                    origin = Menu.get_origin()
                    destination = Menu.get_destination()
                    list_of_stops = Menu.get_list_stop()
                    try:
                        new_route = best_bus.start_route(line_number, origin, destination, list_of_stops)
                    except Exception as e:
                        print(e)
                    print(best_bus)
                case 2:
                    print("Deleting Route by Line number: ")
                    delete = Menu.delete_route()
                    ask = input("Are you sure? y/n ")
                    if "y" in ask:
                        new_route = best_bus.delete_ride(delete)
                        print(best_bus)
                    if "n" in ask:
                        continue
                case 3:
                    print("Updating Route")
                    line_to_update = Menu.line_to_update()
                    try:
                        update_val = Menu.update_route()
                        if "1" in update_val:
                            new_origin = Menu.get_origin()
                            new_route = best_bus.update_route_info(line_number, new_origin, destination, list_of_stops)
                        if "2" in update_val:
                            new_destination = Menu.get_destination()
                            new_route = best_bus.update_route_info(line_number, origin, new_destination, list_of_stops)
                        if "3" in update_val:
                            new_list_of_stops = Menu.get_list_stop()
                            new_route = best_bus.update_route_info(line_number, origin, destination, new_list_of_stops)
                        print(new_route)
                    except Exception as e:
                        print(e)
                case 4:

                    print(best_bus)
                    schedule = Menu.get_info()
                    if line_number != schedule:
                        print("no such line number")
                        continue
                    else:
                        driver = ScheduledRide.get_driver(ScheduledRide)
                        origin_time = ScheduledRide.get_origin_time(ScheduledRide)
                        dest = ScheduledRide.get_dest_time(ScheduledRide)
                        # new_route = best_bus.start_route(line_number, origin, destination, list_of_stops)
                        sc = ScheduledRide(origin_time,dest, driver)
                        print(sc)

                        print(new_route)

                case 5:
                    print("Exiting")
                    break




