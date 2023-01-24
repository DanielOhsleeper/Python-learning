import datetime


class CountryCalendar:
    def _init__(
            self,
            country_name,
            country_work_days,
            year,
            country_public_holidays,
    ):
        self.country_name = country_name,
        self.country_work_days = {},
        self.year = year,
        self.country_public_holidays = {},



    def place_name(self):
        self.country_name = "USA"
        return self.country_name

    def work_days(self):
        week_days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        return week_days[1:6]

    def year(self):
        today = datetime.datetime.today()
        return today.year

    def public_days(self):
        pass

    def total_working_days(self, from_date: datetime.date, to_date: datetime.date):
            working = [1, 2, 3, 4, 5]
            count = 0
            holidays_usa = [(datetime.date(2023, 1, 1)), (datetime.date(2023, 1, 16)), (datetime.date(2023, 2, 20)),
                            (datetime.date(2023, 5, 29)), (datetime.date(2023, 6, 19)), (datetime.date(2023, 7, 4)), (
                                datetime.date(2023, 9, 4)),
                            (datetime.date(2023, 10, 9)),
                            (datetime.date(2023, 11, 10)),
                            (datetime.date(2023, 11, 23)),
                            (datetime.date(2023, 12, 25))]
            
            d = datetime.timedelta(days=1)
            while from_date <= to_date:
                if from_date.isoweekday() in working and from_date not in holidays_usa:
                    count += 1
                from_date += d
                if from_date in holidays_usa:
                    print(f"{from_date} is holiday")
            return f"{count} working days"

    def total_vacation_days(self, from_date: datetime.date, to_date: datetime.date):
        holi = [0, 6]
        count_holi = 0
        d = datetime.timedelta(days=1)
        while from_date <= to_date:
            if from_date.isoweekday() in holi:
                count_holi += 1
            from_date += d
        return f"{count_holi} vacation days"





    def working_hours(self, from_date: datetime.date, to_date: datetime.date, start: datetime.time
                      , end: datetime.time):

        count_hours = 0
        d = datetime.timedelta(days=1)
        while from_date <= to_date:
            if from_date.isoweekday() <= 5:
                work_time = end - start
                count_hours += work_time
                from_date += d
            return count_hours


if __name__ == '__main__':

# work_hour_start = datetime.datetime.strptime("09:00", "%H:%M")
# end_working_time = datetime.datetime.strptime("19:00", "%H:%M")
    cc = CountryCalendar()

# print(cc.place_name())
# print(cc.vacation_days())
# print(end_working_time - work_hour_start)
print(cc.work_days())
print(cc.year())
print(cc.total_working_days(datetime.date(2023, 1, 1), datetime.date(2023, 2, 24)))
print(cc.total_vacation_days(datetime.date(2023, 1, 1), datetime.date(2023, 2, 24)))
print(cc.working_hours(datetime.date(2023, 1, 1), datetime.date(2023, 2, 24), start=datetime.datetime.strptime("09:00", "%H:%M"),
                       end=datetime.datetime.strptime("19:00", "%H:%M")))


