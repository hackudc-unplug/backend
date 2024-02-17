import datetime


class DateService:
    @staticmethod
    def valid_date(day: int, month: int, year: int) -> bool:
        try:
            date = datetime.datetime(year, month, day)
            min_date = datetime.datetime(2021, 8, 3)
            max_date = datetime.datetime(2023, 8, 8)
            if date < min_date or date > max_date:
                return False
            return True
        except ValueError:
            return False
