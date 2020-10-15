"""Dessert classes."""


class Cupcake:
    """A cupcake."""

    cache = {}

    def __init__(self, name, flavor, price):
        self.name = name
        self.qty = 0
        self.flavor = flavor
        self.price = price
        self.cache[self.name] = self


    def __repr__(self):
        """Human-readable printout for debugging."""

        return f'<Cupcake name="{self.name}" qty={self.qty}>'
    
    def add_stock(self, amount):
        self.qty += amount

    def sell(self,amount):
        if self.qty == 0:
            print('Sorry, these cupcakes are sold out')
        elif self.qty < amount:
            self.qty = 0 
        else:
            self.qty -= amount

    
    @staticmethod
    def scale_recipe(ingredients, amount):

        ingredient_list = []

        for ingredient in ingredients:
            ingredient = (ingredient[0], ingredient[1] * amount)
            ingredient_list.append(ingredient)
        
        return ingredient_list

    #Cupcake.scale_recipe([('flour', 1), ('eggs', 3)], 2)

    @classmethod
    def get(cls, name):
        if name in cls.cache:
            return cls.cache[name]
        else:
            print("Sorry, that cupcake doesn't exist")

    #Cupcake.get('test')

class Brownie(Cupcake):
    flavor = 'chocolate'

    def __init__(self, name, price):
        super().__init__(name, "chocolate", price)


if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
