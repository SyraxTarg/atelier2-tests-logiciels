import decimal

class Laboratory():

    def __init__(self, substances: list[str]):

        if substances == []:
            raise Exception("List can't be empty")

        self.stock = []

        for s in substances:
            self.stock.append(
                {
                    "name":s,
                    "quantity": 0
                }
            )

    def getQuantity(self, substance: str)-> float:
        index = self.check_existent_substance(substance)

        quantity = self.stock[index]["quantity"]
        return quantity

    def check_decimal_number(self, number: float | int):
        d = decimal.Decimal(str(number))
        if d.as_tuple().exponent < -4:
            raise Exception("The quantity must be rounded to a maximum of four decimal places.")

    def check_existent_substance(self, substance: str)->int:
        found_substance = ""
        index = -1
        for s in self.stock:
            index += 1
            if s["name"] == substance:
                return index
        if found_substance == "":
            raise Exception("No such substance in stock")

    def add(self, substance: str, quantity: int)->dict:

        self.check_decimal_number(quantity)
        if (type(quantity) != float and type(quantity) != int) or type(substance) != str:
            raise Exception("The quantity must be a float and substance must be string")
        if quantity < 0:
            raise Exception("Impossible to add negative quantities")

        index = self.check_existent_substance(substance)
        self.stock[index]["quantity"] = quantity
        return self.stock[index]


substances = [
            "ethanol",
            "copper",
            "bleach",
            "azote",
            "salt",
            "antimatter"
        ]
l = Laboratory(substances)
l.getQuantity("azote")