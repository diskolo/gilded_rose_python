from abc import abstractmethod

from gilded_rose.domain.quality import Quality
from gilded_rose.domain.sell_in import SellIn


class Item:
    def __init__(self, name, sell_in: SellIn, quality: Quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    @abstractmethod
    def update(self):
        raise NotImplementedError

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)