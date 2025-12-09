import decimal
import json

class Laboratory():

    def __init__(self, substances: list[str], reactions: dict):

        if substances == []:
            raise Exception("List can't be empty")

        self.reactions = reactions

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
        print(index)
        quantity = self.stock[index]["quantity"]
        print(self.stock[index])
        return quantity

    def check_decimal_number(self, number: float | int):
        d = decimal.Decimal(str(number))
        if d.as_tuple().exponent < -4:
            raise Exception("The quantity must be rounded to a maximum of four decimal places.")

    def add_reaction_to_stock(self, substance: str):
        self.stock.append(
            {
                "name": substance,
                "quantity": 0
            }
        )
        return (len(self.stock) - 1)

    def check_existent_substance(self, substance: str)->int:
        found_substance = ""
        index = -1
        for s in self.stock:
            index += 1
            if s["name"] == substance:
                return index
        if found_substance == "":
            reaction_index = self.check_substance_in_reactions(substance)
            if reaction_index:
                return reaction_index
            raise Exception("No such substance in stock or reactions")

    def check_substance_in_reactions(self, substance: str):
        for reaction in self.reactions:
            print(reaction)
            if reaction == substance:
                return self.add_reaction_to_stock(reaction)

    def add(self, substance: str, quantity: int)->dict:

        self.check_decimal_number(quantity)
        if (type(quantity) != float and type(quantity) != int) or type(substance) != str:
            raise Exception("The quantity must be a float and substance must be string")
        if quantity < 0:
            raise Exception("Impossible to add negative quantities")

        index = self.check_existent_substance(substance)
        self.stock[index]["quantity"] = quantity
        return self.stock[index]

    def make(self, substance: str, quantity: float | int) -> float | int:
        self.check_decimal_number(quantity)
        if (type(quantity) != float and type(quantity) != int) or type(substance) != str:
            raise Exception("The quantity must be a float and substance must be string")
        if quantity < 0:
            raise Exception("Impossible to add negative quantities")

        index = self.check_existent_substance(substance)
        print(self.reactions[substance])
        ingredients = self.reactions[substance]

        needed_quantities = []
        for name, amount in ingredients:
            needed = amount * quantity
            needed_quantities.append(needed)
            possessed = self.getQuantity(name)
            if possessed < needed:
                raise Exception(f"Not enough {name}, needed {needed}, possessed {possessed}")

        index_ingredients = 0
        for using_name, using_amount in ingredients:
            needed = needed_quantities[index_ingredients]
            index = self.check_existent_substance(using_name)
            self.stock[index]["quantity"] -= needed
            index_ingredients += 1

        self.add(substance, quantity)
        print(self.stock)
        return quantity

substances = ["toto", "tata"]
reactions = {
    "tutu" : [("toto", 1), ("tata", 2)]
}
l = Laboratory(substances, reactions)
l.add("toto", 26)
l.add("tata", 41)

l.make("tutu", 12)