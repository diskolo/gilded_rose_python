import unittest

from gilded_rose.domain.aged_brie import AgedBrie
from gilded_rose.domain.backstage import BackStage
from gilded_rose.domain.quality import Quality
from gilded_rose.domain.sell_in import SellIn
from gilded_rose.domain.sulfuras import Sulfuras
from gilded_rose.gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_update_quality(self):
        items = [
            AgedBrie("Aged Brie", SellIn(20), Quality(40)),
            BackStage("Backstage passes to a TAFKAL80ETC concert", SellIn(12), Quality(30)),
            Sulfuras("Sulfuras, Hand of Ragnaros", SellIn(12), Quality(80))
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in.days, 19)
        self.assertEqual(items[0].quality.units, 41)
        self.assertEqual(items[1].sell_in.days, 11)
        self.assertEqual(items[1].quality.units, 31)
        self.assertEqual(items[2].sell_in.days, 12)
        self.assertEqual(items[2].quality.units, 80)

    def test_update_aged_brie_quality_with_sell_in_zero_update_double_quality(self):
        items = [
            AgedBrie("Aged Brie",SellIn(1), Quality(40))
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in.days, 0)
        self.assertEqual(items[0].quality.units, 42)


    def test_quality_article_is_not_bigger_than_50(self):
        items = [
            AgedBrie("Aged Brie", SellIn(20), Quality(50)),
            BackStage("Backstage passes to a TAFKAL80ETC concert", SellIn(12), Quality(50)),
            Sulfuras("Sulfuras, Hand of Ragnaros", SellIn(12), Quality(80))
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in.days, 19)
        self.assertEqual(items[0].quality.units, 50)
        self.assertEqual(items[1].sell_in.days, 11)
        self.assertEqual(items[1].quality.units, 50)
        self.assertEqual(items[2].sell_in.days, 12)
        self.assertEqual(items[2].quality.units, 80)

    def test_baskstage_dicrease_two_units_if_sell_in_is_equals_to_ten_days(self):
        items = [
            BackStage("Backstage passes to a TAFKAL80ETC concert", SellIn(11), Quality(40))
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in.days, 10)
        self.assertEqual(items[0].quality.units, 42)

    def test_baskstage_dicrease_three_units_if_sell_in_is_equals_to_five_days(self):
        items = [
            BackStage("Backstage passes to a TAFKAL80ETC concert", SellIn(6), Quality(40))
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in.days, 5)
        self.assertEqual(items[0].quality.units, 43)

    def test_baskstage_dicrease_to_zero_if_sell_in_date_is_finished(self):
        items = [
            BackStage("Backstage passes to a TAFKAL80ETC concert", SellIn(1), Quality(40))
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in.days, 0)
        self.assertEqual(items[0].quality.units, 0)








if __name__ == '__main__':
    unittest.main()