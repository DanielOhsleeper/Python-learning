import datetime

class RavKav:
    rides = {'short': {'range': (0, 15), 'price': 5.5},
             'medium': {'range': (16, 40), 'price': 12},
             'long': {'range': (40, 1000), 'price': 23},
             }

    def __init__(self, holder_id: int, holder_name: str):
        self.holder_id = holder_id
        self.holder_name = holder_name
        self.balance = 0
        self.ride_log = {}


    def ride_type(self, km):
        for type, details in RavKav.rides.items():
            if details["range"][0] <= km <= details["range"][1]:
                return type


    def buy_ride(self, km,  date: datetime.date = datetime.date.today()):
        ride = self.ride_type(km)
        price = self.rides[ride]["price"]
        if self.balance < price:
            return f"Not enough money in account"
        self.balance -= price

        if date not in self.ride_log:
            self.ride_log[date] = 0
        self.ride_log[date] += 1




    def holder_id(self):
        return self.holder_id

    def holder_name(self):
        return self.holder_name

    def top_up(self, money_update):
        if money_update > 0:
            self.balance += money_update

    def get_current_balance(self):
        return self.balance

    def get_rides_by_date(self, date: datetime.date):
        return self.ride_log.get(date)



if __name__ == '__main__':
    rav = RavKav(12345, "zaza")
    print(rav.ride_type(1))
    rav.top_up(1000)
    rav.buy_ride(20)
    rav.buy_ride(10)
    print(rav.balance)
    print(rav.get_rides_by_date(datetime.date.today()))