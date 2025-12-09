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
        found_substance = ""
        index = -1
        for s in self.stock:
            index += 1
            if s["name"] == substance:
                found_substance = s
                break
        if found_substance == "":
            raise Exception("No such substance in stock")

        quantity = self.stock[index]["quantity"]
        return quantity


    def add(self, substance: str, quantity: int)->dict:

        d = decimal.Decimal(str(quantity))
        if d.as_tuple().exponent < -4:
            print(d.as_tuple().exponent)
            raise Exception("The quantity must be rounded to a maximum of four decimal places.")

        if (type(quantity) != float and type(quantity) != int) or type(substance) != str:
            raise Exception("The quantity must be a float and substance must be string")

        if quantity < 0:
            raise Exception("Impossible to add negative quantities")

        found_substance = ""
        index = -1
        for s in self.stock:
            index += 1
            if s["name"] == substance:
                found_substance = s
                break
        if found_substance == "":
            raise Exception("No such substance in stock")

        return {"name": "toto", "quantity": 12}


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