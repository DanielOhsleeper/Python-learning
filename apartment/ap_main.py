class Apartment:
    def __init__(
            self, address: dict,
                 apartment: dict,
                 rooms_data: dict,
                 bathroom_data: dict,
                 kitchen_size: dict,
                 balconies_data: bool
    ):
        self.address = address,
        self.apartment = apartment,
        self.rooms_data = rooms_data,
        self.bathroom_data = bathroom_data,
        self.kitchen_size = kitchen_size,
        self.balconies_data = bool,
        self.get_total_living_space_size()


    def get_rooms_number(self):
        return rooms_data["Amount of rooms"]

    def is_last_floor(self):
        if apartment["Apartment floor"] != apartment["Total floors"]:
            return False
        return True


    def get_total_living_space_size(self):
        living = 0
        for room, sizes in rooms_data.items():
            living += sizes
        return living - rooms_data["Amount of rooms"]

    def get_total_apartment_size(self):
        return self.get_total_living_space_size()+ kitchen_size["Kitchen Size"] + bathroom_data["Size"]

    def get_total_area_of_balconies(self, is_balcony: bool):
        if is_balcony:
            return balconies_data
        return f"No balcony exist"

    def get_annual_arnona(self, is_balcony: bool):

        base_arnona_tarif = 38 / 12
        return ((self.get_total_apartment_size() * base_arnona_tarif)\
               + (base_arnona_tarif * 0.75 * self.get_total_area_of_balconies(is_balcony))) * 12


    def __str__(self):
        return f"Address:{address}\nApartment sqr:{self.get_total_apartment_size()}" \
               f"\nAnnual arnona:{self.get_annual_arnona(is_balcony=bool)}"

if __name__ == '__main__':
        address = {
            "Country": "Israel",
            "City": "Rishpon le Tsyon",
            "Street": "Spinoza",
            "House num": "30",
            "Flat num": "19"
        }
        apartment = {
            "Apartment floor": 3,
            "Total floors": 8
        }

        rooms_data = {
            "Amount of rooms": 4,
            "1st room": 15,
            "2nd room": 20,
            "3rd room": 25,
            "4th room": 20
        }

        bathroom_data = {
            "Amount of bathroom": 1,
            "Size": 10,
            "Includes": "toilet, sink, bath"
        }

        kitchen_size = {
            "Kitchen Size": 13
        }

        balconies_data = 10
        ap = Apartment(address, apartment, rooms_data, bathroom_data, kitchen_size, balconies_data=bool)

        print(ap.get_rooms_number())
        print(ap.is_last_floor())
        print(ap.get_total_apartment_size())
        print(ap.get_total_living_space_size())
        print(ap.get_total_area_of_balconies(True))
        print(ap.get_annual_arnona(True))
        print(ap)






