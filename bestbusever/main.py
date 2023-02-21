import pickle

from bestbusever.backend.scheduled_ride import ScheduledRide
from bestbusever.frontend.menu import Menu
from bestbusever.backend.bestbus import BestBusCompany
import os

if __name__ == '__main__':
    if not os.path.exists('best_bus.pickle'):
        best_bus = BestBusCompany()
    else:
        with open('best_bus.pickle', 'rb') as fh:
            best_bus = pickle.load(fh)
    role = Menu.main_menu()
    password = "r"
    flag = False
    while True:
        if role == 1:
            count = 0
            while not flag:
                count += 1
                password_access = Menu.pass_acc()
                if password_access == password:
                    flag = True
                elif count == 3:
                    print("You’ve tried to sign in too many times with an incorrect password, try again later")
                    exit(role)
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
                    line_number = Menu.get_line_number()
                    try:
                        update_val = Menu.update_route()
                        if "1" in update_val:
                            new_origin = Menu.get_origin()
                            best_bus.update_route_info(line_number, origin=new_origin)
                        if "2" in update_val:
                            new_destination = Menu.get_destination()
                            best_bus.update_route_info(line_number, destination=new_destination)
                        if "3" in update_val:
                            new_list_of_stops = Menu.get_list_stop()
                            best_bus.update_route_info(line_number, list_of_stops=new_list_of_stops)
                        print(best_bus.get_route_by_line(line_number))
                    except Exception as e:
                        print(e)
                case 4:
                    try:
                        line_number = Menu.get_line_number()
                        print(best_bus.get_line(line_number))
                        driver = Menu.get_driver()
                        origin_time = Menu.get_origin_time()
                        dest = Menu.get_dest_time()
                        print(best_bus)
                        print(best_bus.add_sched_to_route(line_number, origin_time, dest, driver))
                    except Exception as e:
                        print(e)
                case 5:
                    print("Exit to Main Menu")
                    role = Menu.main_menu()
        if role == 2:
            action = Menu.passenger_menu()
            match action:
                case 1:
                    srch = Menu.search_by()
                    try:
                        if "1" in srch:
                            origin_search = Menu.get_origin()
                            print(best_bus.search(origin_search))
                        elif "2" in srch:
                            dest_search = Menu.get_destination()
                            print(best_bus.search(dest_search))
                        elif "3" in srch:
                            stop = Menu.get_stop_station()
                            print(best_bus.search_by_stop(stop))
                        elif "4" in srch:
                            line_number = Menu.get_line_number()
                            print(best_bus.get_route_by_line(line_number))
                    except Exception as e:
                        print(e)
                case 2:
                    print("Reporting Delay")
                    line_number = Menu.get_line_number()
                    print(best_bus.show_scheduled_rides_by_line(line_number))
                    id_by_passenger = Menu.ride_id_to_delay()
                    best_bus.update_delay(int(line_number), int(id_by_passenger))
                    print("Done with update")
                    print(best_bus.show_scheduled_rides_by_line(line_number))
                case 3:
                    print("Exit to Main Menu")
                    role = Menu.main_menu()
        if role == 3:
            with open('best_bus.pickle', 'wb') as fh:
                pickle.dump(best_bus, fh)
            exit()

# TODO_list
# 2.exceptions
# 3.unittests
# 4.pickle +
# 5.delays
