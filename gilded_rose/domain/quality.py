class Quality:

    UNITS_BY_TWO = 2
    UNITS_BY_THREE = 3
    UNITS_BY_ONE = 1
    UNITS_TO_ZERO = 0
    MAX_UNITS = 50

    def __init__(self, units: int) -> None:
        self.units = units

    def increase_quality_by_two(self) -> "Quality":
        if self._has_reached_max_units(self.UNITS_BY_TWO):
            return Quality(self.MAX_UNITS)
        return Quality(self.units + self.UNITS_BY_TWO)

    def increase_quality(self) -> "Quality":
        if self._has_reached_max_units(self.UNITS_BY_ONE):
            return Quality(self.MAX_UNITS)
        return Quality(self.units + self.UNITS_BY_ONE)

    def increase_quality_by_three(self) -> "Quality":
        if self._has_reached_max_units(self.UNITS_BY_THREE):
            return Quality(self.MAX_UNITS)
        return Quality(self.units + self.UNITS_BY_THREE)

    def to_zero(self):
        return Quality(self.UNITS_TO_ZERO)

    def _has_reached_max_units(self, units):
        return self.units + units > self.MAX_UNITS