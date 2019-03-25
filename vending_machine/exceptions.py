class VendingMachineException(Exception):
    def __init__(self, message=None):
        self.message = message

    def __str__(self):
        return "Exception: message - {}".format(self.message)


class DrinkNotFound(VendingMachineException):
    pass


class IngredientNotFound(VendingMachineException):
    pass
