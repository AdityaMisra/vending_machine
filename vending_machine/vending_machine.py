from vending_machine.drinks import Drink
from vending_machine.exceptions import DrinkNotFound, IngredientNotFound
from vending_machine.ingredient import Ingredient


class VendingMachine(object):
    def __init__(self):
        self.all_drinks = set()
        self.ingredients = set()
        self.ingredient_names = set()

    def add_new_drink(self, drink_name, ingredient_quantity_tuple):
        for each_drink in self.all_drinks:
            if each_drink.name == drink_name:
                print("Drink already exist! New drink is not created.")
                return each_drink

        ingredients_quantity_mapping = {}

        for ingredient_name, quantity in ingredient_quantity_tuple:
            ingredient = None
            if ingredient_name not in self.ingredient_names:
                ingredient = self.add_ingredient(ingredient_name, 10 * quantity)
            else:
                for _i in self.ingredients:
                    if _i.name == ingredient_name:
                        ingredient = _i
                        break
            ingredients_quantity_mapping.update({ingredient: quantity})

        drink = Drink(drink_name, ingredients_quantity_mapping)
        self.all_drinks.add(drink)
        return drink

    def remove_a_drink(self, drink_name):
        drink_to_remove = None
        for each_drink in self.all_drinks:
            if each_drink.name == drink_name:
                drink_to_remove = each_drink
        if drink_to_remove:
            self.all_drinks.remove(drink_to_remove)
            del drink_to_remove
            return True
        raise DrinkNotFound("{} does not exist in this vending machine".format(drink_name))

    def add_ingredient(self, ingredient_name, total_quantity):
        if ingredient_name in self.ingredient_names:
            for _ingredient in self.ingredients:
                if _ingredient.name == ingredient_name:
                    _ingredient.total_quantity += total_quantity
                    _ingredient.available_quantity += total_quantity
                    return _ingredient

        ingredient = Ingredient(ingredient_name, total_quantity)
        self.ingredients.add(ingredient)
        self.ingredient_names.add(ingredient.name)
        return ingredient

    def remove_ingredient(self, ingredient_name):
        if ingredient_name not in self.ingredient_names:
            IngredientNotFound("{} does not exist in this vending machine".format(ingredient_name))

        ingredient_to_remove = None
        for each_ingredient in self.ingredients:
            if each_ingredient.name == ingredient_name:
                ingredient_to_remove = each_ingredient

        ingredient_to_remove.available_quantity = 0
        return ingredient_to_remove

    def update_ingredient_quantity(self, ingredient_name, new_quantity):
        for each_ingredient in self.ingredients:
            if each_ingredient.name == ingredient_name:
                return each_ingredient.refill_ingredient(new_quantity)

        raise IngredientNotFound("{} does not exist in this vending machine".format(ingredient_name))

    def dispense_drink(self, drink_name):
        for each_drink in self.all_drinks:
            if drink_name == each_drink.name:
                return each_drink.check_and_prepare_drink()
        raise DrinkNotFound("{} does not exist in this vending machine".format(drink_name))

    def show_all_drinks(self):
        for idx, drink in enumerate(self.all_drinks, 1):
            print("{} - {}".format(idx, drink.name))

    def check_ingredient_status(self):
        for ingredient in self.ingredients:
            print("Name: ", ingredient.name, "| Total: ", ingredient.total_quantity,
                  "| Available: ", ingredient.available_quantity, "| Empty: ",
                  ingredient.empty, "| ", ingredient.alert())


def run_test():
    v = VendingMachine()
    v.add_new_drink('tea', (('leaves', 1), ('water', 4), ('sugar', 2)))
    v.show_all_drinks()
    v.check_ingredient_status()
    v.dispense_drink("tea")
    v.check_ingredient_status()
    v.update_ingredient_quantity('leaves', 50)
    v.check_ingredient_status()
    v.add_ingredient('sugar', 30)
    v.add_ingredient('coffee-powder', 100)
    v.check_ingredient_status()
    v.add_new_drink('coffee', (('coffee-powder', 1), ('water', 4), ('sugar', 2),))
    v.check_ingredient_status()
    v.dispense_drink('coffee')
