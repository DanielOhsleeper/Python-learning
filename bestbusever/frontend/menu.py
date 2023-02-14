class Menu:
    @staticmethod
    def main_menu():
        user_role = input("Hello. Please choose your role:\n1. Passenger\n2. Manager\nYour choice (1 or 2): ")
        return int(user_role)

    @staticmethod
    def passenger_menu():
        passenger_action = input("Please choose your action:\n1. Search Route\n2. Report Delay\nYour choice (1 or 2): ")
        return int(passenger_action)

    @staticmethod
    def manager_menu():
        manager_action = input("Please enter your action:\n1. Add Route\n2. Delete Route...")
        return int(manager_action)

    @staticmethod
    def get_line_number():
        return int(input("Please enter the line number: ").strip())


    @staticmethod
    def get_origin():
        return str(input("Please enter origin: "))

    @staticmethod
    def get_list_stop():
        return input("Please insert stop stations separated by comma's: ")

    @staticmethod
    def get_destination():
        return str(input("Please insert destination stop: "))



