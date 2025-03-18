class SellIn:

    END_DATE = 0
    TEN_DAYS_THRESHOLD = 11
    FIVE_DAYS_THRESHOLD = 6

    def __init__(self, days: int) -> None:
        self.days = days

    def dicrease(self) -> "SellIn":
        if self._is_end_date():
            return SellIn(self.END_DATE)
        return SellIn(self.days - 1)

    def _is_end_date(self):
        return self.days == self.END_DATE

    def has_reached_end_date(self):
        return self.days == self.END_DATE

    def is_equals_or_less_than_five_days(self):
        return self.days < self.FIVE_DAYS_THRESHOLD

    def is_equals_or_less_than_eleven_days(self):
        return self.days < self.TEN_DAYS_THRESHOLD