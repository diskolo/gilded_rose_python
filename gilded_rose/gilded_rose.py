from typing import List

from gilded_rose.domain.item import Item


class GildedRose(object):

    AGED_BRIE = "Aged Brie"
    SULFURAS = "Sulfuras, Hand of Ragnaros"
    BACKSTAGE = "Backstage passes to a TAFKAL80ETC concert"

    def __init__(self, items: List[Item]):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update()



    def _update_backstage_ticket_quality(self, item: Item) -> None:
        if item.sell_in == 0:
            item.quality = 0
        elif item.sell_in < 6:
            self._increase_quality(item, 3)
        elif item.sell_in < 11:
            self._increase_quality(item, 2)
        else:
            self._increase_quality(item, 1)


    @staticmethod
    def _increase_quality(item: Item, units: int) -> None:
        if item.quality + units > 50:
            item.quality = 50
        else:
            item.quality = item.quality + units

    @staticmethod
    def _decrease_sell_in(item) -> None:
        if item.sell_in != 0:
            item.sell_in = item.sell_in -1




