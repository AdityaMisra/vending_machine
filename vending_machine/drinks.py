class Drink(object):
    def __init__(self, name, ingredients_quantity_mapping):
        self.name = name
        self.ingredients_quantity = ingredients_quantity_mapping
        self.ingredients = ingredients_quantity_mapping.keys()

    def _prepare_drink(self):
        for ingredient, quantity in self.ingredients_quantity.items():
            # we don't have to worry about using some ingredient and then some other ingredient going OOS
            if not ingredient.use_ingredient(quantity):
                print("DRINK cannot be served. Not enough quantity of {} is available for preparing {}".
                      format(ingredient.name, self.name))
                return False
        print("Here you go..! Enjoy your {}!".format(self.name))
        return True

    def can_prepare_drink(self):
        for ingredient, quantity in self.ingredients_quantity.items():
            if not ingredient.is_available(quantity):
                print("DRINK cannot be served. Not enough quantity of {} is available for preparing {}".
                      format(ingredient.name, self.name))
                return False
        return True

    def check_and_prepare_drink(self):
        if self.can_prepare_drink():
            return self._prepare_drink()
