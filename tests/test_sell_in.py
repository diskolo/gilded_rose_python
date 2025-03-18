import unittest

from gilded_rose.domain.quality import Quality
from gilded_rose.domain.sell_in import SellIn


class TestSellIn(unittest.TestCase):
    def test_two_sell_in_are_equals(self):
        sell_in_one = SellIn(1)
        sell_in_two = SellIn(1)
        self.assertEqual(sell_in_one, sell_in_two)

    def test_sell_in_not_equals_to_quality(self):
        sell_in = SellIn(1)
        quality = Quality(1)
        self.assertNotEqual(sell_in,quality)

    def test_two_sell_in_with_different_day_are_not_equal(self):
        sell_in_one = SellIn(1)
        sell_in_two = SellIn(2)
        self.assertNotEqual(sell_in_one, sell_in_two)