import pprint
import requests

class Horoscope:
    horolist = {1: "Aries", 2: "Taurus", 3: "Gemini",
                4: "Cancer", 5: "Leo", 6: "Virgo",
                7: "Libra", 8: "Scorpio", 9: "Sagittarius",
                10: "Capricorn", 11: "Aquarius", 12: "Pisces"}

    days = {1: "yesterday",
            2: "today",
            3: "tomorrow"}
    def __init__(self):
        self.horo_choice = int
        self.day_choice = int

    @staticmethod
    def greet():
        return "Welcome to your daily description horoscope sign!"

    def convert_int_to_day(self):
        return Horoscope.days.get(self.day_choice)

    def convert_int_to_horoscope(self):
        return Horoscope.horolist.get(self.horo_choice)


if __name__ == '__main__':
    horo = Horoscope()
    print(horo.greet())
    horo.horo_choice = int(input("Please insert your horoscope sign by number\n"
                                 " 1 - Aries\n 2 - Taurus\n 3 - Gemini\n 4 - Cancer\n 5 - Leo\n "
                                 "6 - Virgo\n 7 - Libra\n 8 - Scorpio\n 9 - Sagittarius\n"
                                 " 10 - Capricorn\n 11 - Aquarius\n 12 - Pisces "))

    horo.day_choice = int(input("For which day you want to get the info?\n"
                                "1 - yesterday\n"
                                "2 - today\n"
                                "3 - tomorrow "))

    url = "https://sameer-kumar-aztro-v1.p.rapidapi.com/"

    querystring = {"sign": horo.convert_int_to_horoscope(), "day": horo.convert_int_to_day()}

    headers = {
        "X-RapidAPI-Key": "8be027306cmsh17f7924e0e64352p1ac5ecjsnb3d76aef4686",
        "X-RapidAPI-Host": "sameer-kumar-aztro-v1.p.rapidapi.com"
    }

    response = requests.request("POST", url, headers=headers, params=querystring)
    pprint.pprint(response.json()['description'])
