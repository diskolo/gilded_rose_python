from gilded_rose.domain.item import Item
from gilded_rose.domain.quality import Quality
from gilded_rose.domain.sell_in import SellIn


class AgedBrie(Item):

    def __init__(self, name: str, sell_in: SellIn, quality: Quality):
        super().__init__(name, sell_in, quality)

    def update(self):
        self.sell_in = self.sell_in.dicrease()
        if self.sell_in.has_reached_end_date():
            self.quality = self.quality.increase_quality_by_two()
        else:
            self.quality = self.quality.increase_quality()
