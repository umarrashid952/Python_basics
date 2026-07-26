class FruitShop:

    def __init__(self, name, fruitPrices, stock=None, discountPercent=0.0):
        """
            name: Name of the fruit shop

            fruitPrices: Dictionary with keys as fruit
            strings and prices for values e.g.
            {'apples':2.00, 'oranges': 1.50, 'pears': 1.75}

            stock: Optional dictionary with keys as fruit strings and
            values as pounds in stock, e.g. {'apples': 10}. Fruits not
            present in this dictionary are treated as unlimited/untracked.

            discountPercent: Percentage (0-100) taken off the total of
            every order, e.g. 10 for 10% off.
        """
        self.fruitPrices = fruitPrices
        self.name = name
        self.stock = dict(stock) if stock else {}
        self.discountPercent = discountPercent
        print('Welcome to %s fruit shop' % (name))

    def getCostPerPound(self, fruit):
        """
            fruit: Fruit string
        Returns cost of 'fruit', assuming 'fruit'
        is in our inventory or None otherwise
        """
        if fruit not in self.fruitPrices:
            print("Sorry we don't have %s" % (fruit))
            return None
        return self.fruitPrices[fruit]

    def getStock(self, fruit):
        """
            fruit: Fruit string
        Returns pounds of 'fruit' in stock, or None if 'fruit'
        is untracked (treated as unlimited).
        """
        return self.stock.get(fruit)

    def restock(self, fruit, amount):
        """
            fruit: Fruit string
            amount: Pounds to add to stock (must be > 0)

        Adds 'amount' pounds of 'fruit' to stock, tracking 'fruit'
        if it wasn't already tracked.
        """
        if amount <= 0:
            raise ValueError('restock amount must be greater than 0')
        self.stock[fruit] = self.stock.get(fruit, 0) + amount

    def setDiscount(self, percent):
        """
            percent: Discount percentage (0-100) to apply to every order
        """
        if not 0 <= percent <= 100:
            raise ValueError('discount percent must be between 0 and 100')
        self.discountPercent = percent

    def getPriceOfOrder(self, orderList):
        """
            orderList: List of (fruit, numPounds) tuples

        Returns cost of orderList, capped by available stock for any
        tracked fruit and reduced by the shop's current discount.
        """
        totalCost = 0.0
        for fruit, numPounds in orderList:
            costPerPound = self.getCostPerPound(fruit)
            if costPerPound == None:
                continue
            available = self.stock.get(fruit)
            if available is None:
                purchaseAmount = numPounds
            else:
                purchaseAmount = min(numPounds, available)
                if purchaseAmount < numPounds:
                    print('Sorry, only %.2f lbs of %s in stock' % (available, fruit))
                self.stock[fruit] = available - purchaseAmount
            totalCost += purchaseAmount * costPerPound
        return totalCost * (1 - self.discountPercent / 100.0)

    def getName(self):
        return self.name

    def __str__(self):
        return "<FruitShop: %s>" % self.getName()
