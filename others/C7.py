class Apartment:
    def __init__(
            self,
            address,
            size_in_sq_meters,
            rooms_num,
            floor,
            has_balcony,
            is_penthouse,
            is_villa,
            monthly_municipal_tax,
            deal_state,
    ):
        self.address = address
        self.size_in_sq_meters = size_in_sq_meters
        self.rooms_num = rooms_num
        self.floor = floor
        self.has_balcony = has_balcony
        self.is_penthouse = is_penthouse
        self.is_villa = is_villa
        self.monthly_municipal_tax = monthly_municipal_tax
        self.deal_state = deal_state

    def get_annual_municipal_tax(self):
        return self.monthly_municipal_tax * 12

    def close_deal(self, apartment_status):
        if "rented" in apartment_status:
            return f"Ap is rented"
        else:
            return f"Ap is sold"

    def deal_state(self, status):
        if status == "open":
            return True
        if status == "close":
            return False


class ApartmentForRent(Apartment):
    def __init__(self, address, size_in_sq_meters, rooms_num, floor, has_balcony, rent_price_per_month, is_penthouse,
                 is_villa, monthly_municipal_tax, deal_state, pets_allowed):
        super().__init__(address, size_in_sq_meters, rooms_num, floor, has_balcony, is_penthouse, is_villa,
                         monthly_municipal_tax, deal_state)
        self.rent_price_per_month = rent_price_per_month
        self.pets_allowed = pets_allowed

    def get_annual_rent_price(self):
        return self.rent_price_per_month * 12

    def get_agency_fee(self):
        return self.rent_price_per_month


class ApartmentForSale(Apartment):
    def __init__(self, address, size_in_sq_meters, rooms_num, floor, has_balcony, is_penthouse,
                 is_villa, monthly_municipal_tax, deal_state, sale_price):
        super().__init__(address, size_in_sq_meters, rooms_num, floor, has_balcony, is_penthouse, is_villa,
                         monthly_municipal_tax, deal_state)
        self.sale_price = sale_price

    def get_agency_fee(self):
        return self.sale_price * 0.02


if __name__ == '__main__':
    ap_rent = ApartmentForRent("Rishon", 100, 4, 3, False, 5000, False, False, 1000, "open", False)
    print(ap_rent.get_annual_rent_price())
    ap_sale = ApartmentForSale("TelAviv", 200, 6, 30, True, False, False, 5000, "open", 5_000_000)
    print(ap_sale.get_agency_fee())