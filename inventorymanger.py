import csv
class Ingredient:
    def __init__(self, name: str, quantity: float, unit: str, reorder_level: int):
        self.name = name
        self.quantity = quantity
        self.unit = unit
        self.reorder_level = reorder_level

class InventoryManager:
    def __init__(self):
        self.inventory_file = "data/inventory.csv"
        self.inventory = self.load_inventory()
    
    def load_inventory(self):
        try:
            with open(self.inventory_file, newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                return [Ingredient(*row) for row in reader]
        except FileNotFoundError:
            return []

    def save_inventory(self):
        with open(self.inventory_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows([(ingredient.name, ingredient.quantity, ingredient.unit, ingredient.reorder_level)
                              for ingredient in self.inventory])

    

    def get_inventory(self):
        return self.inventory

    def add_ingredient(self, ingredient_name, quantity):
        ingredient = Ingredient(ingredient_name, float(quantity), "unit", 10)  # Set default values as needed
        self.inventory.append(ingredient)
        self.save_inventory()

    def remove_ingredient(self, ingredient: str, quantity: float):
        if ingredient in self.__ingredients:
            if quantity >= self.__ingredients[ingredient].quantity:
                del self.__ingredients[ingredient]
            else:
                self.__ingredients[ingredient].quantity -= quantity

    def use_ingredient(self, recipe: dict[str, int], pizza_recipe=None):
        if pizza_recipe is None:
            raise Exception("Missing pizza_recipe argument")
        for ingredient_name, quantity in recipe.items():
            if ingredient_name in self.__ingredients:
                self.__ingredients[ingredient_name].quantity -= quantity
            else:
                # Add missing ingredient to inventory if not already present
                missing_ingredient = pizza_recipe.get_ingredient(ingredient_name)
                if missing_ingredient:
                    self.add_ingredient(missing_ingredient)
                    self.use_ingredient({ingredient_name: quantity}, pizza_recipe)
                else:
                    raise Exception(f"Missing ingredient '{ingredient_name}'")

    def check_reorder_levels(self):
        return [
            ingredient.name
            for ingredient in self.__ingredients.values()
            if ingredient.quantity < ingredient.reorder_level
        ]

    def print_inventory(self):
        print("Inventory:")
        for ingredient in self.__ingredients.values():
            print(f"{ingredient.name}: {ingredient.quantity} {ingredient.unit}")

    def display(self):
        print(self)

class IngredientRepository:
    def __init__(self, filename: str):
        self.__filename = filename

    def save_ingredients(self, ingredients: list[Ingredient]):
        with open(self.__filename, "w") as file:
            for ingredient in ingredients:
                file.write(f"{ingredient.name},{ingredient.quantity},{ingredient.unit},{ingredient.reorder_level}\n")

    def load_ingredients(self) -> list[Ingredient]:
        ingredients = []
        with open(self.__filename, "r") as file:
            for line in file.readlines():
                name, quantity, unit, reorder_level = line.strip().split(",")
                ingredients.append(Ingredient(name, float(quantity), unit, int(reorder_level)))
        return ingredients