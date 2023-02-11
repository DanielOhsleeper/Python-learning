from manager import Manager
from bestbus import BestBus


class Menu:
    passenger = {1: "Search route", 2: "Report Delay"}
    manager = {1: "Add route", 2: "Delete route", 3: "Update route", 4: "Add scheduled ride"}

    @staticmethod
    def role_and_action():
        role_choice = input("passenger or manager")
        if "1" in role_choice:
            print("Hello Passenger, What is your choice: ")
            action = int(input(Menu.passenger))
            print(Menu.passenger[action])
        if "2" in role_choice:
            print("Hello Manager, What do you want to do? ")
            action = int(input(Menu.manager))
            print(Menu.manager[action])
            if action == 1:
                Manager.add_info_for_line()
            if action == 2:
                Manager.delete_route()







    # def delete_info():


# print(BestBus.rides_dict)
# print(BestBus.ride_list)
while True:
    Menu.role_and_action()
    print(BestBus.ride_list)

