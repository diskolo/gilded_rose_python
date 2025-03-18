from gilded_rose.domain.item import Item
from gilded_rose.domain.quality import Quality
from gilded_rose.domain.sell_in import SellIn


class Conjured(Item):

    def __init__(self, name: str, sell_in: SellIn, quality: Quality) -> None:
        super().__init__(name, sell_in, quality)

    def update(self):
        self.sell_in = self.sell_in.dicrease()
        self.quality = self.quality.dicrease_by_two()
