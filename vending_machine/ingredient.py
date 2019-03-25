class Ingredient(object):
    def __init__(self, name, total_quantity, threshold_for_alert=5):
        self.name = name
        self.total_quantity = total_quantity
        self.available_quantity = total_quantity
        self.threshold_for_alert = threshold_for_alert
        self.empty = False

    def alert(self):
        if self.threshold_for_alert >= self.available_quantity:
            return "ALERT!!! {} is running low. Please refill ASAP!".format(self.name)
        return ""

    def use_ingredient(self, quantity):
        if self.empty or quantity > self.available_quantity:
            return False

        self.available_quantity -= quantity

        if not self.available_quantity:
            self.empty = True

        return True

    def is_available(self, quantity):
        print(self.alert())

        if self.empty or quantity > self.available_quantity:
            return False
        return True

    def refill_ingredient(self, quantity):
        if self.available_quantity == self.total_quantity:
            print("No need to refill!")
            return False
        diff = self.total_quantity - self.available_quantity
        if quantity > diff:
            quantity = diff

        self.available_quantity += quantity
        return True
