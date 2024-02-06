
import csv
from inventorymanger import Ingredient

class IngredientRepository:
    def __init__(self, filename: str):
        self.__filename = filename

    def save_ingredients(self, ingredients: list[Ingredient]):
        with open(self.__filename, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["name", "quantity", "unit", "reorder_level"])
            for ingredient in ingredients:
                writer.writerow([ingredient.name, ingredient.quantity, ingredient.unit, ingredient.reorder_level])

    def load_ingredients(self) -> list[Ingredient]:
        ingredients = []
        with open(self.__filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                ingredients.append(Ingredient(
                    name=row["name"],
                    quantity=float(row["quantity"]),
                    unit=row["unit"],
                    reorder_level=int(row["reorder_level"])
                ))
        return ingredients
