import unittest

from shop import FruitShop


class FruitShopTest(unittest.TestCase):

    def setUp(self):
        self.prices = {'apples': 2.00, 'oranges': 1.50, 'pears': 1.75}

    def test_get_cost_per_pound_known_fruit(self):
        shop = FruitShop('Test Shop', self.prices)
        self.assertEqual(shop.getCostPerPound('apples'), 2.00)

    def test_get_cost_per_pound_unknown_fruit_returns_none(self):
        shop = FruitShop('Test Shop', self.prices)
        self.assertIsNone(shop.getCostPerPound('kiwis'))

    def test_get_price_of_order_basic(self):
        shop = FruitShop('Test Shop', self.prices)
        total = shop.getPriceOfOrder([('apples', 2), ('oranges', 1)])
        self.assertAlmostEqual(total, 2 * 2.00 + 1 * 1.50)

    def test_untracked_fruit_has_unlimited_stock(self):
        shop = FruitShop('Test Shop', self.prices)
        self.assertIsNone(shop.getStock('apples'))
        total = shop.getPriceOfOrder([('apples', 100)])
        self.assertAlmostEqual(total, 100 * 2.00)

    def test_restock_new_fruit(self):
        shop = FruitShop('Test Shop', self.prices)
        shop.restock('apples', 5)
        self.assertEqual(shop.getStock('apples'), 5)

    def test_restock_existing_stock(self):
        shop = FruitShop('Test Shop', self.prices, stock={'apples': 3})
        shop.restock('apples', 2)
        self.assertEqual(shop.getStock('apples'), 5)

    def test_restock_invalid_amount_raises(self):
        shop = FruitShop('Test Shop', self.prices)
        with self.assertRaises(ValueError):
            shop.restock('apples', 0)

    def test_order_exceeding_stock_is_capped(self):
        shop = FruitShop('Test Shop', self.prices, stock={'apples': 2})
        total = shop.getPriceOfOrder([('apples', 5)])
        self.assertAlmostEqual(total, 2 * 2.00)
        self.assertEqual(shop.getStock('apples'), 0)

    def test_order_within_stock_decrements_stock(self):
        shop = FruitShop('Test Shop', self.prices, stock={'apples': 5})
        shop.getPriceOfOrder([('apples', 2)])
        self.assertEqual(shop.getStock('apples'), 3)

    def test_discount_set_in_constructor(self):
        shop = FruitShop('Test Shop', self.prices, discountPercent=10)
        total = shop.getPriceOfOrder([('apples', 2)])
        self.assertAlmostEqual(total, 2 * 2.00 * 0.9)

    def test_set_discount(self):
        shop = FruitShop('Test Shop', self.prices)
        shop.setDiscount(50)
        total = shop.getPriceOfOrder([('oranges', 2)])
        self.assertAlmostEqual(total, 2 * 1.50 * 0.5)

    def test_set_discount_invalid_raises(self):
        shop = FruitShop('Test Shop', self.prices)
        with self.assertRaises(ValueError):
            shop.setDiscount(150)

    def test_get_name(self):
        shop = FruitShop('Berkeley Bowl', self.prices)
        self.assertEqual(shop.getName(), 'Berkeley Bowl')

    def test_str(self):
        shop = FruitShop('Berkeley Bowl', self.prices)
        self.assertEqual(str(shop), '<FruitShop: Berkeley Bowl>')


if __name__ == '__main__':
    unittest.main()
