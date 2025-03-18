from gilded_rose.domain.item import Item
from gilded_rose.domain.quality import Quality
from gilded_rose.domain.sell_in import SellIn


class BackStage(Item):
    def __init__(self, name: str, sell_in: SellIn, quality: Quality):
        super().__init__(name, sell_in, quality)

    def update(self):
        self.sell_in = self.sell_in.dicrease()
        if self.sell_in.has_reached_end_date():
            self.quality = self.quality.to_zero()
        elif self.sell_in.is_equals_or_less_than_five_days():
            self.quality = self.quality.increase_quality_by_three()
        elif self.sell_in.is_equals_or_less_than_eleven_days():
            self.quality = self.quality.increase_quality_by_two()
        else:
            self.quality = self.quality.increase_quality()