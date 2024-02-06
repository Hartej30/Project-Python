
import csv
from inventorymanger import InventoryManager
from recipeManager import RecipeManager
from pizzaStore import PizzaMenuItem

class MenuManager:
    def __init__(self):
        self.menu_file = "data/menu_items.csv"
        self.menu = self.load_menu()

    def load_menu(self):
        try:
            with open(self.menu_file, "r") as file:
                return [PizzaMenuItem(**row) for row in csv.DictReader(file)]
        except FileNotFoundError:
            return []

    def save_menu(self):
        with open(self.menu_file, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["name", "description", "price", "size", "recipe", "category"])
            for pizza in self.menu:
                writer.writerow([pizza.name, pizza.description, pizza.price, pizza.size, pizza.recipe, pizza.category])

    def get_menu(self):
        return self.menu

    def add_pizza(self, pizza_name, description, price, size, recipe, category):
        pizza = PizzaMenuItem(name=pizza_name, description=description, price=price, size=size, recipe=recipe, category=category)
        self.menu.append(pizza)
        self.save_menu()