import unittest

from gilded_rose.gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_update_quality(self):
        items = [
            Item("Aged Brie", 20, 40),
            Item("Backstage passes to a TAFKAL80ETC concert", 12, 30),
            Item("Sulfuras, Hand of Ragnaros", 12, 80)
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in, 19)
        self.assertEqual(items[0].quality, 41)
        self.assertEqual(items[1].sell_in, 11)
        self.assertEqual(items[1].quality, 31)
        self.assertEqual(items[2].sell_in, 12)
        self.assertEqual(items[2].quality, 80)

    def test_update_aged_brie_quality_with_sell_in_zero_update_double_quality(self):
        items = [
            Item("Aged Brie", 1, 40)
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in, 0)
        self.assertEqual(items[0].quality, 42)


    def test_quality_article_is_not_bigger_than_50(self):
        items = [
            Item("Aged Brie", 20, 50),
            Item("Backstage passes to a TAFKAL80ETC concert", 12, 50),
            Item("Sulfuras, Hand of Ragnaros", 12, 80)
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in, 19)
        self.assertEqual(items[0].quality, 50)
        self.assertEqual(items[1].sell_in, 11)
        self.assertEqual(items[1].quality, 50)
        self.assertEqual(items[2].sell_in, 12)
        self.assertEqual(items[2].quality, 80)

    def test_baskstage_dicrease_two_units_if_sell_in_is_equals_to_ten_days(self):
        items = [
            Item("Backstage passes to a TAFKAL80ETC concert", 11, 40)
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in, 10)
        self.assertEqual(items[0].quality, 42)

    def test_baskstage_dicrease_three_units_if_sell_in_is_equals_to_five_days(self):
        items = [
            Item("Backstage passes to a TAFKAL80ETC concert", 6, 40)
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in, 5)
        self.assertEqual(items[0].quality, 43)

    def test_baskstage_dicrease_to_Zero_if_sell_in_date_is_finish(self):
        items = [
            Item("Backstage passes to a TAFKAL80ETC concert", 1, 40)
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in, 0)
        self.assertEqual(items[0].quality, 0)








if __name__ == '__main__':
    unittest.main()