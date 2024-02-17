import datetime


class DateService:
    @staticmethod
    def valid_date(day: int, month: int, year: int) -> bool:
        try:
            datetime.datetime(year, month, day)
            return True
        except ValueError:
            return False
