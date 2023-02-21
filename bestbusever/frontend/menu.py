import datetime


class Menu:


    @staticmethod
    def main_menu():
        try:
            user_role = int(input("Hello. Please choose your role:\n1. Manager\n2. Passenger\n 3. Exit\n Your choice (1,"
                              "2 or 3): "))
            return int(user_role)
        except Exception:
            print("Invalid input")





    @staticmethod
    def passenger_menu():
        passenger_action = input("Please choose your action:\n1. Search Route\n2. Report Delay\n3. Back to Main Menu: "
                                 "\n "
                                 "Your Choice: ")
        return int(passenger_action)

    @staticmethod
    def manager_menu():
            manager_action = input("Please enter your action:\n1. Add Route\n2. Delete Route\n"
                                   "3. Update Route\n4. Add Scheduled Ride\n5. Back to Main Menu \n"
                                   "Your Choice: ")
            return int(manager_action)


    @staticmethod
    def get_line_number():
        return int(input("Please enter the line number: ").strip())

    @staticmethod
    def get_origin():
        return str(input("Please enter origin: "))

    @staticmethod
    def get_list_stop():
        stop_list = input("Please insert stop stations separated by comma's: ")
        return stop_list.strip()

    @staticmethod
    def get_destination():
        return str(input("Please insert destination stop: "))

    @staticmethod
    def delete_route():
        return int(input("What route do you want to delete? "))

    @staticmethod
    def update_route():
        return input("What do you want to update in this line?\n"
                     "1. Origin \n"
                     "2. Destination \n"
                     "3. List of Stops ")

    @staticmethod
    def get_info():
        return int(input("What line number would you like to update with a new ride? "))

    @staticmethod
    def get_origin_time():
        o_t = input("Insert origin time in format 'hh-mm':  ")
        try:
            converted_orig = datetime.datetime.strptime(o_t, "%H-%M")
            return converted_orig.time()
        except Exception:
            print("Wrong date format")


    @staticmethod
    def get_driver():
        return input("Please insert Driver's name: ")

    @staticmethod
    def get_dest_time():
        d_t = input("Insert destination time in format 'hh-mm':  ")
        try:
            converted_dest = datetime.datetime.strptime(d_t, "%H-%M")
            return converted_dest.time()
        except Exception:
            print("Wrong time format")


    @staticmethod
    def search_by():
        return input("By what do you wanna search?\n"
                     "1.Origin \n"
                     "2.Destination \n"
                     "3.Stop \n"
                     "4.Line number \n"
                     "")

    @staticmethod
    def get_stop_station():
        return input("Insert stop station: ")

    @staticmethod
    def pass_acc():
        return input("Please Insert your password: ")

    @staticmethod
    def ride_id_to_delay():
        return int(input("Please Enter ID, that you want to report about: "))