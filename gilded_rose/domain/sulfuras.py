from gilded_rose.domain.item import Item
from gilded_rose.domain.quality import Quality
from gilded_rose.domain.sell_in import SellIn


class Sulfuras(Item):
    def __init__(self, name: str, sell_in: SellIn, quality: Quality):
        super().__init__(name, sell_in, quality)

    def update(self):
        pass